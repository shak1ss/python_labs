from linked_list import SinglyLinkedList

lst = SinglyLinkedList()
print("=== Тест SinglyLinkedList ===")
print(f"   Список: {lst}")
print(f"   Длина: {len(lst)}")
lst.append(10)
lst.append(20)
lst.append(30)
print(f"   После append: {lst}")
print(f"   Длина: {len(lst)}")
lst.prepend(5)
print(f"   После prepend(5): {lst}")
lst.insert(2, 15)
print(f"   После insert(2, 15): {lst}")
print(f"   Элементы: ", end="")
for x in lst:
    print(x, end=" ")
print()
lst.insert(0, 1)
lst.insert(len(lst), 100)
print(f"   После вставки в начало и в конец: {lst}")
try:
    lst.insert(-5, 999)
except IndexError as e:
    print(f"   Ошибка при insert(-5): {e}")
try:
    lst.insert(100, 100)
except IndexError as e:
    print(f"   Ошибка при insert(100): {e}")
