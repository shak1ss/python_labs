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
