import { useEditor, createShapeId, TLShapeId, track } from 'tldraw'
import { useState, useCallback, useEffect } from 'react'

type SkillType = 'discovery' | 'linkedin' | 'twitter' | 'instagram' | 'gmail' | 'workflow' | 'template' | 'audience' | 'campaign'

const skills: Array<{
  type: SkillType
  label: string
  icon: string
  inputs: string[]
  outputs: string[]
}> = [
  { type: 'discovery', label: 'Discovery', icon: '🔍', inputs: ['query'], outputs: ['people'] },
  { type: 'audience', label: 'Audience', icon: '👥', inputs: [], outputs: ['filters'] },
  { type: 'linkedin', label: 'LinkedIn', icon: '💼', inputs: ['person'], outputs: ['sent'] },
  { type: 'twitter', label: 'Twitter', icon: '🐦', inputs: ['person'], outputs: ['sent'] },
  { type: 'instagram', label: 'Instagram', icon: '📸', inputs: ['person'], outputs: ['sent'] },
  { type: 'gmail', label: 'Gmail', icon: '📧', inputs: ['person', 'template'], outputs: ['sent'] },
  { type: 'template', label: 'Template', icon: '📝', inputs: ['context'], outputs: ['message'] },
  { type: 'campaign', label: 'Campaign', icon: '🚀', inputs: ['audience'], outputs: ['results'] },
]

const descriptions: Record<string, string> = {
  discovery: 'Find people using Exa AI',
  audience: 'Define target audience',
  linkedin: 'LinkedIn automation',
  twitter: 'Twitter/X automation',
  instagram: 'Instagram automation',
  gmail: 'Send emails via Gmail',
  template: 'Message template',
  workflow: 'Multi-step sequence',
  campaign: 'Outreach campaign',
}

interface PortClickData {
  nodeId: TLShapeId
  portType: 'input' | 'output'
  nodeLabel: string
}

// Use track() to make this component reactive to editor changes
export const WorkflowToolbar = track(function WorkflowToolbar() {
  const editor = useEditor()
  const [connectMode, setConnectMode] = useState(false)
  const [sourcePort, setSourcePort] = useState<PortClickData | null>(null)
  const [isRunning, setIsRunning] = useState(false)
  const [isSimulating, setIsSimulating] = useState(false)
  const [isPreviewing, setIsPreviewing] = useState(false)

  // Listen for port clicks from nodes
  useEffect(() => {
    const handlePortClick = (e: CustomEvent<PortClickData>) => {
      const { nodeId, portType, nodeLabel } = e.detail

      if (!sourcePort) {
        // First click - must be output port (source)
        if (portType === 'output') {
          setSourcePort({ nodeId, portType, nodeLabel })
          setConnectMode(true)
        } else {
          // Clicked input first, ignore or show hint
          console.log('Click OUTPUT port (green ▶) first to start connection')
        }
      } else {
        // Second click - must be input port (target) on different node
        if (portType === 'input' && nodeId !== sourcePort.nodeId) {
          createConnection(sourcePort.nodeId, nodeId)
          setSourcePort(null)
          setConnectMode(false)
        } else if (portType === 'output') {
          // Clicked another output, switch source
          setSourcePort({ nodeId, portType, nodeLabel })
        } else {
          console.log('Click INPUT port (blue ◀) on a different node to complete connection')
        }
      }
    }

    window.addEventListener('port-click', handlePortClick as EventListener)
    return () => window.removeEventListener('port-click', handlePortClick as EventListener)
  }, [sourcePort])

  const addSkillNode = useCallback((skill: typeof skills[0]) => {
    const viewportCenter = editor.getViewportScreenCenter()
    const pagePoint = editor.screenToPage(viewportCenter)

    const newId = createShapeId()
    editor.createShape({
      id: newId,
      type: 'skill-node' as any,
      x: pagePoint.x - 100,
      y: pagePoint.y - 60,
      props: {
        w: 200,
        h: 120,
        skillType: skill.type,
        label: skill.label,
        description: descriptions[skill.type] || 'Custom node',
        status: 'idle',
        inputs: skill.inputs,
        outputs: skill.outputs,
        config: {},
      },
    })

    // Select the new node
    editor.select(newId)
  }, [editor])

  const createConnection = useCallback((fromId: TLShapeId, toId: TLShapeId) => {
    const fromShape = editor.getShape(fromId) as any
    const toShape = editor.getShape(toId) as any
    if (!fromShape || !toShape) {
      console.error('Cannot find shapes for connection')
      return
    }

    // Calculate connection points - right side of source, left side of target
    const fromX = fromShape.x + (fromShape.props?.w || 200)
    const fromY = fromShape.y + (fromShape.props?.h || 120) / 2
    const toX = toShape.x
    const toY = toShape.y + (toShape.props?.h || 120) / 2

    editor.createShape({
      id: createShapeId(),
      type: 'connection' as any,
      x: 0,
      y: 0,
      props: {
        start: { x: fromX, y: fromY },
        end: { x: toX, y: toY },
        fromNodeId: fromId,
        toNodeId: toId,
        label: '',
      },
    })

    console.log(`Connected: ${fromShape.props.label} → ${toShape.props.label}`)
  }, [editor])

  // Update connections when nodes move
  const updateConnections = useCallback(() => {
    const shapes = editor.getCurrentPageShapes() as any[]
    const connections = shapes.filter((s: any) => s.type === 'connection')

    connections.forEach((conn: any) => {
      const fromShape = editor.getShape(conn.props.fromNodeId) as any
      const toShape = editor.getShape(conn.props.toNodeId) as any

      if (fromShape && toShape) {
        const fromX = fromShape.x + (fromShape.props?.w || 200)
        const fromY = fromShape.y + (fromShape.props?.h || 120) / 2
        const toX = toShape.x
        const toY = toShape.y + (toShape.props?.h || 120) / 2

        if (
          conn.props.start.x !== fromX ||
          conn.props.start.y !== fromY ||
          conn.props.end.x !== toX ||
          conn.props.end.y !== toY
        ) {
          editor.updateShape({
            id: conn.id,
            type: 'connection' as any,
            props: {
              ...conn.props,
              start: { x: fromX, y: fromY },
              end: { x: toX, y: toY },
            },
          })
        }
      }
    })
  }, [editor])

  // Register shape change handler for updating connections
  useEffect(() => {
    const cleanup = editor.sideEffects.registerAfterChangeHandler('shape', (prev: any, next: any) => {
      if (next.type === 'skill-node') {
        requestAnimationFrame(updateConnections)
      }
    })
    return cleanup
  }, [editor, updateConnections])

  // Build ordered workflow steps from connections
  const buildOrderedWorkflow = useCallback(() => {
    const shapes = editor.getCurrentPageShapes() as any[]
    const nodes = shapes.filter((s: any) => s.type === 'skill-node')
    const connections = shapes.filter((s: any) => s.type === 'connection')

    if (nodes.length === 0) return null

    // Build adjacency map
    const outgoing = new Map<string, string[]>()
    const incoming = new Map<string, string[]>()

    nodes.forEach((n: any) => {
      outgoing.set(n.id, [])
      incoming.set(n.id, [])
    })

    connections.forEach((c: any) => {
      const from = c.props.fromNodeId
      const to = c.props.toNodeId
      if (from && to) {
        outgoing.get(from)?.push(to)
        incoming.get(to)?.push(from)
      }
    })

    // Find start nodes (no incoming connections)
    const startNodes = nodes.filter((n: any) => incoming.get(n.id)?.length === 0)

    // Topological sort to get execution order
    const visited = new Set<string>()
    const orderedNodes: any[] = []

    const visit = (nodeId: string) => {
      if (visited.has(nodeId)) return
      visited.add(nodeId)

      // Visit all nodes that this node connects to
      const targets = outgoing.get(nodeId) || []
      targets.forEach((targetId) => {
        // Only visit if all incoming connections have been visited
        const incomingNodes = incoming.get(targetId) || []
        if (incomingNodes.every((id) => visited.has(id))) {
          visit(targetId)
        }
      })
    }

    // Start from nodes with no incoming connections
    startNodes.forEach((n: any) => visit(n.id))

    // Build ordered list based on BFS
    const queue = [...startNodes]
    const seen = new Set<string>()

    while (queue.length > 0) {
      const node = queue.shift()!
      if (seen.has(node.id)) continue
      seen.add(node.id)
      orderedNodes.push(node)

      const targets = outgoing.get(node.id) || []
      targets.forEach((targetId) => {
        const targetNode = nodes.find((n: any) => n.id === targetId)
        if (targetNode && !seen.has(targetId)) {
          queue.push(targetNode)
        }
      })
    }

    // Add any unconnected nodes at the end
    nodes.forEach((n: any) => {
      if (!seen.has(n.id)) {
        orderedNodes.push(n)
      }
    })

    return {
      nodes: orderedNodes,
      connections,
      nodeMap: new Map(nodes.map((n: any) => [n.id, n])),
    }
  }, [editor])

  const exportWorkflow = async () => {
    const workflowData = buildOrderedWorkflow()

    if (!workflowData || workflowData.nodes.length === 0) {
      alert('No nodes to run! Add some skill nodes first.')
      return
    }

    const { nodes, connections } = workflowData

    // Build workflow with ordered steps
    const workflow = {
      name: '10x-Team Workflow',
      version: '1.0',
      created: new Date().toISOString(),
      steps: nodes.map((n: any, index: number) => ({
        step: index + 1,
        id: n.id,
        skill: n.props.skillType,
        label: n.props.label,
        description: n.props.description,
        config: n.props.config || {},
        inputs: n.props.inputs || [],
        outputs: n.props.outputs || [],
      })),
      connections: connections.map((c: any) => {
        const fromNode = nodes.find((n: any) => n.id === c.props.fromNodeId)
        const toNode = nodes.find((n: any) => n.id === c.props.toNodeId)
        const fromStep = nodes.indexOf(fromNode) + 1
        const toStep = nodes.indexOf(toNode) + 1
        return {
          from: c.props.fromNodeId,
          to: c.props.toNodeId,
          fromStep,
          toStep,
          description: fromNode && toNode
            ? `Step ${fromStep} (${fromNode.props.label}) → Step ${toStep} (${toNode.props.label})`
            : '',
        }
      }),
      execution: {
        totalSteps: nodes.length,
        order: nodes.map((n: any, i: number) => ({
          step: i + 1,
          skill: n.props.skillType,
          label: n.props.label,
        })),
      },
    }

    setIsRunning(true)

    try {
      // Try to save to server
      const response = await fetch('/api/save-workflow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(workflow),
      })

      const result = await response.json()

      if (result.success) {
        // Also copy to clipboard
        navigator.clipboard.writeText(JSON.stringify(workflow, null, 2))

        // Update node statuses to show they're queued
        nodes.forEach((node: any, index: number) => {
          editor.updateShape({
            id: node.id,
            type: 'skill-node' as any,
            props: { ...node.props, status: index === 0 ? 'running' : 'idle' },
          })
        })

        alert(`Workflow saved with ${nodes.length} steps!\n\nFile: ${result.file}\n\nExecution order:\n${
          workflow.execution.order.map((s: any) => `${s.step}. ${s.label}`).join('\n')
        }\n\nSay "/workflow run" in Claude Code to execute.`)
      } else {
        throw new Error(result.error)
      }
    } catch (error) {
      console.error('Failed to save workflow:', error)
      // Fallback: copy to clipboard
      navigator.clipboard.writeText(JSON.stringify(workflow, null, 2))
      alert(`Workflow copied to clipboard! (${nodes.length} steps)\n\nExecution order:\n${
        workflow.execution.order.map((s: any) => `${s.step}. ${s.label}`).join('\n')
      }\n\nPaste in Claude Code or save manually.`)
    } finally {
      setIsRunning(false)
    }
  }

  const cancelConnection = () => {
    setConnectMode(false)
    setSourcePort(null)
  }

  // Preview workflow - highlight execution path
  const togglePreview = useCallback(() => {
    const shapes = editor.getCurrentPageShapes() as any[]
    const connections = shapes.filter((s: any) => s.type === 'connection')

    if (isPreviewing) {
      // Turn off preview - reset all highlights
      connections.forEach((conn: any) => {
        editor.updateShape({
          id: conn.id,
          type: 'connection' as any,
          props: { ...conn.props, isHighlighted: false, isActive: false },
        })
      })
      setIsPreviewing(false)
    } else {
      // Turn on preview - highlight all connections
      connections.forEach((conn: any) => {
        editor.updateShape({
          id: conn.id,
          type: 'connection' as any,
          props: { ...conn.props, isHighlighted: true },
        })
      })
      setIsPreviewing(true)
    }
  }, [editor, isPreviewing])

  // Simulate workflow execution step by step
  const simulateWorkflow = useCallback(async () => {
    if (isSimulating) return

    const workflowData = buildOrderedWorkflow()
    if (!workflowData || workflowData.nodes.length === 0) {
      alert('No workflow to simulate! Add nodes and connect them.')
      return
    }

    setIsSimulating(true)
    const { nodes, connections } = workflowData

    // Reset all states
    nodes.forEach((node: any) => {
      editor.updateShape({
        id: node.id,
        type: 'skill-node' as any,
        props: { ...node.props, status: 'idle' },
      })
    })
    connections.forEach((conn: any) => {
      editor.updateShape({
        id: conn.id,
        type: 'connection' as any,
        props: { ...conn.props, isHighlighted: false, isActive: false },
      })
    })

    // Simulate each step
    for (let i = 0; i < nodes.length; i++) {
      const node = nodes[i]

      // Mark current node as running
      editor.updateShape({
        id: node.id,
        type: 'skill-node' as any,
        props: { ...node.props, status: 'running' },
      })

      // Highlight incoming connection
      const incomingConn = connections.find((c: any) => c.props.toNodeId === node.id)
      if (incomingConn) {
        editor.updateShape({
          id: incomingConn.id,
          type: 'connection' as any,
          props: { ...incomingConn.props, isActive: true },
        })
      }

      // Wait for simulation delay
      await new Promise((resolve) => setTimeout(resolve, 1500))

      // Mark as completed
      editor.updateShape({
        id: node.id,
        type: 'skill-node' as any,
        props: { ...node.props, status: 'completed' },
      })

      // Deactivate connection
      if (incomingConn) {
        editor.updateShape({
          id: incomingConn.id,
          type: 'connection' as any,
          props: { ...incomingConn.props, isActive: false, isHighlighted: true },
        })
      }

      // Highlight outgoing connection
      const outgoingConns = connections.filter((c: any) => c.props.fromNodeId === node.id)
      outgoingConns.forEach((conn: any) => {
        editor.updateShape({
          id: conn.id,
          type: 'connection' as any,
          props: { ...conn.props, isHighlighted: true },
        })
      })
    }

    setIsSimulating(false)
    alert(`Simulation complete! ${nodes.length} steps executed.`)
  }, [editor, buildOrderedWorkflow, isSimulating])

  return (
    <>
      {/* Main Toolbar */}
      <div
        style={{
          position: 'absolute',
          top: '12px',
          left: '50%',
          transform: 'translateX(-50%)',
          display: 'flex',
          gap: '2px',
          background: '#1e1e2e',
          borderRadius: '10px',
          padding: '6px',
          boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
          pointerEvents: 'all',
          border: '1px solid #334155',
          zIndex: 100,
        }}
      >
        {skills.map((skill) => (
          <button
            key={skill.type}
            onClick={() => addSkillNode(skill)}
            title={`Add ${skill.label}`}
            style={{
              background: 'transparent',
              border: 'none',
              padding: '6px 10px',
              borderRadius: '6px',
              cursor: 'pointer',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: '2px',
              color: '#e2e8f0',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.background = '#334155')}
            onMouseLeave={(e) => (e.currentTarget.style.background = 'transparent')}
          >
            <span style={{ fontSize: '18px' }}>{skill.icon}</span>
            <span style={{ fontSize: '9px' }}>{skill.label}</span>
          </button>
        ))}

        <div style={{ width: '1px', background: '#334155', margin: '4px 6px' }} />

        {/* Preview Button */}
        <button
          onClick={togglePreview}
          title="Preview workflow path"
          style={{
            background: isPreviewing ? '#f59e0b' : 'transparent',
            border: 'none',
            padding: '6px 10px',
            borderRadius: '6px',
            cursor: 'pointer',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '2px',
            color: isPreviewing ? 'white' : '#e2e8f0',
          }}
          onMouseEnter={(e) => !isPreviewing && (e.currentTarget.style.background = '#334155')}
          onMouseLeave={(e) => !isPreviewing && (e.currentTarget.style.background = 'transparent')}
        >
          <span style={{ fontSize: '18px' }}>👁️</span>
          <span style={{ fontSize: '9px' }}>{isPreviewing ? 'Hide' : 'Preview'}</span>
        </button>

        {/* Simulate Button */}
        <button
          onClick={simulateWorkflow}
          disabled={isSimulating}
          title="Simulate workflow execution"
          style={{
            background: isSimulating ? '#8b5cf6' : 'transparent',
            border: 'none',
            padding: '6px 10px',
            borderRadius: '6px',
            cursor: isSimulating ? 'wait' : 'pointer',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '2px',
            color: isSimulating ? 'white' : '#e2e8f0',
          }}
          onMouseEnter={(e) => !isSimulating && (e.currentTarget.style.background = '#334155')}
          onMouseLeave={(e) => !isSimulating && (e.currentTarget.style.background = 'transparent')}
        >
          <span style={{ fontSize: '18px' }}>{isSimulating ? '⏳' : '🎬'}</span>
          <span style={{ fontSize: '9px' }}>{isSimulating ? 'Running...' : 'Simulate'}</span>
        </button>

        <div style={{ width: '1px', background: '#334155', margin: '4px 6px' }} />

        {/* Run Button */}
        <button
          onClick={exportWorkflow}
          disabled={isRunning || isSimulating}
          style={{
            background: isRunning ? '#6366f1' : '#10b981',
            border: 'none',
            padding: '6px 14px',
            borderRadius: '6px',
            cursor: isRunning ? 'wait' : 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            color: 'white',
            fontWeight: 600,
            fontSize: '12px',
            opacity: isRunning ? 0.8 : 1,
          }}
        >
          <span>{isRunning ? '⏳' : '▶'}</span>
          <span>{isRunning ? 'Saving...' : 'Run'}</span>
        </button>
      </div>

      {/* Connection Mode Indicator */}
      {connectMode && (
        <div
          style={{
            position: 'absolute',
            bottom: '20px',
            left: '50%',
            transform: 'translateX(-50%)',
            background: '#10b981',
            color: 'white',
            padding: '12px 24px',
            borderRadius: '8px',
            boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
            zIndex: 1000,
            pointerEvents: 'all',
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            fontSize: '14px',
          }}
        >
          <span>🔗</span>
          <span style={{ fontWeight: 500 }}>
            {sourcePort
              ? `From "${sourcePort.nodeLabel}" → Click INPUT (blue ◀) on target node`
              : 'Click OUTPUT (green ▶) on source node'}
          </span>
          <button
            onClick={cancelConnection}
            style={{
              background: 'rgba(255,255,255,0.2)',
              border: 'none',
              padding: '6px 12px',
              borderRadius: '4px',
              color: 'white',
              cursor: 'pointer',
              fontSize: '12px',
            }}
          >
            Cancel
          </button>
        </div>
      )}

      {/* Connection Instructions - shown when no connection is active */}
      {!connectMode && (
        <div
          style={{
            position: 'absolute',
            bottom: '20px',
            left: '20px',
            background: '#1e1e2e',
            color: '#94a3b8',
            padding: '8px 12px',
            borderRadius: '6px',
            boxShadow: '0 2px 10px rgba(0,0,0,0.3)',
            zIndex: 50,
            pointerEvents: 'none',
            fontSize: '11px',
            border: '1px solid #334155',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ color: '#10b981' }}>▶</span>
            <span>Click green output → then blue input</span>
            <span style={{ color: '#3b82f6' }}>◀</span>
          </div>
        </div>
      )}
    </>
  )
})
