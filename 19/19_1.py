from pathlib import Path
from PIL import Image
import os


def average_color(img: Image.Image):
    img_rgb = img.convert("RGB")
    pixels = list(img_rgb.getdata())
    num_pixels = len(pixels)

    if num_pixels == 0:
        raise ValueError("Изображение пустое")

    r_sum = g_sum = b_sum = 0
    for r, g, b in pixels:
        r_sum += r
        g_sum += g
        b_sum += b

    avg_r = int(r_sum / num_pixels)
    avg_g = int(g_sum / num_pixels)
    avg_b = int(b_sum / num_pixels)

    return (avg_r, avg_g, avg_b)


def create_solid_image(size, color):
    return Image.new("RGB", size, color)


def main(input_path: Path, output_path: Path):
    if not input_path.exists():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    img = Image.open(input_path)
    avg_col = average_color(img)

    print(f"Средний цвет изображения: RGB{avg_col}")

    new_img = create_solid_image(img.size, avg_col)

    new_img.show(title="Средний цвет")

    new_img.save(output_path)
    print(f"Изображение сохранено: {output_path}")


inp = Path(r"C:\Users\FamilyGame\Desktop\19\input.png")
outp = Path(r"C:\Users\FamilyGame\Desktop\19\output.png")



print(f"Проверяем путь: {inp}")
print(f"Файл существует: {inp.exists()}")

if inp.exists():
    main(inp, outp)
else:
    print("❌ Файл не найден! Проверьте:")
    print(f"   - Существует ли папка: {inp.parent}")
    print(f"   - Есть ли файл input.png в папке 19")
    print(f"   - Правильно ли указано имя файла")

    if inp.parent.exists():
        print(f"\n📁 Содержимое папки {inp.parent}:")
        for file in inp.parent.iterdir():
            print(f"   - {file.name}")