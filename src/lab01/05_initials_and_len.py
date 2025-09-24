FIO = input("ФИО: ")
while '  ' in FIO:
    FIO = FIO.replace('  ', ' ')
splitwords = FIO.split()
FIO_2 = FIO.strip()
fletters = []
str_fletters = ''
for words in splitwords:
    fletters.append(words[0])
for letter in fletters:
    str_fletters +=  letter
print(f"Инициалы: {str_fletters}")
print(f"Длина (символов): {len(FIO_2)}")
