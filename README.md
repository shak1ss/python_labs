# effective-broccoli

## Лабораторная работа 1

### Задание 1
```python
name = (input("Имя: "))
age = int(input("Возраст: "))
print (f"Привет, {name}! Через год тебе будет {age+1}.")
```
![Картинка 1](./images/lab01/01.png)

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
FIO = input("Введите полное ФИО: ")
length = len(FIO.strip())
parts = FIO.split()
initials = "".join(word[0].upper() for word in parts) + "."
print (f"ФИО: {FIO}\n"
       f"Инициалы: {initials}\n"
       f"Длина (символов): {length}")
```
![Картинка 5](./images/lab01/05.png)# python_labs