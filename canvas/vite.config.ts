import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs'
import path from 'path'

// Command queue for Claude Code to control the canvas
interface CanvasCommand {
  id: string
  type: 'add-node' | 'add-connection' | 'clear' | 'load-workflow' | 'run-simulation'
  payload: Record<string, unknown>
  timestamp: number
}

let commandQueue: CanvasCommand[] = []
let lastProcessedId = ''

// Plugin to handle workflow saving and canvas control API
function workflowSavePlugin(): Plugin {
  return {
    name: 'workflow-save',
    configureServer(server) {
      // CORS middleware for all /api routes
      server.middlewares.use((req, res, next) => {
        if (req.url?.startsWith('/api')) {
          res.setHeader('Access-Control-Allow-Origin', '*')
          res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
          res.setHeader('Access-Control-Allow-Headers', 'Content-Type')
          if (req.method === 'OPTIONS') {
            res.writeHead(204)
            res.end()
            return
          }
        }
        next()
      })

      // ============================================
      // CANVAS CONTROL API - For Claude Code
      // ============================================

      // POST /api/canvas/command - Add a command to the queue
      server.middlewares.use('/api/canvas/command', (req, res) => {
        if (req.method === 'POST') {
          let body = ''
          req.on('data', (chunk) => { body += chunk.toString() })
          req.on('end', () => {
            try {
              const command = JSON.parse(body) as Omit<CanvasCommand, 'id' | 'timestamp'>
              const fullCommand: CanvasCommand = {
                ...command,
                id: `cmd-${Date.now()}-${Math.random().toString(36).slice(2, 9)}`,
                timestamp: Date.now(),
              }
              commandQueue.push(fullCommand)
              console.log(`Canvas command queued: ${command.type}`)
              res.writeHead(200, { 'Content-Type': 'application/json' })
              res.end(JSON.stringify({ success: true, commandId: fullCommand.id }))
            } catch (error) {
              res.writeHead(400, { 'Content-Type': 'application/json' })
              res.end(JSON.stringify({ success: false, error: String(error) }))
            }
          })
        } else {
          res.writeHead(405)
          res.end()
        }
      })

      // GET /api/canvas/commands - Poll for pending commands
      server.middlewares.use('/api/canvas/commands', (req, res) => {
        if (req.method === 'GET') {
          const url = new URL(req.url || '', `http://${req.headers.host}`)
          const lastId = url.searchParams.get('lastId') || ''

          // Get commands after lastId
          const startIdx = lastId ? commandQueue.findIndex(c => c.id === lastId) + 1 : 0
          const pending = commandQueue.slice(startIdx)

          res.writeHead(200, { 'Content-Type': 'application/json' })
          res.end(JSON.stringify({ commands: pending }))
        } else {
          res.writeHead(405)
          res.end()
        }
      })

      // POST /api/canvas/clear-commands - Clear processed commands
      server.middlewares.use('/api/canvas/clear-commands', (req, res) => {
        if (req.method === 'POST') {
          commandQueue = []
          res.writeHead(200, { 'Content-Type': 'application/json' })
          res.end(JSON.stringify({ success: true }))
        } else {
          res.writeHead(405)
          res.end()
        }
      })

      // POST /api/canvas/workflow - Create a complete workflow (convenience endpoint)
      server.middlewares.use('/api/canvas/workflow', (req, res) => {
        if (req.method === 'POST') {
          let body = ''
          req.on('data', (chunk) => { body += chunk.toString() })
          req.on('end', () => {
            try {
              const workflow = JSON.parse(body)

              // Clear command
              commandQueue.push({
                id: `cmd-${Date.now()}-clear`,
                type: 'clear',
                payload: {},
                timestamp: Date.now(),
              })

              // Add node commands with proper positioning
              const nodes = workflow.nodes || workflow.steps || []
              const nodePositions: Record<string, { x: number; y: number }> = {}

              nodes.forEach((node: Record<string, unknown>, index: number) => {
                const x = 200 + (index % 4) * 280
                const y = 150 + Math.floor(index / 4) * 200
                const nodeId = (node.id as string) || `node-${index}`
                nodePositions[nodeId] = { x, y }

                commandQueue.push({
                  id: `cmd-${Date.now()}-node-${index}`,
                  type: 'add-node',
                  payload: {
                    id: nodeId,
                    skillType: node.skill || node.skillType || 'discovery',
                    label: node.label || node.name || `Step ${index + 1}`,
                    description: node.description || '',
                    x,
                    y,
                    config: node.config || {},
                  },
                  timestamp: Date.now() + index,
                })
              })

              // Add connection commands
              const connections = workflow.connections || []
              connections.forEach((conn: Record<string, unknown>, index: number) => {
                const fromPos = nodePositions[conn.from as string] || { x: 200, y: 200 }
                const toPos = nodePositions[conn.to as string] || { x: 400, y: 200 }

                commandQueue.push({
                  id: `cmd-${Date.now()}-conn-${index}`,
                  type: 'add-connection',
                  payload: {
                    from: conn.from,
                    to: conn.to,
                    fromX: fromPos.x + 240,
                    fromY: fromPos.y + 40,
                    toX: toPos.x,
                    toY: toPos.y + 40,
                  },
                  timestamp: Date.now() + 1000 + index,
                })
              })

              console.log(`Workflow queued: ${nodes.length} nodes, ${connections.length} connections`)
              res.writeHead(200, { 'Content-Type': 'application/json' })
              res.end(JSON.stringify({
                success: true,
                nodesQueued: nodes.length,
                connectionsQueued: connections.length,
              }))
            } catch (error) {
              res.writeHead(400, { 'Content-Type': 'application/json' })
              res.end(JSON.stringify({ success: false, error: String(error) }))
            }
          })
        } else {
          res.writeHead(405)
          res.end()
        }
      })

      // GET /api/canvas/status - Check if canvas is running
      server.middlewares.use('/api/canvas/status', (req, res) => {
        if (req.method === 'GET') {
          res.writeHead(200, { 'Content-Type': 'application/json' })
          res.end(JSON.stringify({
            running: true,
            queueLength: commandQueue.length,
            timestamp: Date.now(),
          }))
        } else {
          res.writeHead(405)
          res.end()
        }
      })

      // ============================================
      // WORKFLOW SAVE API (existing)
      // ============================================

      server.middlewares.use('/api/save-workflow', (req, res) => {
        if (req.method === 'POST') {
          let body = ''
          req.on('data', (chunk) => {
            body += chunk.toString()
          })
          req.on('end', () => {
            try {
              const workflow = JSON.parse(body)

              // Project root directory (parent of canvas)
              const projectRoot = path.resolve(__dirname, '..')
              const outputDir = path.resolve(projectRoot, 'output')
              const workflowDir = path.resolve(outputDir, 'workflows')

              // Ensure directories exist
              if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true })
              if (!fs.existsSync(workflowDir)) fs.mkdirSync(workflowDir, { recursive: true })

              // Create a readable filename with timestamp
              const date = new Date()
              const timestamp = date.toISOString().replace(/[:.]/g, '-').slice(0, 19)
              const filename = `workflow-${timestamp}.json`
              const filepath = path.join(workflowDir, filename)

              // Save workflow with timestamp
              fs.writeFileSync(filepath, JSON.stringify(workflow, null, 2))

              // Also save as latest.json for easy access by Claude Code
              const latestPath = path.join(workflowDir, 'latest.json')
              fs.writeFileSync(latestPath, JSON.stringify(workflow, null, 2))

              // Also save to project root for quick access
              const rootPath = path.join(projectRoot, 'workflow.json')
              fs.writeFileSync(rootPath, JSON.stringify(workflow, null, 2))

              console.log(`Workflow saved: ${filepath}`)
              console.log(`Steps: ${workflow.steps?.length || 0}`)

              res.writeHead(200, { 'Content-Type': 'application/json' })
              res.end(JSON.stringify({
                success: true,
                file: filename,
                path: filepath,
                rootPath: rootPath,
                steps: workflow.steps?.length || 0,
              }))
            } catch (error) {
              console.error('Workflow save error:', error)
              res.writeHead(400, { 'Content-Type': 'application/json' })
              res.end(JSON.stringify({ success: false, error: String(error) }))
            }
          })
        } else {
          res.writeHead(405, { 'Content-Type': 'application/json' })
          res.end(JSON.stringify({ error: 'Method not allowed' }))
        }
      })
    }
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), workflowSavePlugin()],
})
