import AppKit

// Render the editable vector card at its Open Graph dimensions.
let root = URL(fileURLWithPath: #filePath)
    .deletingLastPathComponent().deletingLastPathComponent()
let input = root.appendingPathComponent("assets/social-card.svg")
let output = root.appendingPathComponent("assets/social-card.png")
let size = NSSize(width: 1200, height: 630)

guard let image = NSImage(contentsOf: input),
      let bitmap = NSBitmapImageRep(
        bitmapDataPlanes: nil, pixelsWide: 1200, pixelsHigh: 630,
        bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true,
        isPlanar: false, colorSpaceName: .deviceRGB,
        bytesPerRow: 0, bitsPerPixel: 0
      ), let context = NSGraphicsContext(bitmapImageRep: bitmap) else {
    fatalError("Could not load the SVG or create the rendering context.")
}

bitmap.size = size
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = context
image.draw(in: NSRect(origin: .zero, size: size))
context.flushGraphics()
NSGraphicsContext.restoreGraphicsState()

guard let data = bitmap.representation(using: .png, properties: [:]) else {
    fatalError("Could not encode the social card.")
}
try data.write(to: output, options: .atomic)
print("Rendered assets/social-card.png (1200 × 630).")
