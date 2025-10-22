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
