from bubble_sort import bubble 
from insertion_sort import insertion
from reverse_bubble_sort import reverse_bubble 
from quick_sort import quick_sort

print('Введите элемнты списка через пробел. Только числа или только буквы.')
elements = input()
elements = elements.split(' ')
for i in range(len(elements)):
    elements[i] = int(elements[i])
print('Каким методом вы бы хотели отсортировать список? Введите номер. \n 1: Пузырьком \n 2: Утюжком \n 3: Вставками \n 4: Быстрым')
chose = input()

if chose == '1':
    print('Пузырьком')
    elements = bubble(elements)
elif chose == '2':
    print('Утюжком')
    elements = reverse_bubble(elements)
elif chose == '3':
    print('Вставками')
    elements = insertion(elements)
elif chose == '4':
    print('Быстрая')
    elements = quick_sort(elements)
else:
    print('Я так не умею, перечитайте условие')

print(elements)
    