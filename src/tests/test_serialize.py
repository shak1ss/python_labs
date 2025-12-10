import pytest
from src.lab08.serialize import students_to_json, students_from_json

def test_serialization():
    students = students_from_json('src/data/lab08/students_input.json')
    for student in students:
        print(f"{student.fio}, {student.birthdate}, {student.group}, GPA: {student.gpa}")
    students_to_json(students, 'src/data/lab08/students_output.json')
    print("Файл сохранён в src/data/lab08/students_output.json")
