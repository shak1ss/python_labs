# effective-broccoli

## Лабораторная работа 1

### Задание 1
```python
name = (input("Имя: "))
age = int(input("Возраст: "))
print (f"Привет, {name}! Через год тебе будет {age+1}.")
```
![Картинка 1](./images/lab01/01.png)# python_labs

### Задание 2
```python
a = float(input("a: "))
b = float(input("b: "))
sum = a + b
average = sum /2
print (f"sum - {round(sum, 2)}; average - {round(average, 2)}")
```
![Картинка 2](./images/lab01/02.png)# python_labs

### Задание 3
```python
price = float(input("Price: "))
discount = float(input("Discount: "))
vat = float(input("VAT: "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print (f"База после скидки: {base:.2f} ₽\n"
       f"НДС: {vat_amount:.2f} ₽\n"
       f"Итого к оплате: {total:.2f} ₽\n")
```
![Картинка 3](./images/lab01/03.png)# python_labs

### Задание 4
```python
m = int(input("Целые минуты: "))
hour = m // 60
min = m % 60
print (f"{hour}:{min:02d}")
```
![Картинка 4](./images/lab01/04.png)# python_labs

### Задание 5
```python
FIO = input("ФИО: ")
FIO = ' '.join(FIO.split())
splitwords = FIO.split()
FIO_2 = FIO.strip()
fletters = []
str_fletters = '' 
for word in splitwords:
    fletters.append(word[0].upper())
for letter in fletters:
    str_fletters += letter
print(f"Инициалы: {str_fletters}")
print(f"Длина (символов): {len(FIO_2)}")
```
![Картинка 5](./images/lab01/05.png)# python_labs



## Лабораторная работа 2

### Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:    
    if not nums:    
        raise ValueError("Список пуст")    
    return (min(nums),max(nums))    
    
def unique_sorted(nums: list[float | int]) -> list[float | int]:     
    return sorted(set(nums)) if nums else []       

def flatten(mat: list[list | tuple]) -> list:   
    if not mat: 
        raise ValueError("Список пуст")   

    result = []
    for row in mat:
        if not isinstance(row,(list,tuple)): 
            raise TypeError("строка не строка строк матрицы")  
        result.extend(row)  
    return result 
    


def show_min_max(x):
    try:
        print(x, "→", min_max(x))
    except ValueError:
        print(x, "→ ValueError")

def show_unique_sorted(x):
    print(x, "→", unique_sorted(x))

def show_flatten(x):
    try:
        print(x, "→", flatten(x))
    except TypeError:
        print(x, "→ TypeError")


show_min_max([1337, -1, 6, 5, 0])
show_min_max([428])
show_min_max([-5, -29, -9])
show_min_max([])
show_min_max([1.55, 2, 2.1, -3.9])

print()

show_unique_sorted([1337, 2, 4, 2, 1337])
show_unique_sorted([])
show_unique_sorted([-2, -2, 0, 3, 3])
show_unique_sorted([1.0, 1, 2.5, 2.5, 0])

print()

show_flatten([[1, 2], [8, 9]])
show_flatten([[1], [23, 73], (43, 53)])
show_flatten([[1], [6, 5], [1]])
show_flatten([[1, 2], "strcmp"])
```
![Картинка 1](./images/lab02/arrays.png)# python_labs

### Задание 2
```python
def transpose(mat: list[list[int | float]]) -> list[list[int | float]]:
    if not mat:
        return []
    
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            raise ValueError("Матрица рваная")

    result = []
    for i in range(len(mat[0])):
        new_list = []
        for k in range(len(mat)):
            new_list.append(mat[k][i])  
        result.append(new_list)         
    return result 



def row_sums(mat: list[list[int | float]]) -> list[float]:
    if not mat:
        return []
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):  
            raise ValueError("Матрица рваная")
    result = []
    for row in mat:
        s = 0.0
        for x in row:
            s += x
        result.append(s)
    return result


def col_sums(mat: list[list[int | float]]) -> list[float]:
    if not mat:
        return []
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            raise ValueError("Матрица рваная")
    rows = len(mat)        
    cols = len(mat[0]) 
    result = [0.0] * cols
    for j in range(cols):
        s = 0.0
        for i in range(rows):
            s += mat[i][j]
        result[j] = s
    return result



def show_transpose(m):
    try:
        print(f"{str(m):<25} → {transpose(m)}")
    except ValueError:
        print(f"{str(m):<25} → ValueError")

def show_row_sums(m):
    try:
        print(f"{str(m):<25} → {row_sums(m)}")
    except ValueError:
        print(f"{str(m):<25} → ValueError")

def show_col_sums(m):
    try:
        print(f"{str(m):<25} → {col_sums(m)}")
    except ValueError:
        print(f"{str(m):<25} → ValueError")

show_transpose([[11, 12, 13], [41, 52, 63]])   
show_transpose([[-3, 3], [7, -7]])    
show_transpose([[0, 0], [0, 0]]) 
show_transpose([[1, 2], [3]])  
print()
show_row_sums([[1, 12, 23], [44, 65, 86]])   
show_row_sums([[-1, 5], [2, -10]])    
show_row_sums([[1, 1], [1, 1]]) 
show_row_sums([[1, 2], [3]])  
print()
show_col_sums([[1, 99, 366], [42, 52, 61]])   
show_col_sums([[-1, 4], [8, -10]])    
show_col_sums([[0, 0], [0, 0]]) 
show_col_sums([[1, 2], [5]])    
```
![Картинка 2](./images/lab02/matrix.png)# python_labs

### Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("Некорректное ФИО")
    surname = parts[0].capitalize()
    initial = "".join(w[0].upper()+"." for w in parts [1:3])
    group1 = " ".join(group.split()).upper()
    if not group1:
        raise ValueError("Группа не должна быть пустой")
    if not isinstance(gpa,(int,float)):
        raise TypeError("GPA должен быть числом")
    gpa_str = f"{float(gpa):.2f}"

    return f"{surname} {initial}, гр. {group1}, GPA {gpa_str}"

print(format_record(("Иванов Иван Иванович", "BVIT-25", 4.6)))
print(format_record(("Петров Пётр", "ИКВО-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "ИКВО-12", 5.0)))
print(format_record(("  сидорова   анна  сергеевна ", "ABB-01", 3.999)))
print(format_record((" ", "BVIT-25", 4.6)))
```
![Картинка 3](./images/lab02/tuples.png)# python_labs

## Лабораторная работа 3

### Задание А
```
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    s=text
    if casefold :
        s=s.casefold()
    if yo2e :
        s=s.replace("ё","е").replace("Ё","Е")
    s=s.replace("\t"," ").replace("\r"," ").replace("\n"," ")
    s = ' '.join(s.split())
    s=s.strip()

    return s

def tokenize(text: str) -> list[str]:
    pattern= r'\w+(?:-\w+)*'
    tokenstext = re.findall(pattern, text)

    return tokenstext

def count_freq(tokens: list[str]) -> dict[str, int]:
    counts={}
    for word in tokens:
        counts[word]=counts.get(word,0)+1
    return counts

def sort_key(item):
    return [-item[1], item[0]]

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_freq= sorted(freq.items(),key=sort_key)
    top_n=[]

    for i in range(min(n, len(sorted_freq))):
        top_n.append((sorted_freq[i][0], sorted_freq[i][1]))

    return top_n

def summary(text):
    normalized_text = normalize(text)

    tokens = tokenize(normalized_text)

    total_words = len(tokens)
    freq_sorted = count_freq(tokens)
    unique_words = len(freq_sorted)
    top = top_n(freq_sorted, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")

    for word, count in top:
        print(f"{word}:{count}")
```
Отдельный тестовый файл с тест-кейсами
```
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.lib.text import *

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```
![Картинка 1](./images/lab03/text.png)# python_labs
### Задание B
```
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    input_text = sys.stdin.readline()


    text_norm = normalize(input_text)
    tokens = tokenize(text_norm)
    freq = count_freq(tokens)

    words_total = len(tokens)
    unique_words = len(freq)

    top_words = top_n(freq, 5)

    print(f"Всего слов: {words_total}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
![Картинка 2](./images/lab03/text_stats.png)# python_labs

## Лабораторная работа 4

### Задание A
```
from pathlib import Path
from typing import Iterable, Sequence
import csv

# Ридинг
def read_text(path: str, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        return p.read_text(encoding=encoding) 
    except UnicodeDecodeError:
        print("Ошибка кодировки.")
        exit(1)  

# Врайтинг
def write_csv(rows: Iterable[Sequence], path: str | Path, header: list[str] = None) -> None:
    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f: 
        writer = csv.writer(f)
        if header:
            writer.writerow(header)  
        writer.writerows(rows)  
```
### Задание B
```
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
```
![Картинка 1][./images/lab04/text_report.png]# python_labs


## Лабораторная работа 5

### Тестовые данные (people.json)
![Картинка 1](./images/lab05/people.png)# python_labs

### Задание A
```
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file.suffix != '.json':
        raise ValueError(f"Неверный тип файла: {json_path}. Ожидается .json")
    
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
# Ридинг из json
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        raise ValueError(f"Пустой JSON файл: {json_path}")

# Врайтинг в csv
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        else:
            raise ValueError(f"Пустой JSON файл: {json_path}")
        
    print(f"Файл успешно преобразован в CSV: {csv_path}")

# Пути к файлам
json_file_path = 'src/data/samples/people.json' 
csv_file_path = 'src/data/out/people_from_json.csv'  

json_to_csv(json_file_path, csv_file_path)
```
![Картинка 2](./images/lab05/people_from_json.png)# python_labs


### Задание B
```
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if csv_file.suffix != '.csv':
        raise ValueError(f"Неверный тип файла: {csv_path}. Ожидается .csv")
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
# Ридинг из csv
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError(f"Пустой CSV файл: {csv_path}")
# Врайтинг в xlsx
    with open(xlsx_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"Файл успешно преобразован в XLSX: {xlsx_path}")

# Пути к файлам
csv_file_path = 'src/data/out/people_from_json.csv'  
xlsx_file_path = 'src/data/out/people_from_csv.xlsx'  

csv_to_xlsx(csv_file_path, xlsx_file_path)
```
![Картинка 3](./images/lab05/people_from_csv.png)# python_labs

## Лабораторная работа 6

### Задание 1
```
import argparse
import re
from collections import Counter

# Функция для вывода содержимого файла
def cat(input_file, number_lines=False):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
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
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\w+', text)
            word_counts = Counter(words)
            most_common = word_counts.most_common(top)
            print(f"Топ {top} самых часто встречающихся слов:")
            for word, count in most_common:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")

def main():
    parser = argparse.ArgumentParser(description="CLI утилиты для работы с текстовыми файлами")
    subparsers = parser.add_subparsers(dest="command")

    # Подкоманда cat — для вывода содержимого файла
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats — для анализа частоты слов
    stats_parser = subparsers.add_parser("stats", help="Анализ частотности слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество часто встречающихся слов")

    args = parser.parse_args()

    if args.command == "cat":
        cat(args.input, args.n)
    elif args.command == "stats":
        stats(args.input, args.top)

if __name__ == "__main__":
    main()
```
![Картинка 1](./images/lab06/cat.png)# python_labs
![Картинка 2](./images/lab06/stats.png)# python_labs

### Задание 2
```
import argparse
import json
import csv

# Конвертация JSON в CSV
def json2csv(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
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
        with open(input_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)  # Заголовки (первый ряд)
            rows = [dict(zip(headers, row)) for row in reader]
        
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, indent=4)
        print(f"Конвертация из CSV в JSON завершена: {output_file}")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    subparsers = parser.add_subparsers(dest="cmd")

    # Подкоманда json2csv — конвертация из JSON в CSV
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Путь к файлу JSON")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Путь к файлу CSV")

    # Подкоманда csv2json — конвертация из CSV в JSON
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Путь к файлу CSV")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Путь к файлу JSON")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json2csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv2json(args.input, args.output)

if __name__ == "__main__":
    main()
```
![Картинка 1](./images/lab06/convert.png)# python_labs
![Картинка 2](./images/lab06/people_json.png)# python_labs
![Картинка 3](./images/lab06/people_csv.png)# python_labs

## Лабораторная работа 7

### Задание test_text.py
```
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("гоша,саша,васютка!", ["гоша", "саша", "васютка"]),
        (
            "email@example.com website.shh",
            ["email", "example", "com", "website", "shh"],
        ),
        ("!", []),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (
            ["я", "ненавижу", "python", "я", "ненавижу", "код"],
            {"я": 2, "ненавижу": 2, "python": 1, "код": 1},
        ),
        (["four", "five", "six"], {"four": 1, "five": 1, "six": 1}),
        (["xdxd", "xd", "xdxd", "xdxdxd", "xdxd"], {"xdxd": 3, "xd": 1, "xdxdxd": 1}),
    ],
)
def test_count_freq_and_top_n(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, n, expected",
    [
        ({"я": 2, "люблю": 2, "python": 1, "код": 1}, 2, [("люблю", 2), ("я", 2)]),
        ({"один": 1, "два": 1, "три": 1}, 2, [("два", 1), ("один", 1)]),
        ({"lala": 3, "la": 1, "lalala": 1}, 2, [("lala", 3), ("la", 1)]),
    ],
)
def test_top_n_tie_breaker(source, n, expected):
    assert top_n(source, n) == expected
```
![Картинка 1](./images/lab07/test_text.png)# python_labs

### Задание test_json_csv.py
```
import pytest
import json, csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv
from src.lab05.csv_json import csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    json_data = [
        {"name": "Vasia", "age": 54},
        {"name": "Bob", "age": 15},
    ]
    src.write_text(
        json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    empty_json_data = []
    src.write_text(json.dumps(empty_json_data), encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_invalid_json(tmp_path: Path):
    src = tmp_path / "invalid.json"
    dst = tmp_path / "out.csv"
    invalid_json_data = (
        '{"name": "Vasia", "age": 54'  
    )
    src.write_text(invalid_json_data, encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    csv_data = """name,age
Vasia,54
Bob,15"""

    src.write_text(csv_data, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        result_data = json.load(f)

    assert isinstance(result_data, list) and len(result_data) == 2
    assert set(result_data[0]) == {"name", "age"}


def test_file_not_exist(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```
![Картинка 2](./images/lab07/test_json_csv.png)# python_labs

### Задание black
![Картинка 3](./images/lab07/black.png)# python_labs


## Лабораторная работа 8

### Задание А
```
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Student:
    fio: str          
    birthdate: str    
    group: str        
    gpa: float        

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты рождения: {self.birthdate}")
        
        if not (0 <= self.gpa <= 10):
            raise ValueError(f"Средний балл должен быть от 0 до 10, но получен: {self.gpa}")

    def age(self) -> int:
        birth_year = int(self.birthdate[:4])
        current_year = datetime.today().year
        return current_year - birth_year

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(fio=data["fio"], birthdate=data["birthdate"], group=data["group"], gpa=data["gpa"])

    def __str__(self):
        # Для красоты
        return f"Student(fio={self.fio}, group={self.group}, gpa={self.gpa})"
```
## тест
```
from src.lab08.models import Student  

def test_age():
    student = Student("Майк Тайсон", "1966-06-30", "БИВТ-25-1", 5.0)
    assert student.age() == 59 

def test_to_dict():
    student = Student("Флойд Мэйвезер", "1977-02-24", "БИВТ-25-2", 4.8)
    student_dict = student.to_dict()
    assert student_dict == {
        'fio': 'Флойд Мэйвезер',
        'birthdate': '1977-02-24',
        'group': 'БИВТ-25-2',
        'gpa': 4.8
    }

def test_from_dict():
    student_dict = {
        'fio': 'Джордж Флойд',
        'birthdate': '1973-10-14',
        'group': 'БИВТ-25-3',
        'gpa': 3.9
    }
    student = Student.from_dict(student_dict)
    assert student.fio == "Джордж Флойд"
    assert student.gpa == 3.9
```
![Картинка 1](./images/lab08/test_models.png)# python_labs

### Задание B
```
import json
from typing import List
from .models import Student

def students_to_json(students: List[Student], path: str):
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Student.from_dict(item) for item in data]
```

## тест
```
import pytest
from src.lab08.serialize import students_to_json, students_from_json

def test_serialization():
    students = students_from_json('src/data/lab08/students_input.json')
    for student in students:
        print(f"{student.fio}, {student.birthdate}, {student.group}, GPA: {student.gpa}")
    students_to_json(students, 'src/data/lab08/students_output.json')
    print("Файл сохранён в src/data/lab08/students_output.json")
```
![Картинка 2](./images/lab08/output_test.png)# python_labs

## Лабораторная работа 9
### Задание A
```
import csv
from pathlib import Path
from ..lab08.models import Student


class Group:

    headers = ["fio", "birthdate", "group", "gpa"]
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            if not self.path.exists():
                with open(self.path, 'w', encoding='utf-8') as f:
                    f.write("fio,birthdate,group,gpa\n")

    
    def _read_all_dicts(self):
        if not self.path.exists():
            return []
        rows = []
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        
        return rows
    
    def _write_all_dicts(self, rows):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self):
        rows = self._read_all_dicts()
        students = []
        for row in rows:
            student = Student.from_dict(row)
            students.append(student)
        return students
    
    def add(self, student):
        rows = self._read_all_dicts()
        student_dict = student.to_dict()
        student_dict["gpa"] = str(student_dict["gpa"])
        rows.append(student_dict)
        self._write_all_dicts(rows)
    
    def find(self, substr):
        all_students = self.list()
        substr_lower = substr.strip().lower()
        found_students = []
        for student in all_students:
            if substr_lower in student.fio.lower():
                found_students.append(student)
        return found_students
    
    def remove(self, fio: str):
        rows = self._read_all_dicts()
        new_rows = [r for r in rows if r["fio"] != fio]
        removed = len(rows) - len(new_rows)
        if removed:
            self._write_all_dicts(new_rows)
        return removed
    
    def update(self, fio, **fields):
        rows = self._read_all_dicts()
        fio_lower = fio.strip().lower()
        for row in rows:
            if row["fio"].strip().lower() == fio_lower:
                row.update({k: str(v) for k, v in fields.items()})
                self._write_all_dicts(rows)
                return True
        return False
```

## тест
```
from src.lab09.group import Group
from src.lab08.models import Student


def main():
    path = "data/lab09/students.csv"
    group = Group(path)

    print("Изначальный список")
    for s in group.list():
        print("  ", s)

    print("Добавление студента")
    new_student = Student(
        fio="Тестовый Студент",
        birthdate="2007-05-11",
        group="БИВТ-25-4",
        gpa=4.7
    )
    group.add(new_student)
    print("Добавлен:", new_student)

    print("Проверка списка после добавления")
    for s in group.list():
        print("  ", s)

    print("Поиск студента по ФИО")
    found = group.find("Тест")
    for s in found:
        print("найден:", s)

    print("Обновление GPA")
    group.update("Тестовый Студент", gpa=5.0)
    print("GPA обновлён.")

    print("Список после обновления")
    for s in group.list():
        print("  ", s)

    print("Удаление")
    group.remove("Тестовый Студент")
    print("Удалён Тестовый Студент")

    print("Финальный список")
    for s in group.list():
        print("  ", s)

if __name__ == "__main__":
    main()
```
![Картинка 1](./images/lab09/lab09.png)# python_labs
![Картинка 2](./images/lab09/lab0901.png)# python_labs