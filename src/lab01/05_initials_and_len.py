FIO = input("Введите полное ФИО: ")
length = len(FIO.strip())
parts = FIO.split()
initials = "".join(word[0].upper() for word in parts) + "."
print (f"ФИО: {FIO}\n"
       f"Инициалы: {initials}\n"
       f"Длина (символов): {length}")