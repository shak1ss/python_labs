import csv
import re
from pathlib import Path
from collections import Counter


# Ридинг
def read_text(path: str) -> str:
    p = Path(path)
    try:
        with p.open("r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
        return ""


# Приведение в нижний регистр
def normalize(text: str) -> str:
    return text.lower().replace("\n", " ").replace("\r", " ")


# Разделение на слова
def tokenize(text: str) -> list[str]:
    WORD_RE = re.compile(r"\b\w+\b")  # Регулярное выражение для поиска слов
    return WORD_RE.findall(text)


# Подсчет частоты
def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))


# Сортировка по частоте
def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)


# Функции записи в csv
def write_csv(rows: list[list[str]], path: str, header=None):
    with open(path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)


# Все вместе
def process_and_write_text():
    text = read_text("src/data/lab04/input.txt")
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    sorted_freq = sorted_word_counts(freq)

    # Запись в csv
    write_csv(sorted_freq, "src/data/lab04/report.csv", header=["word", "count"])


# Запуск
if __name__ == "__main__":
    process_and_write_text()
