import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if csv_file.suffix != ".csv":
        raise ValueError(f"Неверный тип файла: {csv_path}. Ожидается .csv")

    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    # Ридинг из csv
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError(f"Пустой CSV файл: {csv_path}")
    # Врайтинг в xlsx
    with open(xlsx_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Файл успешно преобразован в XLSX: {xlsx_path}")


# Пути к файлам
csv_file_path = "src/data/out/people_from_json.csv"
xlsx_file_path = "src/data/out/people_from_csv.xlsx"

csv_to_xlsx(csv_file_path, xlsx_file_path)
