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
