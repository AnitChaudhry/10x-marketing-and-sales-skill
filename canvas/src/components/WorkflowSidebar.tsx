import { useEditor, useValue, createShapeId, TLShapeId } from 'tldraw'
import { useState, useCallback } from 'react'
import { DraggablePanel } from './DraggablePanel'

interface PresetNode {
  type: string
  label: string
  x: number
  y: number
}

interface PresetConnection {
  from: number
  to: number
}

const workflowPresets: Array<{
  name: string
  icon: string
  description: string
  nodes: PresetNode[]
  connections: PresetConnection[]
}> = [
  {
    name: 'B2B Outreach',
    icon: '💼',
    description: '14-day sequence',
    nodes: [
      { type: 'audience', label: 'Target Audience', x: 100, y: 150 },
      { type: 'discovery', label: 'Find Prospects', x: 350, y: 150 },
      { type: 'linkedin', label: 'LinkedIn Connect', x: 600, y: 150 },
      { type: 'gmail', label: 'Send Email', x: 850, y: 150 },
    ],
    connections: [{ from: 0, to: 1 }, { from: 1, to: 2 }, { from: 2, to: 3 }],
  },
  {
    name: 'Brand Partnership',
    icon: '🤝',
    description: '21-day outreach',
    nodes: [
      { type: 'audience', label: 'Brand List', x: 100, y: 175 },
      { type: 'instagram', label: 'Instagram', x: 350, y: 100 },
      { type: 'twitter', label: 'Twitter', x: 350, y: 250 },
      { type: 'gmail', label: 'Email', x: 600, y: 175 },
    ],
    connections: [{ from: 0, to: 1 }, { from: 0, to: 2 }, { from: 1, to: 3 }, { from: 2, to: 3 }],
  },
  {
    name: 'Influencer',
    icon: '⭐',
    description: 'Creator outreach',
    nodes: [
      { type: 'discovery', label: 'Find Creators', x: 100, y: 175 },
      { type: 'twitter', label: 'Engage', x: 350, y: 100 },
      { type: 'instagram', label: 'Follow', x: 350, y: 250 },
      { type: 'gmail', label: 'Pitch', x: 600, y: 175 },
    ],
    connections: [{ from: 0, to: 1 }, { from: 0, to: 2 }, { from: 1, to: 3 }, { from: 2, to: 3 }],
  },
  {
    name: 'Multi-Platform',
    icon: '🌐',
    description: '30-day adaptive',
    nodes: [
      { type: 'audience', label: 'Targets', x: 100, y: 200 },
      { type: 'linkedin', label: 'LinkedIn', x: 350, y: 75 },
      { type: 'twitter', label: 'Twitter', x: 350, y: 200 },
      { type: 'instagram', label: 'Instagram', x: 350, y: 325 },
      { type: 'campaign', label: 'Campaign', x: 600, y: 200 },
    ],
    connections: [{ from: 0, to: 1 }, { from: 0, to: 2 }, { from: 0, to: 3 }, { from: 1, to: 4 }, { from: 2, to: 4 }, { from: 3, to: 4 }],
  },
]

const nodeDescriptions: Record<string, string> = {
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

const nodeInputs: Record<string, string[]> = {
  discovery: ['query'], audience: [], linkedin: ['person'], twitter: ['person'],
  instagram: ['person'], gmail: ['person', 'template'], template: ['context'],
  workflow: ['trigger'], campaign: ['audience', 'message'],
}

const nodeOutputs: Record<string, string[]> = {
  discovery: ['people'], audience: ['filters'], linkedin: ['sent'], twitter: ['sent'],
  instagram: ['sent'], gmail: ['sent'], template: ['message'], workflow: ['complete'],
  campaign: ['results'],
}

export function WorkflowSidebar() {
  const editor = useEditor()
  const [isOpen, setIsOpen] = useState(true)

  const skillNodes = useValue('skill-nodes', () => {
    return (editor.getCurrentPageShapes() as any[]).filter((s) => s.type === 'skill-node')
  }, [editor])

  const connections = useValue('connections', () => {
    return (editor.getCurrentPageShapes() as any[]).filter((s) => s.type === 'connection')
  }, [editor])

  const createConnection = useCallback((fromId: TLShapeId, toId: TLShapeId) => {
    const fromShape = editor.getShape(fromId) as any
    const toShape = editor.getShape(toId) as any
    if (!fromShape || !toShape) return

    const fromX = fromShape.x + (fromShape.props?.w || 200)
    const fromY = fromShape.y + (fromShape.props?.h || 120) / 2
    const toX = toShape.x
    const toY = toShape.y + (toShape.props?.h || 120) / 2

    editor.createShape({
      id: createShapeId(),
      type: 'connection' as any,
      x: 0, y: 0,
      props: { start: { x: fromX, y: fromY }, end: { x: toX, y: toY }, fromNodeId: fromId, toNodeId: toId, label: '' },
    })
  }, [editor])

  const loadPreset = useCallback((preset: typeof workflowPresets[0]) => {
    const shapes = editor.getCurrentPageShapes()
    editor.deleteShapes(shapes.map((s) => s.id))

    const nodeIds: TLShapeId[] = []
    preset.nodes.forEach((node) => {
      const id = createShapeId()
      nodeIds.push(id)
      editor.createShape({
        id,
        type: 'skill-node' as any,
        x: node.x,
        y: node.y,
        props: {
          w: 200, h: 120,
          skillType: node.type,
          label: node.label,
          description: nodeDescriptions[node.type] || 'Custom node',
          status: 'idle',
          inputs: nodeInputs[node.type] || [],
          outputs: nodeOutputs[node.type] || [],
        },
      })
    })

    setTimeout(() => {
      preset.connections.forEach((conn) => {
        if (nodeIds[conn.from] && nodeIds[conn.to]) {
          createConnection(nodeIds[conn.from], nodeIds[conn.to])
        }
      })
      editor.zoomToFit({ animation: { duration: 300 } })
    }, 100)
  }, [editor, createConnection])

  const exportWorkflow = useCallback(() => {
    const shapes = editor.getCurrentPageShapes() as any[]
    const nodes = shapes.filter((s) => s.type === 'skill-node')
    const conns = shapes.filter((s) => s.type === 'connection')

    const workflow = {
      name: '10x-Team Workflow',
      version: '1.0',
      created: new Date().toISOString(),
      nodes: nodes.map((n) => ({
        id: n.id,
        type: n.props.skillType,
        label: n.props.label,
        config: n.props.config || {},
      })),
      connections: conns.map((c) => ({
        from: c.props.fromNodeId,
        to: c.props.toNodeId,
      })),
    }

    navigator.clipboard.writeText(JSON.stringify(workflow, null, 2))
    alert('Workflow copied! Paste in Claude Code.')
  }, [editor])

  const panelContent = (
    <>
      {/* Stats */}
      <div style={{ display: 'flex', gap: '4px', padding: '8px 12px', borderBottom: '1px solid #334155' }}>
        <div style={{ flex: 1, background: '#0f172a', padding: '6px', borderRadius: '6px', textAlign: 'center' }}>
          <div style={{ color: '#6366f1', fontSize: '16px', fontWeight: 700 }}>{skillNodes.length}</div>
          <div style={{ color: '#64748b', fontSize: '9px' }}>Nodes</div>
        </div>
        <div style={{ flex: 1, background: '#0f172a', padding: '6px', borderRadius: '6px', textAlign: 'center' }}>
          <div style={{ color: '#f59e0b', fontSize: '16px', fontWeight: 700 }}>{connections.length}</div>
          <div style={{ color: '#64748b', fontSize: '9px' }}>Links</div>
        </div>
      </div>

      {/* Templates */}
      <div style={{ padding: '8px' }}>
        <div style={{ color: '#64748b', fontSize: '10px', marginBottom: '6px', padding: '0 4px' }}>TEMPLATES</div>
        {workflowPresets.map((preset, i) => (
          <button
            key={i}
            onClick={() => loadPreset(preset)}
            style={{
              width: '100%',
              background: 'transparent',
              border: 'none',
              padding: '8px',
              borderRadius: '6px',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              textAlign: 'left',
              marginBottom: '2px',
            }}
            onMouseEnter={(e) => e.currentTarget.style.background = '#334155'}
            onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
          >
            <span style={{ fontSize: '16px' }}>{preset.icon}</span>
            <div style={{ flex: 1 }}>
              <div style={{ color: '#e2e8f0', fontSize: '12px', fontWeight: 500 }}>{preset.name}</div>
              <div style={{ color: '#64748b', fontSize: '10px' }}>{preset.description}</div>
            </div>
            <span style={{ color: '#64748b', fontSize: '10px' }}>{preset.nodes.length}</span>
          </button>
        ))}
      </div>

      {/* Nodes List */}
      {skillNodes.length > 0 && (
        <div style={{ padding: '8px' }}>
          <div style={{ color: '#64748b', fontSize: '10px', marginBottom: '6px', padding: '0 4px' }}>NODES</div>
          {skillNodes.slice(0, 6).map((node: any) => (
            <div
              key={node.id}
              onClick={() => {
                editor.select(node.id)
                editor.zoomToSelection({ animation: { duration: 200 } })
              }}
              style={{
                padding: '6px 8px',
                borderRadius: '4px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                marginBottom: '2px',
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = '#334155'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              <div style={{
                width: '6px', height: '6px', borderRadius: '50%',
                background: node.props.status === 'completed' ? '#10b981' : node.props.status === 'running' ? '#f59e0b' : '#64748b',
              }} />
              <span style={{ color: '#e2e8f0', fontSize: '11px', flex: 1 }}>{node.props.label}</span>
            </div>
          ))}
          {skillNodes.length > 6 && (
            <div style={{ color: '#64748b', fontSize: '10px', padding: '4px 8px' }}>
              +{skillNodes.length - 6} more
            </div>
          )}
        </div>
      )}

      {/* Actions */}
      <div style={{ padding: '8px', borderTop: '1px solid #334155' }}>
        <div style={{ display: 'flex', gap: '4px' }}>
          <button
            onClick={exportWorkflow}
            style={{
              flex: 1,
              background: '#6366f1',
              border: 'none',
              padding: '8px',
              borderRadius: '6px',
              color: 'white',
              cursor: 'pointer',
              fontSize: '10px',
              fontWeight: 500,
            }}
          >
            📋 Export
          </button>
          <button
            onClick={() => editor.zoomToFit({ animation: { duration: 300 } })}
            style={{
              background: '#334155',
              border: 'none',
              padding: '8px 12px',
              borderRadius: '6px',
              color: 'white',
              cursor: 'pointer',
              fontSize: '10px',
            }}
          >
            🔍
          </button>
          <button
            onClick={() => {
              const shapes = editor.getCurrentPageShapes()
              editor.deleteShapes(shapes.map((s) => s.id))
            }}
            style={{
              background: '#dc2626',
              border: 'none',
              padding: '8px 12px',
              borderRadius: '6px',
              color: 'white',
              cursor: 'pointer',
              fontSize: '10px',
            }}
          >
            🗑️
          </button>
        </div>
      </div>
    </>
  )

  return (
    <DraggablePanel
      title="10x-Team"
      icon="🚀"
      initialPosition={{ x: window.innerWidth - 260, y: 72 }}
      width={240}
      isOpen={isOpen}
      onToggle={() => setIsOpen(!isOpen)}
    >
      {panelContent}
    </DraggablePanel>
  )
}
