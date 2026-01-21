import { useState } from 'react'
import { useEditor, createShapeId } from 'tldraw'
import { getTemplatesGroupedByCategory, templateStats, Template } from '../data/templates'
import { DraggablePanel } from './DraggablePanel'

const platformConfig = {
  linkedin: { color: '#0077b5', icon: '💼', name: 'LinkedIn', nodeType: 'linkedin' },
  twitter: { color: '#1da1f2', icon: '🐦', name: 'Twitter', nodeType: 'twitter' },
  instagram: { color: '#e4405f', icon: '📸', name: 'Instagram', nodeType: 'instagram' },
  email: { color: '#ea4335', icon: '📧', name: 'Email', nodeType: 'gmail' },
}

export function TemplatesPanel() {
  const editor = useEditor()
  const [selectedPlatform, setSelectedPlatform] = useState<Template['platform']>('linkedin')
  const [expandedCategory, setExpandedCategory] = useState<string | null>(null)
  const [selectedTemplate, setSelectedTemplate] = useState<Template | null>(null)
  const [isOpen, setIsOpen] = useState(false)  // Start collapsed

  const groupedTemplates = getTemplatesGroupedByCategory(selectedPlatform)
  const config = platformConfig[selectedPlatform]

  // Add platform node with template pre-configured
  const addPlatformNodeWithTemplate = (template: Template) => {
    const viewportCenter = editor.getViewportScreenCenter()
    const pagePoint = editor.screenToPage(viewportCenter)
    const nodeType = platformConfig[template.platform].nodeType

    const getAction = (category: string, platform: string): string => {
      if (category.toLowerCase().includes('dm') || category.toLowerCase().includes('message')) {
        return platform === 'linkedin' ? 'message' : 'dm'
      }
      if (category.toLowerCase().includes('connect')) return 'connect'
      if (category.toLowerCase().includes('follow')) return 'follow'
      if (category.toLowerCase().includes('comment')) return 'comment'
      if (category.toLowerCase().includes('inmail')) return 'message'
      return 'message'
    }

    ;(editor as any).createShape({
      id: createShapeId(),
      type: 'skill-node',
      x: pagePoint.x - 100,
      y: pagePoint.y - 60,
      props: {
        w: 200, h: 120,
        skillType: nodeType,
        label: `${platformConfig[template.platform].name}: ${template.name}`,
        description: template.description,
        status: 'idle',
        inputs: ['person'],
        outputs: ['sent'],
        config: {
          action: getAction(template.category, template.platform),
          template: template.path,
          templateId: template.id,
          delay: template.platform === 'instagram' ? 48 : 24,
        },
      },
    })
  }

  const panelContent = (
    <>
      {/* Platform Tabs - Fixed */}
      <div
        style={{
          display: 'flex',
          gap: '4px',
          padding: '8px 12px',
          borderBottom: '1px solid #334155',
          flexShrink: 0,
        }}
      >
        {(Object.keys(platformConfig) as Template['platform'][]).map((platform) => {
          const p = platformConfig[platform]
          const isSelected = selectedPlatform === platform
          return (
            <button
              key={platform}
              onClick={() => {
                setSelectedPlatform(platform)
                setExpandedCategory(null)
                setSelectedTemplate(null)
              }}
              style={{
                flex: 1,
                background: isSelected ? p.color : 'transparent',
                border: 'none',
                padding: '6px',
                borderRadius: '6px',
                cursor: 'pointer',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '2px',
              }}
            >
              <span style={{ fontSize: '14px' }}>{p.icon}</span>
              <span style={{ color: isSelected ? 'white' : '#64748b', fontSize: '9px' }}>
                {templateStats[platform]}
              </span>
            </button>
          )
        })}
      </div>

      {/* Scrollable Content */}
      <div
        style={{
          flex: 1,
          overflow: 'auto',
          padding: '8px',
        }}
      >
        {Object.entries(groupedTemplates).map(([category, categoryTemplates]) => (
          <div key={category} style={{ marginBottom: '4px' }}>
            <button
              onClick={() => setExpandedCategory(expandedCategory === category ? null : category)}
              style={{
                width: '100%',
                background: expandedCategory === category ? '#334155' : 'transparent',
                border: 'none',
                padding: '8px 10px',
                borderRadius: '6px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ color: '#e2e8f0', fontSize: '12px' }}>{category}</span>
                <span style={{
                  background: config.color,
                  color: 'white',
                  fontSize: '9px',
                  padding: '1px 5px',
                  borderRadius: '8px',
                }}>
                  {categoryTemplates.length}
                </span>
              </div>
              <span style={{ color: '#64748b', fontSize: '10px' }}>
                {expandedCategory === category ? '▼' : '▶'}
              </span>
            </button>

            {expandedCategory === category && (
              <div style={{ padding: '4px 0 4px 8px' }}>
                {categoryTemplates.map((template) => (
                  <div
                    key={template.id}
                    onClick={() => addPlatformNodeWithTemplate(template)}
                    style={{
                      padding: '8px',
                      borderRadius: '6px',
                      cursor: 'pointer',
                      marginBottom: '2px',
                      background: 'transparent',
                      borderLeft: `2px solid ${config.color}`,
                      marginLeft: '4px',
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.background = '#334155'}
                    onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                  >
                    <div style={{ color: '#e2e8f0', fontSize: '11px', fontWeight: 500 }}>
                      {template.name}
                    </div>
                    <div style={{ color: '#64748b', fontSize: '10px' }}>
                      Click to add • {template.type}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Quick Add - Fixed */}
      <div
        style={{
          padding: '8px 12px',
          borderTop: '1px solid #334155',
          flexShrink: 0,
        }}
      >
        <button
          onClick={() => {
            const viewportCenter = editor.getViewportScreenCenter()
            const pagePoint = editor.screenToPage(viewportCenter)
            ;(editor as any).createShape({
              id: createShapeId(),
              type: 'skill-node',
              x: pagePoint.x - 100,
              y: pagePoint.y - 60,
              props: {
                w: 200, h: 120,
                skillType: config.nodeType,
                label: config.name,
                description: `${config.name} automation`,
                status: 'idle',
                inputs: ['person'],
                outputs: ['sent'],
              },
            })
          }}
          style={{
            width: '100%',
            background: config.color,
            border: 'none',
            padding: '8px',
            borderRadius: '6px',
            color: 'white',
            cursor: 'pointer',
            fontSize: '11px',
            fontWeight: 500,
          }}
        >
          {config.icon} Add {config.name} Node
        </button>
      </div>
    </>
  )

  return (
    <DraggablePanel
      title={`Templates (${templateStats.total})`}
      icon="📝"
      initialPosition={{ x: 12, y: 72 }}
      width={280}
      isOpen={isOpen}
      onToggle={() => setIsOpen(!isOpen)}
    >
      {panelContent}
    </DraggablePanel>
  )
}
