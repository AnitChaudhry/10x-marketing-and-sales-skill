import { useEditor, useValue } from 'tldraw'

/**
 * N8N-style dotted grid background for the canvas.
 */
export function DottedGrid() {
  const editor = useEditor()

  const camera = useValue('camera', () => editor.getCamera(), [editor])
  const bounds = useValue('bounds', () => editor.getViewportScreenBounds(), [editor])

  const zoom = camera.z
  const gridSize = 20

  // Calculate offset based on camera position
  const offsetX = (camera.x * zoom) % (gridSize * zoom)
  const offsetY = (camera.y * zoom) % (gridSize * zoom)

  // Dot size that's visible at various zoom levels
  const dotSize = Math.max(1, Math.min(2, zoom * 1.5))

  // Don't render if zoomed out too far
  if (zoom < 0.05) {
    return (
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundColor: '#1a1a2e',
          pointerEvents: 'none',
        }}
      />
    )
  }

  const scaledGrid = gridSize * zoom

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        backgroundColor: '#1a1a2e',
        pointerEvents: 'none',
        overflow: 'hidden',
      }}
    >
      <svg
        width="100%"
        height="100%"
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
        }}
      >
        <defs>
          <pattern
            id="grid-dots"
            x={offsetX}
            y={offsetY}
            width={scaledGrid}
            height={scaledGrid}
            patternUnits="userSpaceOnUse"
          >
            <circle
              cx={scaledGrid / 2}
              cy={scaledGrid / 2}
              r={dotSize}
              fill="#3f4865"
            />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid-dots)" />
      </svg>
    </div>
  )
}
