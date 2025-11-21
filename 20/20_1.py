from PIL import Image, ImageDraw, ImageFont
import math

# ====== ПАРАМЕТРЫ ======
OUT_W, OUT_H = 1200, 400
SCALE = 4
W, H = OUT_W * SCALE, OUT_H * SCALE

BLUE = "#0033ff"
RED = "#ff0033"
TEXT_COLOR = "#666666"
OUTLINE_COLOR = "black"

THICK = 16
THICK_S = int(THICK * SCALE)

# ====== ХЕЛПЕРЫ ======
def stroke_line(draw, p1, p2, width, fill):
    """Рисуем толстую линию."""
    draw.line([p1, p2], fill=fill, width=int(width))

def thick_rect(draw, xy, fill):
    """Толстый прямоугольник (заполненный)."""
    x1, y1, x2, y2 = [int(v) for v in xy]
    draw.rectangle((x1, y1, x2, y2), fill=fill)

def thick_round_rect(draw, xy, radius, fill):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)

# ====== ФУНКЦИИ РИСОВКИ БУКВ ======
def draw_D(draw, x, y):
    w = 150 * SCALE
    h = 220 * SCALE
    left = x
    top = y
    leg_w = 20 * SCALE
    thick_rect(draw, (left + 20*SCALE, top + 70*SCALE, left + 20*SCALE + leg_w, top + h), BLUE)
    thick_rect(draw, (left + w - 40*SCALE, top + 70*SCALE, left + w - 40*SCALE + leg_w, top + h), BLUE)
    thick_rect(draw, (left + 20*SCALE, top + 40*SCALE, left + w - 20*SCALE, top + 60*SCALE), RED)
    ellipse_bbox = (left + w - 120*SCALE, top + 40*SCALE, left + w + 40*SCALE, top + h - 20*SCALE)
    draw.ellipse(ellipse_bbox, fill=BLUE)
    thick_rect(draw, (left + w - 120*SCALE, top + 40*SCALE, left + w - 40*SCALE, top + h - 20*SCALE), BLUE)
    thick_rect(draw, (left + 20*SCALE, top + h - 20*SCALE, left + w - 20*SCALE, top + h), BLUE)

def draw_A(draw, x, y):
    left_bottom = (x + 20*SCALE, y + 220*SCALE)
    apex = (x + 90*SCALE, y + 20*SCALE)
    right_bottom = (x + 160*SCALE, y + 220*SCALE)
    stroke_line(draw, left_bottom, apex, THICK_S, BLUE)
    stroke_line(draw, right_bottom, apex, THICK_S, BLUE)
    thick_rect(draw, (x + 60*SCALE, y + 120*SCALE, x + 140*SCALE, y + 140*SCALE), RED)

def draw_N(draw, x, y):
    thick_rect(draw, (x + 10*SCALE, y + 20*SCALE, x + 30*SCALE, y + 240*SCALE), BLUE)
    thick_rect(draw, (x + 110*SCALE, y + 20*SCALE, x + 130*SCALE, y + 240*SCALE), BLUE)
    stroke_line(draw, (x + 30*SCALE, y + 30*SCALE), (x + 110*SCALE, y + 220*SCALE), THICK_S, RED)

def draw_I(draw, x, y):
    thick_rect(draw, (x + 10*SCALE, y + 20*SCALE, x + 30*SCALE, y + 240*SCALE), BLUE)
    thick_rect(draw, (x + 110*SCALE, y + 20*SCALE, x + 130*SCALE, y + 240*SCALE), BLUE)
    stroke_line(draw, (x + 30*SCALE, y + 40*SCALE), (x + 110*SCALE, y + 220*SCALE), max(1, int(THICK_S/1.2)), RED)

def draw_L(draw, x, y):
    thick_rect(draw, (x + 20*SCALE, y + 100*SCALE, x + 40*SCALE, y + 240*SCALE), BLUE)
    thick_rect(draw, (x + 100*SCALE, y + 100*SCALE, x + 120*SCALE, y + 240*SCALE), BLUE)
    arc_bbox = (x + 20*SCALE, y + 20*SCALE, x + 120*SCALE, y + 140*SCALE)
    draw.pieslice(arc_bbox, start=180, end=360, fill=RED)
    thick_rect(draw, (x + 20*SCALE, y + 100*SCALE, x + 120*SCALE, y + 120*SCALE), (255,255,255))

# ====== СОЗДАЁМ И РИСУЕМ ======
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

start_x = 60 * SCALE
start_y = 60 * SCALE

draw_D(draw, start_x, start_y)
draw_A(draw, start_x + (200 * SCALE), start_y)
draw_N(draw, start_x + (380 * SCALE), start_y)
draw_I(draw, start_x + (560 * SCALE), start_y)
draw_L(draw, start_x + (740 * SCALE), start_y)

dot_positions = [
    (start_x + 240*SCALE, start_y - 30*SCALE),
    (start_x + 420*SCALE, start_y - 30*SCALE),
    (start_x + 800*SCALE, start_y - 30*SCALE),
]
for cx, cy in dot_positions:
    r = 8 * SCALE
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLUE)

try:
    font = ImageFont.truetype("arial.ttf", 20 * SCALE)
except Exception:
    font = ImageFont.load_default()
draw.text((900*SCALE, 320*SCALE), "by Python", fill=TEXT_COLOR, font=font)

small = img.resize((OUT_W, OUT_H), resample=Image.LANCZOS)

outline_draw = ImageDraw.Draw(small)
outline_rects = [
    (100, 150, 120, 320), (190, 150, 210, 320), (100, 130, 210, 150),
    (320, 180, 360, 200),
    (440, 100, 460, 320), (520, 100, 540, 320), (440, 200, 540, 220),
    (580, 100, 600, 320), (660, 100, 680, 320),
    (720, 150, 740, 320), (800, 150, 820, 320)
]
for rect in outline_rects:
    outline_draw.rectangle(rect, outline=OUTLINE_COLOR, width=1)

out_name = "danil_art_sharp.png"
small.save(out_name, "PNG", quality=100, dpi=(300,300))
print("Сохранено:", out_name)
small.show()