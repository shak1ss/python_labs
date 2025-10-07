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