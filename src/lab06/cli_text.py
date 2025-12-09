import argparse
import re
from collections import Counter


# Функция для вывода содержимого файла
def cat(input_file, number_lines=False):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for idx, line in enumerate(file, 1):
                if number_lines:
                    print(f"{idx}: {line.strip()}")
                else:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")


# Функция для анализа частоты слов
def stats(input_file, top=5):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = re.findall(r"\w+", text)
            word_counts = Counter(words)
            most_common = word_counts.most_common(top)
            print(f"Топ {top} самых часто встречающихся слов:")
            for word, count in most_common:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")


def main():
    parser = argparse.ArgumentParser(
        description="CLI утилиты для работы с текстовыми файлами"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Подкоманда cat — для вывода содержимого файла
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats — для анализа частоты слов
    stats_parser = subparsers.add_parser("stats", help="Анализ частотности слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество часто встречающихся слов"
    )

    args = parser.parse_args()

    if args.command == "cat":
        cat(args.input, args.n)
    elif args.command == "stats":
        stats(args.input, args.top)


if __name__ == "__main__":
    main()
