FIO = input("ФИО: ")
while '  ' in FIO:
    FIO = FIO.replace('  ', ' ')
splitwords = FIO.split()
FIO_2 = FIO.rstrip().lstrip()
fletters = []
str_fletters = ''
for splitwords in splitwords:
    fletters.append(splitwords[0])
for letter in fletters:
    str_fletters +=  letter
print(f"Инициалы: {str_fletters}")
print(f"Длина (символов): {len(FIO_2)}")
