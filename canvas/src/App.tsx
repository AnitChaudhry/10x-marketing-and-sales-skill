import { Tldraw, TLComponents, Editor, getSnapshot, loadSnapshot, createShapeId } from 'tldraw'
import 'tldraw/tldraw.css'
import { useMemo, useCallback, useRef, useEffect, useState } from 'react'
import { SkillNodeShapeUtil } from './nodes/SkillNodeShapeUtil'
import { ConnectionShapeUtil } from './connection/ConnectionShapeUtil'
import { WorkflowToolbar } from './components/WorkflowToolbar'
import { WorkflowSidebar } from './components/WorkflowSidebar'
import { TemplatesPanel } from './components/TemplatesPanel'
import { NodeConfigPanel } from './components/NodeConfigPanel'
import { Minimap } from './components/Minimap'
import { DottedGrid } from './components/DottedGrid'
import { ConnectionDragger } from './components/ConnectionDragger'
import { ExportControls } from './components/ExportControls'
import './App.css'

// Custom shape utilities for our workflow nodes
const customShapeUtils = [SkillNodeShapeUtil, ConnectionShapeUtil]

// Storage key for auto-save
const STORAGE_KEY = '10x-team-canvas-snapshot'
const AUTO_SAVE_DELAY = 2000 // 2 seconds debounce
const COMMAND_POLL_INTERVAL = 500 // Poll every 500ms

// Canvas command interface
interface CanvasCommand {
  id: string
  type: 'add-node' | 'add-connection' | 'clear' | 'load-workflow' | 'run-simulation'
  payload: Record<string, unknown>
  timestamp: number
}

// Skill type colors
const SKILL_COLORS: Record<string, string> = {
  discovery: '#9333ea',
  linkedin: '#0077b5',
  twitter: '#1da1f2',
  instagram: '#e4405f',
  email: '#22c55e',
  delay: '#6b7280',
  condition: '#eab308',
}

function CanvasOverlay() {
  return (
    <>
      <WorkflowSidebar />
      <TemplatesPanel />
      <NodeConfigPanel />
      <Minimap />
      <ConnectionDragger />
      <ExportControls />
    </>
  )
}

function App() {
  const editorRef = useRef<Editor | null>(null)
  const saveTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const lastCommandIdRef = useRef<string>('')
  const pollIntervalRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const [claudeConnected, setClaudeConnected] = useState(false)
  const nodeIdMapRef = useRef<Map<string, string>>(new Map())

  const components: TLComponents = useMemo(
    () => ({
      Toolbar: WorkflowToolbar,
      InFrontOfTheCanvas: CanvasOverlay,
      Background: DottedGrid,
    }),
    []
  )

  // Execute a single canvas command
  const executeCommand = useCallback((command: CanvasCommand, editor: Editor) => {
    console.log(`Executing command: ${command.type}`, command.payload)

    switch (command.type) {
      case 'clear': {
        // Delete all shapes
        const allShapeIds = editor.getCurrentPageShapeIds()
        if (allShapeIds.size > 0) {
          editor.deleteShapes([...allShapeIds])
        }
        nodeIdMapRef.current.clear()
        console.log('Canvas cleared')
        break
      }

      case 'add-node': {
        const { id, skillType, label, description, x, y, config } = command.payload as {
          id: string
          skillType: string
          label: string
          description: string
          x: number
          y: number
          config: Record<string, unknown>
        }

        const shapeId = createShapeId()
        nodeIdMapRef.current.set(id, shapeId)

        editor.createShape({
          id: shapeId,
          type: 'skill-node',
          x: x || 200,
          y: y || 200,
          props: {
            skillType: skillType || 'discovery',
            label: label || 'New Node',
            description: description || '',
            color: SKILL_COLORS[skillType] || '#9333ea',
            config: config || {},
            inputs: [],
            outputs: [],
          },
        })

        console.log(`Added node: ${label} (${skillType}) at (${x}, ${y})`)
        break
      }

      case 'add-connection': {
        const { from, to, fromX, fromY, toX, toY } = command.payload as {
          from: string
          to: string
          fromX: number
          fromY: number
          toX: number
          toY: number
        }

        const fromShapeId = nodeIdMapRef.current.get(from)
        const toShapeId = nodeIdMapRef.current.get(to)

        if (fromShapeId && toShapeId) {
          const connectionId = createShapeId()
          editor.createShape({
            id: connectionId,
            type: 'workflow-connection',
            x: Math.min(fromX, toX),
            y: Math.min(fromY, toY),
            props: {
              fromId: fromShapeId,
              toId: toShapeId,
              fromX: fromX,
              fromY: fromY,
              toX: toX,
              toY: toY,
            },
          })
          console.log(`Added connection: ${from} -> ${to}`)
        } else {
          console.warn(`Could not find nodes for connection: ${from} -> ${to}`)
        }
        break
      }

      case 'run-simulation': {
        // Trigger simulation by dispatching a custom event
        window.dispatchEvent(new CustomEvent('run-simulation'))
        console.log('Simulation triggered')
        break
      }

      default:
        console.warn(`Unknown command type: ${command.type}`)
    }
  }, [])

  // Poll for commands from Claude Code
  const pollCommands = useCallback(async (editor: Editor) => {
    try {
      const response = await fetch(`/api/canvas/commands?lastId=${lastCommandIdRef.current}`)
      if (response.ok) {
        const data = await response.json()
        const commands: CanvasCommand[] = data.commands || []

        if (commands.length > 0) {
          setClaudeConnected(true)
          console.log(`Received ${commands.length} commands from Claude Code`)

          // Execute each command with a small delay for visual effect
          for (let i = 0; i < commands.length; i++) {
            const cmd = commands[i]
            setTimeout(() => {
              executeCommand(cmd, editor)
            }, i * 300) // 300ms delay between commands for visual effect
            lastCommandIdRef.current = cmd.id
          }
        }
      }
    } catch (error) {
      // Silently fail - canvas might not have API server running
    }
  }, [executeCommand])

  // Auto-save function with debouncing
  const autoSave = useCallback((editor: Editor) => {
    if (saveTimeoutRef.current) {
      clearTimeout(saveTimeoutRef.current)
    }

    saveTimeoutRef.current = setTimeout(() => {
      try {
        const snapshot = getSnapshot(editor.store)
        localStorage.setItem(STORAGE_KEY, JSON.stringify(snapshot))
        console.log('Auto-saved canvas')
      } catch (error) {
        console.error('Auto-save failed:', error)
      }
    }, AUTO_SAVE_DELAY)
  }, [])

  // Load saved canvas on mount
  const handleMount = useCallback((editor: Editor) => {
    editorRef.current = editor

    // Set up initial canvas
    editor.updateInstanceState({ isDebugMode: false })

    // Try to load saved snapshot
    try {
      const savedData = localStorage.getItem(STORAGE_KEY)
      if (savedData) {
        const snapshot = JSON.parse(savedData)
        loadSnapshot(editor.store, snapshot)
        console.log('Loaded saved canvas')
      }
    } catch (error) {
      console.error('Failed to load saved canvas:', error)
    }

    // Set up auto-save listener
    const unsubscribe = editor.store.listen((entry) => {
      if (entry.source === 'user') {
        autoSave(editor)
      }
    })

    // Start polling for Claude Code commands
    pollIntervalRef.current = setInterval(() => {
      pollCommands(editor)
    }, COMMAND_POLL_INTERVAL)

    // Welcome message in console
    console.log(`
╔══════════════════════════════════════════════════════════════╗
║             10x-Team Visual Workflow Canvas                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  DRAG-TO-CONNECT:                                            ║
║  • Drag from green ▶ (output) to blue ◀ (input)              ║
║  • Or click output, then click input                         ║
║                                                              ║
║  FEATURES:                                                   ║
║  • Auto-save enabled - your work is preserved                ║
║  • Export as PNG/SVG from bottom-right controls              ║
║  • Load workflow templates from Templates panel              ║
║  • Drag panels anywhere on the canvas                        ║
║                                                              ║
║  CLAUDE CODE INTEGRATION:                                    ║
║  • Claude Code can create workflows visually!                ║
║  • Use /workflow create in Claude Code                       ║
║  • Watch the canvas build your workflow in real-time         ║
║                                                              ║
║  WORKFLOW EXECUTION:                                         ║
║  • Click ▶ Run to save workflow                              ║
║  • Say "/workflow run" in Claude Code                        ║
║                                                              ║
║  Powered by Claude Code + TLDraw + Browser-Use MCP           ║
╚══════════════════════════════════════════════════════════════╝
    `)

    return () => {
      unsubscribe()
      if (saveTimeoutRef.current) {
        clearTimeout(saveTimeoutRef.current)
      }
      if (pollIntervalRef.current) {
        clearInterval(pollIntervalRef.current)
      }
    }
  }, [autoSave, pollCommands])

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (saveTimeoutRef.current) {
        clearTimeout(saveTimeoutRef.current)
      }
      if (pollIntervalRef.current) {
        clearInterval(pollIntervalRef.current)
      }
    }
  }, [])

  return (
    <div style={{ position: 'fixed', inset: 0 }}>
      <Tldraw
        shapeUtils={customShapeUtils}
        components={components}
        onMount={handleMount}
      />
    </div>
  )
}

export default App
