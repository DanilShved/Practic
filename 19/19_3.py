from PIL import Image
from pathlib import Path


def process(img):
    """
    Обрабатывает изображение:
    - Конвертирует в RGB
    - Для каждого пикселя:
      * Красный канал = минимальное значение из RGB
      * Зеленый канал = оригинальное значение
      * Синий канал = максимальное значение из RGB
    """
    img = img.convert("RGB")  # убираем альфа, если есть
    w, h = img.size
    pix = img.load()

    for y in range(h):
        for x in range(w):
            r, g, b = pix[x, y]
            mn = min(r, g, b)
            mx = max(r, g, b)
            # красный ← min, синий ← max, зелёный → оригинальный
            pix[x, y] = (mn, g, mx)

    return img


def main(in_path, out_path):
    try:
        input_path = Path(in_path)
        if not input_path.exists():
            raise FileNotFoundError(f"❌ Входной файл не найден: {in_path}")

        print(f"✅ Загружаем изображение: {input_path}")
        im = Image.open(input_path)
        print(f"📏 Размер изображения: {im.size}, формат: {im.format}")

        # Обрабатываем изображение
        print("🔄 Обрабатываем пиксели...")
        processed = process(im)
        print("✅ Обработка пикселей завершена")

        flipped = processed.transpose(Image.FLIP_TOP_BOTTOM)
        print("🔄 Изображение отражено")

        flipped.show(title="Обработанное изображение")
        flipped.save(out_path)
        print(f"💾 Сохранено → {out_path}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

    return True



input_path = r"C:\Users\FamilyGame\Desktop\19\input1.png"
output_path = r"C:\Users\FamilyGame\Desktop\19\output2.png"


print("=" * 50)
print("🔍 ПРОВЕРКА ФАЙЛОВ")
print("=" * 50)

input_file = Path(input_path)
output_dir = Path(output_path).parent

print(f"📁 Входной файл: {input_path}")
print(f"📁 Выходной файл: {output_path}")
print(f"✅ Входной файл существует: {input_file.exists()}")
print(f"✅ Папка для сохранения существует: {output_dir.exists()}")

if input_file.exists():
    print("\n🎯 ЗАПУСК ОБРАБОТКИ...")
    success = main(input_path, output_path)
    if success:
        print("✨ Обработка завершена успешно!")
    else:
        print("💥 Обработка завершена с ошибками")
else:
    print("\n❌ Файл не найден! Проверьте:")
    print(f"   - Папка {output_dir} существует: {output_dir.exists()}")


    if output_dir.exists():
        print(f"\n📁 Содержимое папки {output_dir}:")
        files = list(output_dir.glob("*.png")) + list(output_dir.glob("*.jpg"))
        if files:
            for file in files:
                print(f"   - {file.name}")
        else:
            print("   В папке нет PNG/JPG файлов")