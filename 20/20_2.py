from PIL import Image, ImageDraw

# Размеры картинки
W, H = 800, 600

# Фон – небо
img = Image.new('RGB', (W, H), color='#87CEEB')
draw = ImageDraw.Draw(img)

# Горизонт
horizon_y = int(H * 0.6)
draw.line([(0, horizon_y), (W, horizon_y)], fill='#8B4513', width=2)   # земля

# Трава от горизонта до низа
draw.rectangle([(0, horizon_y), (W, H)], fill='#228B22')   # forest green

# Горные треугольники
mountains = [
    [(150, horizon_y), (300, 250), (450, horizon_y)],
    [(350, horizon_y), (500, 200), (650, horizon_y)],
    [(550, horizon_y), (700, 280), (750, horizon_y)]
]

for pts in mountains:
    draw.polygon(pts, fill='#D3D3D3')   # светло‑серый

    # Снежные шапки
    peak = min(pts, key=lambda p: p[1])          # точка с минимальным y (самая высокая)
    cap_w, cap_h = 30, 20                       # размеры шапки
    cap_pts = [
        (peak[0] - cap_w // 2, peak[1]+cap_h),
        (peak[0], peak[1]),
        (peak[0] + cap_w // 2, peak[1]+cap_h)
    ]
    draw.polygon(cap_pts, fill='#FFFFFF')       # белый снег

# Солнце
sun_center = (W - 100, 80)
r = 40
draw.ellipse(
    [(sun_center[0] - r, sun_center[1] - r),
     (sun_center[0] + r, sun_center[1] + r)],
    fill='#FFD700')   # золотой

# Сохраняем и показываем
img.save('minimalist_mountain.png')
img.show()