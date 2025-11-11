import csv

def write_csv(rows, path, header=None):
    with open(path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)

sorted_freq = [('word', 1), ('hello', 2), ('world', 3)]  # Пример данных
write_csv(sorted_freq, "src/data/lab04/report.csv", header=["word", "count"])
