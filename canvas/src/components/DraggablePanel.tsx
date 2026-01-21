import { useState, useRef, useCallback, ReactNode } from 'react'

interface DraggablePanelProps {
  children: ReactNode
  initialPosition: { x: number; y: number }
  title: string
  icon: string
  width?: number
  onClose?: () => void
  isOpen: boolean
  onToggle: () => void
}

export function DraggablePanel({
  children,
  initialPosition,
  title,
  icon,
  width = 240,
  onClose,
  isOpen,
  onToggle,
}: DraggablePanelProps) {
  const [position, setPosition] = useState(initialPosition)
  const [isDragging, setIsDragging] = useState(false)
  const dragOffset = useRef({ x: 0, y: 0 })
  const panelRef = useRef<HTMLDivElement>(null)

  const handleMouseDown = useCallback((e: React.MouseEvent) => {
    if ((e.target as HTMLElement).closest('button, input, select, textarea')) return

    setIsDragging(true)
    dragOffset.current = {
      x: e.clientX - position.x,
      y: e.clientY - position.y,
    }

    const handleMouseMove = (e: MouseEvent) => {
      setPosition({
        x: e.clientX - dragOffset.current.x,
        y: e.clientY - dragOffset.current.y,
      })
    }

    const handleMouseUp = () => {
      setIsDragging(false)
      document.removeEventListener('mousemove', handleMouseMove)
      document.removeEventListener('mouseup', handleMouseUp)
    }

    document.addEventListener('mousemove', handleMouseMove)
    document.addEventListener('mouseup', handleMouseUp)
  }, [position])

  // Collapsed state - just a button
  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        style={{
          position: 'absolute',
          left: position.x,
          top: position.y,
          background: '#1e1e2e',
          border: '1px solid #334155',
          borderRadius: '8px',
          padding: '8px 12px',
          cursor: 'pointer',
          pointerEvents: 'all',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          color: '#e2e8f0',
          fontSize: '12px',
          zIndex: 50,
        }}
      >
        <span>{icon}</span>
        <span>{title}</span>
      </button>
    )
  }

  return (
    <div
      ref={panelRef}
      style={{
        position: 'absolute',
        left: position.x,
        top: position.y,
        width: `${width}px`,
        background: '#1e1e2e',
        borderRadius: '10px',
        boxShadow: isDragging
          ? '0 8px 32px rgba(99, 102, 241, 0.3)'
          : '0 4px 20px rgba(0,0,0,0.4)',
        border: isDragging ? '1px solid #6366f1' : '1px solid #334155',
        pointerEvents: 'all',
        zIndex: isDragging ? 1000 : 50,
        display: 'flex',
        flexDirection: 'column',
        maxHeight: 'calc(100vh - 100px)',
        transition: isDragging ? 'none' : 'box-shadow 0.2s, border 0.2s',
      }}
    >
      {/* Draggable Header */}
      <div
        onMouseDown={handleMouseDown}
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '10px 12px',
          borderBottom: '1px solid #334155',
          cursor: isDragging ? 'grabbing' : 'grab',
          userSelect: 'none',
          flexShrink: 0,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <span style={{ fontSize: '16px' }}>{icon}</span>
          <span style={{ color: '#e2e8f0', fontSize: '13px', fontWeight: 600 }}>
            {title}
          </span>
        </div>
        <div style={{ display: 'flex', gap: '4px' }}>
          <button
            onClick={onToggle}
            style={{
              background: 'transparent',
              border: 'none',
              color: '#64748b',
              cursor: 'pointer',
              fontSize: '12px',
              padding: '2px 6px',
            }}
            title="Minimize"
          >
            −
          </button>
          {onClose && (
            <button
              onClick={onClose}
              style={{
                background: 'transparent',
                border: 'none',
                color: '#64748b',
                cursor: 'pointer',
                fontSize: '14px',
                padding: '2px 6px',
              }}
              title="Close"
            >
              ✕
            </button>
          )}
        </div>
      </div>

      {/* Panel Content */}
      <div style={{ flex: 1, overflow: 'auto' }}>
        {children}
      </div>
    </div>
  )
}
