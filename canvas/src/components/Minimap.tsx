import { useEditor, useValue } from 'tldraw'

export function Minimap() {
  const editor = useEditor()

  const shapes = useValue('shapes', () => {
    return editor.getCurrentPageShapes() as any[]
  }, [editor])

  const skillNodes = shapes.filter(s => s.type === 'skill-node')
  const connections = shapes.filter(s => s.type === 'connection')

  // Calculate bounds
  const bounds = skillNodes.reduce(
    (acc, node) => ({
      minX: Math.min(acc.minX, node.x),
      minY: Math.min(acc.minY, node.y),
      maxX: Math.max(acc.maxX, node.x + (node.props?.w || 200)),
      maxY: Math.max(acc.maxY, node.y + (node.props?.h || 120)),
    }),
    { minX: Infinity, minY: Infinity, maxX: -Infinity, maxY: -Infinity }
  )

  // If no nodes, don't render
  if (skillNodes.length === 0) return null

  const padding = 20
  const width = 180
  const height = 120

  const contentWidth = bounds.maxX - bounds.minX + padding * 2
  const contentHeight = bounds.maxY - bounds.minY + padding * 2
  const scale = Math.min(width / contentWidth, height / contentHeight, 1)

  const nodeColors: Record<string, string> = {
    discovery: '#6366f1',
    linkedin: '#0077b5',
    twitter: '#1da1f2',
    instagram: '#e4405f',
    gmail: '#ea4335',
    workflow: '#10b981',
    template: '#f59e0b',
    audience: '#8b5cf6',
    campaign: '#ec4899',
  }

  return (
    <div
      style={{
        position: 'absolute',
        left: '12px',
        bottom: '12px',
        width: `${width}px`,
        height: `${height}px`,
        background: '#0f172a',
        borderRadius: '8px',
        border: '1px solid #334155',
        overflow: 'hidden',
        pointerEvents: 'all',
        zIndex: 50,
      }}
    >
      {/* Header */}
      <div
        style={{
          padding: '4px 8px',
          borderBottom: '1px solid #334155',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <span style={{ color: '#64748b', fontSize: '9px' }}>MINIMAP</span>
        <span style={{ color: '#64748b', fontSize: '9px' }}>{skillNodes.length} nodes</span>
      </div>

      {/* Canvas */}
      <svg
        width={width}
        height={height - 24}
        style={{ background: '#1e1e2e' }}
        onClick={(e) => {
          const rect = e.currentTarget.getBoundingClientRect()
          const x = (e.clientX - rect.left) / scale + bounds.minX - padding
          const y = (e.clientY - rect.top) / scale + bounds.minY - padding
          editor.centerOnPoint({ x, y }, { animation: { duration: 200 } })
        }}
      >
        {/* Grid pattern */}
        <defs>
          <pattern id="minimap-grid" width="10" height="10" patternUnits="userSpaceOnUse">
            <circle cx="5" cy="5" r="0.5" fill="#334155" />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#minimap-grid)" />

        {/* Connections */}
        {connections.map((conn: any) => {
          const start = conn.props?.start
          const end = conn.props?.end
          if (!start || !end) return null

          return (
            <line
              key={conn.id}
              x1={(start.x - bounds.minX + padding) * scale}
              y1={(start.y - bounds.minY + padding) * scale}
              x2={(end.x - bounds.minX + padding) * scale}
              y2={(end.y - bounds.minY + padding) * scale}
              stroke="#6366f1"
              strokeWidth={1}
              opacity={0.5}
            />
          )
        })}

        {/* Nodes */}
        {skillNodes.map((node: any) => {
          const x = (node.x - bounds.minX + padding) * scale
          const y = (node.y - bounds.minY + padding) * scale
          const w = (node.props?.w || 200) * scale
          const h = (node.props?.h || 120) * scale
          const color = nodeColors[node.props?.skillType] || '#64748b'

          return (
            <rect
              key={node.id}
              x={x}
              y={y}
              width={w}
              height={h}
              fill={color}
              rx={2}
              opacity={0.8}
              style={{ cursor: 'pointer' }}
              onClick={(e) => {
                e.stopPropagation()
                editor.select(node.id)
                editor.zoomToSelection({ animation: { duration: 200 } })
              }}
            />
          )
        })}
      </svg>
    </div>
  )
}
