import { useEditor, track, TLShapeId, createShapeId } from 'tldraw'
import { useEffect, useState, useCallback } from 'react'

interface DragState {
  sourceNodeId: TLShapeId
  sourceLabel: string
  startPoint: { x: number; y: number }
  currentPoint: { x: number; y: number }
}

// Component that handles drag-to-connect functionality
export const ConnectionDragger = track(function ConnectionDragger() {
  const editor = useEditor()
  const [dragState, setDragState] = useState<DragState | null>(null)
  const [hoveredInputNode, setHoveredInputNode] = useState<{ id: TLShapeId; label: string } | null>(null)

  // Handle drag start from output port
  useEffect(() => {
    const handleDragStart = (e: CustomEvent<{
      nodeId: TLShapeId
      nodeLabel: string
      portType: 'input' | 'output'
      clientX: number
      clientY: number
    }>) => {
      if (e.detail.portType !== 'output') return

      const shape = editor.getShape(e.detail.nodeId) as any
      if (!shape) return

      // Calculate the start point (right side of node)
      const startX = shape.x + (shape.props?.w || 200)
      const startY = shape.y + (shape.props?.h || 120) / 2

      setDragState({
        sourceNodeId: e.detail.nodeId,
        sourceLabel: e.detail.nodeLabel,
        startPoint: { x: startX, y: startY },
        currentPoint: editor.screenToPage({ x: e.detail.clientX, y: e.detail.clientY }),
      })
    }

    window.addEventListener('port-drag-start', handleDragStart as EventListener)
    return () => window.removeEventListener('port-drag-start', handleDragStart as EventListener)
  }, [editor])

  // Handle drag move
  useEffect(() => {
    if (!dragState) return

    const handleMouseMove = (e: MouseEvent) => {
      const pagePoint = editor.screenToPage({ x: e.clientX, y: e.clientY })
      setDragState(prev => prev ? { ...prev, currentPoint: pagePoint } : null)

      // Check if hovering over an input port
      const shapes = editor.getCurrentPageShapes() as any[]
      const skillNodes = shapes.filter(s => s.type === 'skill-node' && s.id !== dragState.sourceNodeId)

      let foundHover = false
      for (const node of skillNodes) {
        const inputX = node.x
        const inputY = node.y + (node.props?.h || 120) / 2
        const distance = Math.sqrt(
          Math.pow(pagePoint.x - inputX, 2) + Math.pow(pagePoint.y - inputY, 2)
        )

        if (distance < 30) {
          setHoveredInputNode({ id: node.id, label: node.props.label })
          foundHover = true
          break
        }
      }

      if (!foundHover) {
        setHoveredInputNode(null)
      }
    }

    const handleMouseUp = (e: MouseEvent) => {
      if (hoveredInputNode && dragState) {
        // Create connection
        createConnection(dragState.sourceNodeId, hoveredInputNode.id)
      }
      setDragState(null)
      setHoveredInputNode(null)
    }

    window.addEventListener('mousemove', handleMouseMove)
    window.addEventListener('mouseup', handleMouseUp)

    return () => {
      window.removeEventListener('mousemove', handleMouseMove)
      window.removeEventListener('mouseup', handleMouseUp)
    }
  }, [dragState, hoveredInputNode, editor])

  const createConnection = useCallback((fromId: TLShapeId, toId: TLShapeId) => {
    const fromShape = editor.getShape(fromId) as any
    const toShape = editor.getShape(toId) as any
    if (!fromShape || !toShape) return

    // Check if connection already exists
    const shapes = editor.getCurrentPageShapes() as any[]
    const existingConnection = shapes.find(
      s => s.type === 'connection' &&
        s.props.fromNodeId === fromId &&
        s.props.toNodeId === toId
    )
    if (existingConnection) {
      console.log('Connection already exists')
      return
    }

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

  if (!dragState) return null

  // Convert page coordinates to screen for SVG overlay
  const startScreen = editor.pageToScreen(dragState.startPoint)
  const endScreen = editor.pageToScreen(dragState.currentPoint)

  // Calculate bezier curve
  const dx = endScreen.x - startScreen.x
  const controlOffset = Math.min(Math.abs(dx) * 0.5, 100)

  const path = `M ${startScreen.x} ${startScreen.y}
                C ${startScreen.x + controlOffset} ${startScreen.y},
                  ${endScreen.x - controlOffset} ${endScreen.y},
                  ${endScreen.x} ${endScreen.y}`

  return (
    <>
      {/* SVG overlay for drag line */}
      <svg
        style={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100vw',
          height: '100vh',
          pointerEvents: 'none',
          zIndex: 9999,
        }}
      >
        {/* Glow effect */}
        <path
          d={path}
          stroke={hoveredInputNode ? '#10b981' : '#6366f1'}
          strokeWidth={8}
          fill="none"
          opacity={0.3}
        />
        {/* Main line */}
        <path
          d={path}
          stroke={hoveredInputNode ? '#10b981' : '#6366f1'}
          strokeWidth={3}
          fill="none"
          strokeDasharray="8 4"
          style={{
            animation: 'dash 0.5s linear infinite',
          }}
        />
        {/* End point indicator */}
        <circle
          cx={endScreen.x}
          cy={endScreen.y}
          r={hoveredInputNode ? 12 : 8}
          fill={hoveredInputNode ? '#10b981' : '#6366f1'}
          opacity={0.8}
        />
      </svg>

      {/* Connection status indicator */}
      <div
        style={{
          position: 'fixed',
          bottom: '80px',
          left: '50%',
          transform: 'translateX(-50%)',
          background: hoveredInputNode ? '#10b981' : '#6366f1',
          color: 'white',
          padding: '12px 24px',
          borderRadius: '8px',
          boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
          zIndex: 10000,
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          fontSize: '14px',
        }}
      >
        <span>🔗</span>
        <span style={{ fontWeight: 500 }}>
          {hoveredInputNode
            ? `Release to connect "${dragState.sourceLabel}" → "${hoveredInputNode.label}"`
            : `Dragging from "${dragState.sourceLabel}" - hover over an input port`}
        </span>
      </div>

      {/* CSS for animation */}
      <style>{`
        @keyframes dash {
          to { stroke-dashoffset: -12; }
        }
      `}</style>
    </>
  )
})
