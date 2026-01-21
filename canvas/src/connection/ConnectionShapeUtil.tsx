import {
  ShapeUtil,
  SVGContainer,
  T,
  Rectangle2d,
  HTMLContainer,
} from 'tldraw'

// Connection shape for linking skill nodes
export class ConnectionShapeUtil extends ShapeUtil<any> {
  static override type = 'connection' as const

  static override props = {
    start: T.object({
      x: T.number,
      y: T.number,
    }),
    end: T.object({
      x: T.number,
      y: T.number,
    }),
    fromNodeId: T.string.nullable(),
    toNodeId: T.string.nullable(),
    label: T.string,
    isHighlighted: T.boolean,
    isActive: T.boolean,
  }

  getDefaultProps() {
    return {
      start: { x: 0, y: 0 },
      end: { x: 100, y: 0 },
      fromNodeId: null,
      toNodeId: null,
      label: '',
      isHighlighted: false,
      isActive: false,
    }
  }

  // Create a proper bounding box for selection
  getGeometry(shape: any) {
    const { start, end } = shape.props
    const minX = Math.min(start.x, end.x)
    const minY = Math.min(start.y, end.y)
    const maxX = Math.max(start.x, end.x)
    const maxY = Math.max(start.y, end.y)

    return new Rectangle2d({
      width: Math.max(maxX - minX, 20),
      height: Math.max(maxY - minY, 20),
      isFilled: false,
    })
  }

  // Allow selection but not other interactions
  override canEdit = () => false
  override canResize = () => false
  override canBind = () => false

  component(shape: any) {
    const { start, end, isHighlighted, isActive } = shape.props
    const editor = this.editor
    const isSelected = editor.getSelectedShapeIds().includes(shape.id)

    // Determine colors based on state
    const baseColor = isActive ? '#10b981' : isHighlighted ? '#f59e0b' : '#6366f1'
    const glowColor = isActive ? '#10b981' : isHighlighted ? '#f59e0b' : '#818cf8'

    // Calculate the path
    const dx = end.x - start.x

    // Bezier curve control points
    const controlOffset = Math.min(Math.abs(dx) * 0.5, 80)

    const path = `M ${start.x} ${start.y}
                  C ${start.x + controlOffset} ${start.y},
                    ${end.x - controlOffset} ${end.y},
                    ${end.x} ${end.y}`

    // Calculate midpoint for delete button
    const midX = (start.x + end.x) / 2
    const midY = (start.y + end.y) / 2

    const markerId = `arrowhead-${shape.id}`

    return (
      <>
        <SVGContainer
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            overflow: 'visible',
            pointerEvents: 'none',
          }}
        >
          <defs>
            <marker
              id={markerId}
              markerWidth="12"
              markerHeight="8"
              refX="10"
              refY="4"
              orient="auto"
              markerUnits="strokeWidth"
            >
              <path
                d="M 0 0 L 12 4 L 0 8 Z"
                fill={isSelected ? glowColor : baseColor}
              />
            </marker>

            {/* Gradient for active connections */}
            {isActive && (
              <linearGradient id={`gradient-${shape.id}`} x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="#10b981" />
                <stop offset="50%" stopColor="#34d399" />
                <stop offset="100%" stopColor="#10b981" />
              </linearGradient>
            )}
          </defs>

          {/* Glow effect - stronger when selected or highlighted */}
          <path
            d={path}
            stroke={isActive ? '#10b981' : isHighlighted ? '#f59e0b' : isSelected ? '#818cf8' : '#6366f1'}
            strokeWidth={isActive ? 16 : isHighlighted ? 12 : isSelected ? 10 : 6}
            fill="none"
            opacity={isActive ? 0.4 : isHighlighted ? 0.35 : isSelected ? 0.3 : 0.2}
          />

          {/* Clickable area - wider for easier selection */}
          <path
            d={path}
            stroke="transparent"
            strokeWidth={24}
            fill="none"
            style={{ pointerEvents: 'stroke', cursor: 'pointer' }}
            onClick={(e) => {
              e.stopPropagation()
              editor.select(shape.id)
            }}
          />

          {/* Main connection line */}
          <path
            d={path}
            stroke={isActive ? `url(#gradient-${shape.id})` : isSelected ? glowColor : baseColor}
            strokeWidth={isActive ? 4 : isHighlighted ? 3 : isSelected ? 3 : 2}
            fill="none"
            markerEnd={`url(#${markerId})`}
          />

          {/* Animated flow indicator */}
          <path
            d={path}
            stroke={isActive ? '#a7f3d0' : isHighlighted ? '#fcd34d' : isSelected ? '#a5b4fc' : '#818cf8'}
            strokeWidth={isActive ? 3 : 2}
            fill="none"
            strokeDasharray={isActive ? '12 8' : '8 12'}
            style={{
              animation: `flow ${isActive ? '0.5s' : '1s'} linear infinite`,
            }}
          />

          {/* Active pulse effect */}
          {isActive && (
            <path
              d={path}
              stroke="#10b981"
              strokeWidth={8}
              fill="none"
              opacity={0.3}
              style={{
                animation: 'pulse-line 1s ease-in-out infinite',
              }}
            />
          )}

          {/* Label */}
          {shape.props.label && (
            <>
              <rect
                x={midX - 30}
                y={midY - 12}
                width={60}
                height={20}
                rx={4}
                fill="#1e1e2e"
                stroke={baseColor}
                strokeWidth={1}
              />
              <text
                x={midX}
                y={midY + 3}
                textAnchor="middle"
                fill={isActive ? '#10b981' : isHighlighted ? '#f59e0b' : '#94a3b8'}
                fontSize={11}
                fontFamily="Inter, sans-serif"
                fontWeight={isActive ? 600 : 400}
              >
                {shape.props.label}
              </text>
            </>
          )}
        </SVGContainer>

        {/* Delete button - shown when selected */}
        {isSelected && (
          <HTMLContainer
            style={{
              position: 'absolute',
              left: midX - 16,
              top: midY - 16,
              width: 32,
              height: 32,
              pointerEvents: 'all',
            }}
          >
            <button
              onClick={(e) => {
                e.stopPropagation()
                editor.deleteShape(shape.id)
              }}
              style={{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: '#dc2626',
                border: '2px solid #1e1e2e',
                color: 'white',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '14px',
                boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
              }}
              title="Delete connection"
            >
              ✕
            </button>
          </HTMLContainer>
        )}
      </>
    )
  }

  indicator(shape: any) {
    const { start, end } = shape.props
    const dx = end.x - start.x
    const controlOffset = Math.min(Math.abs(dx) * 0.5, 80)

    const path = `M ${start.x} ${start.y}
                  C ${start.x + controlOffset} ${start.y},
                    ${end.x - controlOffset} ${end.y},
                    ${end.x} ${end.y}`

    return (
      <path
        d={path}
        strokeWidth={3}
        fill="none"
      />
    )
  }
}

// CSS for animation
if (typeof document !== 'undefined') {
  const style = document.createElement('style')
  style.textContent = `
    @keyframes flow {
      from { stroke-dashoffset: 20; }
      to { stroke-dashoffset: 0; }
    }
    @keyframes pulse-line {
      0%, 100% { opacity: 0.3; stroke-width: 8; }
      50% { opacity: 0.6; stroke-width: 12; }
    }
  `
  if (!document.querySelector('#connection-animation-style')) {
    style.id = 'connection-animation-style'
    document.head.appendChild(style)
  }
}
