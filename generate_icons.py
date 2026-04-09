#!/usr/bin/env python3
"""
generate_icons.py
Run this once to generate all app icons needed for the PWA.
Usage: python3 generate_icons.py

Requires: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
OUTPUT_DIR = "icons"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def make_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background circle - dark green
    padding = int(size * 0.05)
    draw.ellipse([padding, padding, size-padding, size-padding],
                 fill="#1a472a")

    # Cricket bat emoji approximation using text
    font_size = int(size * 0.5)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text = "🏏"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) // 2
    y = (size - text_h) // 2 - int(size * 0.05)

    draw.text((x, y), text, font=font, fill="white")

    path = os.path.join(OUTPUT_DIR, f"icon-{size}.png")
    img.save(path, "PNG")
    print(f"  ✓ Generated icons/icon-{size}.png")

print("Generating tournament app icons...")
for s in SIZES:
    make_icon(s)
print("\nAll icons generated in /icons folder!")
print("Place the icons/ folder next to index.html")
