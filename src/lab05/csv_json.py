import json
import csv
from pathlib import Path


def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        if not data:
            raise ValueError

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    except FileNotFoundError:
        raise FileNotFoundError
