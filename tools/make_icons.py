"""Generate PWA icons (run in CI before deploy): python tools/make_icons.py"""
import os
from PIL import Image, ImageDraw

def icon(n):
    S = n * 4
    im = Image.new('RGB', (S, S), '#070920')
    d = ImageDraw.Draw(im)
    for y in range(S):
        a = max(0, 1 - y / S * 1.4)
        d.line([(0, y), (S, y)], fill=(int(7 + 20 * a), int(9 + 22 * a), int(32 + 60 * a)))
    m, gap = S * 0.14, S * 0.035
    w = (S - 2 * m - 3 * gap) / 4
    top, bh = S * 0.50, S * 0.17
    d.rectangle([0, 0, S * 0.025, S], fill='#2ec5ff')
    d.rectangle([S * 0.975, 0, S, S], fill='#ff3d9a')
    for i in range(4):
        x = m + i * (w + gap)
        y = S * 0.22 - (i % 2) * S * 0.08
        d.rectangle([x, y, x + w, y + S * 0.04], fill='#ffffff')
        d.rounded_rectangle([x, top, x + w, top + bh], radius=S * 0.025, fill='#eef1ff')
    for j in range(2):
        x = m + j * 2 * (w + gap)
        y = top + bh + gap * 1.3
        d.rounded_rectangle([x, y, x + 2 * w + gap, y + S * 0.11], radius=S * 0.025, fill='#ff8a1f')
    d.rectangle([m, S * 0.44, S - m, S * 0.448], fill='#ffffff')
    return im.resize((n, n), Image.LANCZOS)

os.makedirs('icons', exist_ok=True)
icon(192).save('icons/icon-192.png')
icon(512).save('icons/icon-512.png')
icon(180).save('icons/apple-touch-icon.png')
print('icons generated')
