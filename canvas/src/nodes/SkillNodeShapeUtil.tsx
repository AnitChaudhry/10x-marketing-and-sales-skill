import {
  BaseBoxShapeUtil,
  HTMLContainer,
  T,
} from 'tldraw'

// Skill types for 100X Outreach
export type SkillType =
  | 'discovery'
  | 'linkedin'
  | 'twitter'
  | 'instagram'
  | 'gmail'
  | 'workflow'
  | 'template'
  | 'audience'
  | 'campaign'

// Skill configurations with colors and icons
const skillConfig: Record<SkillType, { color: string; icon: string; defaultLabel: string }> = {
  discovery: { color: '#6366f1', icon: '🔍', defaultLabel: 'Discovery' },
  linkedin: { color: '#0077b5', icon: '💼', defaultLabel: 'LinkedIn' },
  twitter: { color: '#1da1f2', icon: '🐦', defaultLabel: 'Twitter' },
  instagram: { color: '#e4405f', icon: '📸', defaultLabel: 'Instagram' },
  gmail: { color: '#ea4335', icon: '📧', defaultLabel: 'Gmail' },
  workflow: { color: '#10b981', icon: '⚡', defaultLabel: 'Workflow' },
  template: { color: '#f59e0b', icon: '📝', defaultLabel: 'Template' },
  audience: { color: '#8b5cf6', icon: '👥', defaultLabel: 'Audience' },
  campaign: { color: '#ec4899', icon: '🚀', defaultLabel: 'Campaign' },
}

export class SkillNodeShapeUtil extends BaseBoxShapeUtil<any> {
  static override type = 'skill-node' as const

  static override props: any = {
    w: T.number,
    h: T.number,
    skillType: T.string,
    label: T.string,
    description: T.string,
    status: T.string,
    inputs: T.arrayOf(T.string),
    outputs: T.arrayOf(T.string),
    config: T.any,
  }

  getDefaultProps() {
    return {
      w: 200,
      h: 120,
      skillType: 'discovery',
      label: 'Discovery',
      description: 'Find people using Exa AI',
      status: 'idle',
      inputs: [],
      outputs: ['people'],
      config: {},
    }
  }

  component(shape: any) {
    const config = skillConfig[shape.props.skillType as SkillType] || skillConfig.discovery
    const statusColors: Record<string, string> = {
      idle: '#64748b',
      running: '#f59e0b',
      completed: '#10b981',
      error: '#ef4444',
    }
    const editor = this.editor
    const isSelected = editor.getSelectedShapeIds().includes(shape.id)
    const isRunning = shape.props.status === 'running'

    // Port click handler - dispatch custom event for connection creation
    const handlePortClick = (portType: 'input' | 'output', e: React.MouseEvent) => {
      e.stopPropagation()
      const event = new CustomEvent('port-click', {
        detail: { nodeId: shape.id, portType, nodeLabel: shape.props.label },
        bubbles: true,
      })
      window.dispatchEvent(event)
    }

    // Port drag handler - dispatch event for drag-to-connect
    const handlePortDragStart = (portType: 'input' | 'output', e: React.MouseEvent) => {
      e.stopPropagation()
      e.preventDefault()

      const event = new CustomEvent('port-drag-start', {
        detail: {
          nodeId: shape.id,
          portType,
          nodeLabel: shape.props.label,
          clientX: e.clientX,
          clientY: e.clientY,
        },
        bubbles: true,
      })
      window.dispatchEvent(event)
    }

    return (
      <HTMLContainer
        style={{
          width: shape.props.w,
          height: shape.props.h,
          pointerEvents: 'all',
          position: 'relative',
        }}
      >
        {/* Input Port - Left side */}
        <div
          onClick={(e) => handlePortClick('input', e)}
          onMouseDown={(e) => handlePortDragStart('input', e)}
          style={{
            position: 'absolute',
            left: '-14px',
            top: '50%',
            transform: 'translateY(-50%)',
            width: '28px',
            height: '28px',
            borderRadius: '50%',
            background: isSelected ? '#3b82f6' : '#1e293b',
            border: '3px solid #3b82f6',
            cursor: 'crosshair',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 10,
            transition: 'all 0.2s ease',
            boxShadow: '0 2px 8px rgba(59, 130, 246, 0.5)',
          }}
          title="Input - Drag here to connect"
          onMouseEnter={(e) => {
            e.currentTarget.style.transform = 'translateY(-50%) scale(1.3)'
            e.currentTarget.style.background = '#3b82f6'
            e.currentTarget.style.boxShadow = '0 0 20px rgba(59, 130, 246, 0.8)'
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.transform = 'translateY(-50%) scale(1)'
            e.currentTarget.style.background = isSelected ? '#3b82f6' : '#1e293b'
            e.currentTarget.style.boxShadow = '0 2px 8px rgba(59, 130, 246, 0.5)'
          }}
        >
          <span style={{ color: 'white', fontSize: '14px', fontWeight: 'bold' }}>◀</span>
        </div>

        {/* Output Port - Right side */}
        <div
          onClick={(e) => handlePortClick('output', e)}
          onMouseDown={(e) => handlePortDragStart('output', e)}
          style={{
            position: 'absolute',
            right: '-14px',
            top: '50%',
            transform: 'translateY(-50%)',
            width: '28px',
            height: '28px',
            borderRadius: '50%',
            background: isSelected ? '#10b981' : '#1e293b',
            border: '3px solid #10b981',
            cursor: 'crosshair',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 10,
            transition: 'all 0.2s ease',
            boxShadow: '0 2px 8px rgba(16, 185, 129, 0.5)',
          }}
          title="Output - Drag from here to connect"
          onMouseEnter={(e) => {
            e.currentTarget.style.transform = 'translateY(-50%) scale(1.3)'
            e.currentTarget.style.background = '#10b981'
            e.currentTarget.style.boxShadow = '0 0 20px rgba(16, 185, 129, 0.8)'
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.transform = 'translateY(-50%) scale(1)'
            e.currentTarget.style.background = isSelected ? '#10b981' : '#1e293b'
            e.currentTarget.style.boxShadow = '0 2px 8px rgba(16, 185, 129, 0.5)'
          }}
        >
          <span style={{ color: 'white', fontSize: '14px', fontWeight: 'bold' }}>▶</span>
        </div>

        {/* Main Node Card */}
        <div
          style={{
            width: '100%',
            height: '100%',
            background: '#1e1e2e',
            borderRadius: '12px',
            border: `2px solid ${isSelected ? '#818cf8' : config.color}`,
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            boxShadow: isSelected
              ? `0 0 0 2px ${config.color}40, 0 4px 20px rgba(0,0,0,0.4)`
              : '0 4px 12px rgba(0,0,0,0.3)',
            animation: isRunning ? 'pulse 1.5s ease-in-out infinite' : 'none',
          }}
        >
          {/* Header */}
          <div
            style={{
              background: config.color,
              padding: '8px 12px',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              position: 'relative',
              overflow: 'hidden',
            }}
          >
            {/* Running animation overlay */}
            {isRunning && (
              <div
                style={{
                  position: 'absolute',
                  top: 0,
                  left: 0,
                  right: 0,
                  bottom: 0,
                  background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent)',
                  animation: 'shimmer 1.5s ease-in-out infinite',
                }}
              />
            )}
            <span style={{ fontSize: '18px', position: 'relative', zIndex: 1 }}>{config.icon}</span>
            <span style={{ color: 'white', fontWeight: 600, fontSize: '14px', flex: 1, position: 'relative', zIndex: 1 }}>
              {shape.props.label}
            </span>
            <div
              style={{
                width: '12px',
                height: '12px',
                borderRadius: '50%',
                background: statusColors[shape.props.status] || statusColors.idle,
                boxShadow: isRunning
                  ? '0 0 12px #f59e0b, 0 0 24px #f59e0b'
                  : shape.props.status === 'completed'
                    ? '0 0 8px #10b981'
                    : 'none',
                animation: isRunning ? 'blink 0.8s ease-in-out infinite' : 'none',
                position: 'relative',
                zIndex: 1,
              }}
            />
          </div>

          {/* Body */}
          <div style={{ padding: '10px 12px', flex: 1 }}>
            <p style={{ color: '#94a3b8', fontSize: '12px', margin: 0 }}>
              {shape.props.description}
            </p>
          </div>

          {/* Port Labels */}
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              padding: '6px 12px',
              borderTop: '1px solid #334155',
              background: '#0f172a',
            }}
          >
            {/* Input labels */}
            <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
              <span style={{ color: '#3b82f6', fontSize: '10px' }}>IN:</span>
              {(shape.props.inputs || []).length > 0 ? (
                (shape.props.inputs || []).map((input: string, i: number) => (
                  <span
                    key={i}
                    style={{
                      background: '#3b82f620',
                      color: '#60a5fa',
                      fontSize: '9px',
                      padding: '2px 5px',
                      borderRadius: '3px',
                    }}
                  >
                    {input}
                  </span>
                ))
              ) : (
                <span style={{ color: '#475569', fontSize: '9px' }}>start</span>
              )}
            </div>
            {/* Output labels */}
            <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
              <span style={{ color: '#10b981', fontSize: '10px' }}>OUT:</span>
              {(shape.props.outputs || []).map((output: string, i: number) => (
                <span
                  key={i}
                  style={{
                    background: '#10b98120',
                    color: '#34d399',
                    fontSize: '9px',
                    padding: '2px 5px',
                    borderRadius: '3px',
                  }}
                >
                  {output}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* CSS Animations */}
        <style>{`
          @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.85; }
          }
          @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
          }
          @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
          }
        `}</style>
      </HTMLContainer>
    )
  }

  indicator(shape: any) {
    return (
      <rect
        width={shape.props.w}
        height={shape.props.h}
        rx={12}
        ry={12}
      />
    )
  }
}

// Export shape type for reference
export type SkillNodeShape = any
