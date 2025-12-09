import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file.suffix != ".json":
        raise ValueError(f"Неверный тип файла: {json_path}. Ожидается .json")

    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    # Ридинг из json
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        raise ValueError(f"Пустой JSON файл: {json_path}")

    # Врайтинг в csv
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        else:
            raise ValueError(f"Пустой JSON файл: {json_path}")

    print(f"Файл успешно преобразован в CSV: {csv_path}")


# Пути к файлам
json_file_path = "src/data/samples/people.json"
csv_file_path = "src/data/out/people_from_json.csv"

json_to_csv(json_file_path, csv_file_path)
