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
