import argparse
import json
import csv


# Конвертация JSON в CSV
def json2csv(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            # Записываем заголовки (из ключей первого словаря)
            writer.writerow(data[0].keys())
            # Записываем данные
            for entry in data:
                writer.writerow(entry.values())
        print(f"Конвертация из JSON в CSV завершена: {output_file}")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")


# Конвертация CSV в JSON
def csv2json(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)  # Заголовки (первый ряд)
            rows = [dict(zip(headers, row)) for row in reader]

        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4)
        print(f"Конвертация из CSV в JSON завершена: {output_file}")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    subparsers = parser.add_subparsers(dest="cmd")

    # Подкоманда json2csv — конвертация из JSON в CSV
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Путь к файлу JSON"
    )
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Путь к файлу CSV"
    )

    # Подкоманда csv2json — конвертация из CSV в JSON
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Путь к файлу CSV"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Путь к файлу JSON"
    )

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json2csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv2json(args.input, args.output)


if __name__ == "__main__":
    main()
