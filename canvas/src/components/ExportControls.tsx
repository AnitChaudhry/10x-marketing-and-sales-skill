import { useEditor, getSnapshot, loadSnapshot } from 'tldraw'
import { useState, useCallback, useRef } from 'react'

export function ExportControls() {
  const editor = useEditor()
  const [isExporting, setIsExporting] = useState(false)
  const [showMenu, setShowMenu] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const exportToPNG = useCallback(async () => {
    setIsExporting(true)
    try {
      const shapeIds = [...editor.getCurrentPageShapeIds()]
      if (shapeIds.length === 0) {
        alert('No shapes to export!')
        return
      }

      const { blob } = await editor.toImage(shapeIds, {
        format: 'png',
        background: true,
        padding: 32,
        scale: 2,
      })

      const link = document.createElement('a')
      link.href = URL.createObjectURL(blob)
      link.download = `10x-workflow-${Date.now()}.png`
      link.click()
      URL.revokeObjectURL(link.href)

      console.log('Exported as PNG')
    } catch (error) {
      console.error('PNG export failed:', error)
      alert('Export failed. Try selecting fewer shapes.')
    } finally {
      setIsExporting(false)
      setShowMenu(false)
    }
  }, [editor])

  const exportToSVG = useCallback(async () => {
    setIsExporting(true)
    try {
      const shapeIds = [...editor.getCurrentPageShapeIds()]
      if (shapeIds.length === 0) {
        alert('No shapes to export!')
        return
      }

      const { blob } = await editor.toImage(shapeIds, {
        format: 'svg',
        background: false,
        padding: 32,
      })

      const link = document.createElement('a')
      link.href = URL.createObjectURL(blob)
      link.download = `10x-workflow-${Date.now()}.svg`
      link.click()
      URL.revokeObjectURL(link.href)

      console.log('Exported as SVG')
    } catch (error) {
      console.error('SVG export failed:', error)
      alert('Export failed. Try selecting fewer shapes.')
    } finally {
      setIsExporting(false)
      setShowMenu(false)
    }
  }, [editor])

  const saveCanvasFile = useCallback(() => {
    try {
      const snapshot = getSnapshot(editor.store)
      const blob = new Blob([JSON.stringify(snapshot, null, 2)], {
        type: 'application/json',
      })

      const link = document.createElement('a')
      link.href = URL.createObjectURL(blob)
      link.download = `10x-workflow-${Date.now()}.10x`
      link.click()
      URL.revokeObjectURL(link.href)

      console.log('Canvas saved to file')
    } catch (error) {
      console.error('Save failed:', error)
      alert('Failed to save canvas')
    }
    setShowMenu(false)
  }, [editor])

  const loadCanvasFile = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    const reader = new FileReader()
    reader.onload = (e) => {
      try {
        const content = e.target?.result as string
        const snapshot = JSON.parse(content)
        loadSnapshot(editor.store, snapshot)
        console.log('Canvas loaded from file')
      } catch (error) {
        console.error('Load failed:', error)
        alert('Failed to load canvas file. Make sure it\'s a valid .10x file.')
      }
    }
    reader.readAsText(file)

    // Reset input
    event.target.value = ''
    setShowMenu(false)
  }, [editor])

  const clearCanvas = useCallback(() => {
    if (confirm('Clear entire canvas? This cannot be undone.')) {
      const shapes = editor.getCurrentPageShapes()
      editor.deleteShapes(shapes.map((s) => s.id))
      console.log('Canvas cleared')
    }
    setShowMenu(false)
  }, [editor])

  const copyToClipboard = useCallback(async () => {
    try {
      const shapeIds = [...editor.getCurrentPageShapeIds()]
      if (shapeIds.length === 0) {
        alert('No shapes to copy!')
        return
      }

      const { blob } = await editor.toImage(shapeIds, {
        format: 'png',
        background: true,
        padding: 16,
        scale: 2,
      })

      await navigator.clipboard.write([
        new ClipboardItem({
          'image/png': blob,
        }),
      ])

      alert('Copied to clipboard!')
    } catch (error) {
      console.error('Copy failed:', error)
      alert('Copy to clipboard failed')
    }
    setShowMenu(false)
  }, [editor])

  return (
    <div
      style={{
        position: 'absolute',
        bottom: '20px',
        right: '20px',
        zIndex: 100,
        pointerEvents: 'all',
      }}
    >
      {/* Hidden file input */}
      <input
        ref={fileInputRef}
        type="file"
        accept=".10x,.json"
        onChange={loadCanvasFile}
        style={{ display: 'none' }}
      />

      {/* Menu */}
      {showMenu && (
        <div
          style={{
            position: 'absolute',
            bottom: '50px',
            right: '0',
            background: '#1e1e2e',
            borderRadius: '8px',
            boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
            border: '1px solid #334155',
            padding: '8px',
            minWidth: '160px',
          }}
        >
          <MenuItem
            icon="📸"
            label="Export PNG"
            onClick={exportToPNG}
            disabled={isExporting}
          />
          <MenuItem
            icon="🎨"
            label="Export SVG"
            onClick={exportToSVG}
            disabled={isExporting}
          />
          <div style={{ height: '1px', background: '#334155', margin: '8px 0' }} />
          <MenuItem
            icon="📋"
            label="Copy to Clipboard"
            onClick={copyToClipboard}
          />
          <div style={{ height: '1px', background: '#334155', margin: '8px 0' }} />
          <MenuItem
            icon="💾"
            label="Save Canvas"
            onClick={saveCanvasFile}
          />
          <MenuItem
            icon="📂"
            label="Load Canvas"
            onClick={() => fileInputRef.current?.click()}
          />
          <div style={{ height: '1px', background: '#334155', margin: '8px 0' }} />
          <MenuItem
            icon="🗑️"
            label="Clear Canvas"
            onClick={clearCanvas}
            danger
          />
        </div>
      )}

      {/* Toggle Button */}
      <button
        onClick={() => setShowMenu(!showMenu)}
        style={{
          width: '48px',
          height: '48px',
          borderRadius: '50%',
          background: showMenu ? '#6366f1' : '#1e1e2e',
          border: '1px solid #334155',
          color: 'white',
          fontSize: '20px',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
          transition: 'all 0.2s ease',
        }}
        title="Export & Save Options"
      >
        {isExporting ? '⏳' : '💾'}
      </button>
    </div>
  )
}

function MenuItem({
  icon,
  label,
  onClick,
  disabled,
  danger,
}: {
  icon: string
  label: string
  onClick: () => void
  disabled?: boolean
  danger?: boolean
}) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      style={{
        width: '100%',
        background: 'transparent',
        border: 'none',
        padding: '8px 12px',
        borderRadius: '4px',
        cursor: disabled ? 'not-allowed' : 'pointer',
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        color: danger ? '#ef4444' : '#e2e8f0',
        opacity: disabled ? 0.5 : 1,
        textAlign: 'left',
        fontSize: '12px',
      }}
      onMouseEnter={(e) => {
        if (!disabled) {
          e.currentTarget.style.background = danger ? '#dc262620' : '#334155'
        }
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.background = 'transparent'
      }}
    >
      <span>{icon}</span>
      <span>{label}</span>
    </button>
  )
}
