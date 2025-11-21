from PIL import Image
import sys
from pathlib import Path


def main(in_path, out_path):
    try:

        if not Path(in_path).exists():
            raise FileNotFoundError(f"Входной файл не найден: {in_path}")


        img = Image.open(in_path)
        print(f"✅ Изображение загружено: {img.size}, формат: {img.format}")


        bw = img.convert("L")
        print("✅ Конвертировано в черно-белое")


        flipped = bw.transpose(Image.FLIP_LEFT_RIGHT)
        print("✅ Изображение отражено")


        resized = flipped.resize((400, 400), Image.LANCZOS)
        print("✅ Размер изменен на 400×400 px")


        resized.show(title="Result")
        resized.save(out_path)
        print(f"✅ Сохранено → {out_path}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)


input_path = r"C:\Users\FamilyGame\Desktop\19\input.png"
output_path = r"C:\Users\FamilyGame\Desktop\19\output1.png"

print(f"🔍 Проверяем путь: {input_path}")

if Path(input_path).exists():
    print("✅ Входной файл найден, запускаем обработку...")
    main(input_path, output_path)
else:
    print("❌ Входной файл не найден!")
    print("Пожалуйста, проверьте:")
    print(f"1. Существует ли папка: {Path(input_path).parent}")
    print(f"2. Находится ли файл input.png в этой папке")
    print(f"3. Правильно ли указано имя файла")

    folder = Path(input_path).parent
    if folder.exists():
        print(f"\n📁 Содержимое папки {folder}:")
        files = list(folder.glob("*.*"))
        if files:
            for file in files:
                print(f"   - {file.name}")
        else:
            print("   Папка пуста")