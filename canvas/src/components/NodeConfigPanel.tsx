import { useState, useEffect } from 'react'
import { useEditor, useValue } from 'tldraw'
import { getTemplatesByPlatform, Template } from '../data/templates'

const nodeConfigs: Record<string, {
  fields: Array<{
    key: string
    label: string
    type: 'text' | 'textarea' | 'select' | 'number' | 'template'
    placeholder?: string
    options?: Array<{ value: string; label: string }>
    platform?: Template['platform']
  }>
}> = {
  discovery: {
    fields: [
      { key: 'query', label: 'Search Query', type: 'text', placeholder: 'AI startup founders...' },
      { key: 'maxResults', label: 'Max Results', type: 'number', placeholder: '10' },
    ],
  },
  audience: {
    fields: [
      { key: 'name', label: 'Audience Name', type: 'text', placeholder: 'Tech Founders' },
      { key: 'size', label: 'Target Size', type: 'number', placeholder: '100' },
    ],
  },
  linkedin: {
    fields: [
      { key: 'action', label: 'Action', type: 'select', options: [
        { value: 'connect', label: 'Connect' },
        { value: 'message', label: 'Message' },
        { value: 'view', label: 'View Profile' },
      ]},
      { key: 'template', label: 'Template', type: 'template', platform: 'linkedin' },
    ],
  },
  twitter: {
    fields: [
      { key: 'action', label: 'Action', type: 'select', options: [
        { value: 'follow', label: 'Follow' },
        { value: 'dm', label: 'DM' },
        { value: 'like', label: 'Like' },
      ]},
      { key: 'template', label: 'Template', type: 'template', platform: 'twitter' },
    ],
  },
  instagram: {
    fields: [
      { key: 'action', label: 'Action', type: 'select', options: [
        { value: 'follow', label: 'Follow' },
        { value: 'dm', label: 'DM' },
        { value: 'like', label: 'Like' },
      ]},
      { key: 'template', label: 'Template', type: 'template', platform: 'instagram' },
    ],
  },
  gmail: {
    fields: [
      { key: 'subject', label: 'Subject', type: 'text', placeholder: 'Quick question...' },
      { key: 'template', label: 'Template', type: 'template', platform: 'email' },
    ],
  },
  template: {
    fields: [
      { key: 'name', label: 'Template Name', type: 'text', placeholder: 'My Template' },
      { key: 'content', label: 'Content', type: 'textarea', placeholder: 'Hi {name}...' },
    ],
  },
  workflow: {
    fields: [
      { key: 'name', label: 'Workflow Name', type: 'text', placeholder: 'My Workflow' },
    ],
  },
  campaign: {
    fields: [
      { key: 'name', label: 'Campaign Name', type: 'text', placeholder: 'Q1 Outreach' },
      { key: 'budget', label: 'Daily Limit', type: 'number', placeholder: '50' },
    ],
  },
}

const skillColors: Record<string, string> = {
  discovery: '#6366f1', linkedin: '#0077b5', twitter: '#1da1f2',
  instagram: '#e4405f', gmail: '#ea4335', workflow: '#10b981',
  template: '#f59e0b', audience: '#8b5cf6', campaign: '#ec4899',
}

const skillIcons: Record<string, string> = {
  discovery: '🔍', linkedin: '💼', twitter: '🐦',
  instagram: '📸', gmail: '📧', workflow: '⚡',
  template: '📝', audience: '👥', campaign: '🚀',
}

export function NodeConfigPanel() {
  const editor = useEditor()
  const [config, setConfig] = useState<Record<string, any>>({})

  const selectedNode = useValue('selected-skill-node', () => {
    const selected = editor.getSelectedShapes()
    return selected.find((s: any) => s.type === 'skill-node') as any
  }, [editor])

  useEffect(() => {
    if (selectedNode) {
      setConfig(selectedNode.props.config || {})
    }
  }, [selectedNode?.id])

  const saveConfig = () => {
    if (!selectedNode) return
    editor.updateShape({
      id: selectedNode.id,
      type: 'skill-node' as any,
      props: { ...selectedNode.props, config },
    })
  }

  if (!selectedNode) return null

  const nodeConfig = nodeConfigs[selectedNode.props.skillType]
  if (!nodeConfig) return null

  const color = skillColors[selectedNode.props.skillType] || '#6366f1'
  const icon = skillIcons[selectedNode.props.skillType] || '⚙️'

  return (
    <div
      style={{
        position: 'absolute',
        left: '50%',
        bottom: '80px',
        transform: 'translateX(-50%)',
        width: '400px',
        background: '#1e1e2e',
        borderRadius: '10px',
        boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
        border: `1px solid ${color}`,
        pointerEvents: 'all',
        zIndex: 100,
      }}
    >
      {/* Header */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          padding: '10px 12px',
          borderBottom: `1px solid ${color}40`,
          background: `${color}20`,
          borderRadius: '10px 10px 0 0',
        }}
      >
        <span style={{ fontSize: '16px' }}>{icon}</span>
        <span style={{ color: '#e2e8f0', fontSize: '13px', fontWeight: 600, flex: 1 }}>
          {selectedNode.props.label}
        </span>
        <button
          onClick={() => editor.deselect(selectedNode.id)}
          style={{
            background: 'transparent',
            border: 'none',
            color: '#64748b',
            cursor: 'pointer',
            fontSize: '14px',
          }}
        >
          ✕
        </button>
      </div>

      {/* Fields */}
      <div style={{ padding: '12px', display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
        {nodeConfig.fields.map((field) => (
          <div key={field.key} style={{ flex: field.type === 'textarea' ? '1 1 100%' : '1 1 calc(50% - 4px)', minWidth: '140px' }}>
            <label style={{ display: 'block', color: '#64748b', fontSize: '10px', marginBottom: '4px' }}>
              {field.label}
            </label>

            {field.type === 'text' && (
              <input
                type="text"
                value={config[field.key] || ''}
                placeholder={field.placeholder}
                onChange={(e) => setConfig({ ...config, [field.key]: e.target.value })}
                style={{
                  width: '100%',
                  background: '#0f172a',
                  border: '1px solid #334155',
                  borderRadius: '4px',
                  padding: '6px 8px',
                  color: '#e2e8f0',
                  fontSize: '11px',
                }}
              />
            )}

            {field.type === 'textarea' && (
              <textarea
                value={config[field.key] || ''}
                placeholder={field.placeholder}
                onChange={(e) => setConfig({ ...config, [field.key]: e.target.value })}
                rows={2}
                style={{
                  width: '100%',
                  background: '#0f172a',
                  border: '1px solid #334155',
                  borderRadius: '4px',
                  padding: '6px 8px',
                  color: '#e2e8f0',
                  fontSize: '11px',
                  resize: 'none',
                }}
              />
            )}

            {field.type === 'number' && (
              <input
                type="number"
                value={config[field.key] || ''}
                placeholder={field.placeholder}
                onChange={(e) => setConfig({ ...config, [field.key]: parseInt(e.target.value) || 0 })}
                style={{
                  width: '100%',
                  background: '#0f172a',
                  border: '1px solid #334155',
                  borderRadius: '4px',
                  padding: '6px 8px',
                  color: '#e2e8f0',
                  fontSize: '11px',
                }}
              />
            )}

            {field.type === 'select' && (
              <select
                value={config[field.key] || ''}
                onChange={(e) => setConfig({ ...config, [field.key]: e.target.value })}
                style={{
                  width: '100%',
                  background: '#0f172a',
                  border: '1px solid #334155',
                  borderRadius: '4px',
                  padding: '6px 8px',
                  color: '#e2e8f0',
                  fontSize: '11px',
                }}
              >
                <option value="">Select...</option>
                {field.options?.map((opt) => (
                  <option key={opt.value} value={opt.value}>{opt.label}</option>
                ))}
              </select>
            )}

            {field.type === 'template' && field.platform && (
              <select
                value={config[field.key] || ''}
                onChange={(e) => setConfig({ ...config, [field.key]: e.target.value })}
                style={{
                  width: '100%',
                  background: '#0f172a',
                  border: '1px solid #334155',
                  borderRadius: '4px',
                  padding: '6px 8px',
                  color: '#e2e8f0',
                  fontSize: '11px',
                }}
              >
                <option value="">Select template...</option>
                {getTemplatesByPlatform(field.platform).map((t) => (
                  <option key={t.id} value={t.path}>{t.name}</option>
                ))}
              </select>
            )}
          </div>
        ))}
      </div>

      {/* Actions */}
      <div style={{ display: 'flex', gap: '6px', padding: '8px 12px', borderTop: '1px solid #334155' }}>
        <button
          onClick={saveConfig}
          style={{
            flex: 1,
            background: color,
            border: 'none',
            padding: '8px',
            borderRadius: '4px',
            color: 'white',
            cursor: 'pointer',
            fontSize: '11px',
            fontWeight: 500,
          }}
        >
          Save
        </button>
        <button
          onClick={() => {
            editor.updateShape({
              id: selectedNode.id,
              type: 'skill-node' as any,
              props: { ...selectedNode.props, status: 'completed' },
            })
          }}
          style={{
            background: '#10b981',
            border: 'none',
            padding: '8px 12px',
            borderRadius: '4px',
            color: 'white',
            cursor: 'pointer',
            fontSize: '11px',
          }}
        >
          ✓ Done
        </button>
        <button
          onClick={() => editor.deleteShape(selectedNode.id)}
          style={{
            background: '#dc2626',
            border: 'none',
            padding: '8px 12px',
            borderRadius: '4px',
            color: 'white',
            cursor: 'pointer',
            fontSize: '11px',
          }}
        >
          🗑️
        </button>
      </div>
    </div>
  )
}
