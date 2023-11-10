from bubble_sort import bubble 
from insertion_sort import insertion
from reverse_bubble_sort import reverse_bubble 

print('Введите элемнты списка через пробел. Только числа или только буквы.')
elements = input()
elements = elements.split(' ')
print('Каким методом вы бы хотели отсортировать список? Введите номер. \n 1: Пузырьком \n 2: Утюжком \n 3: Вставками' )
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
else:
    print('Я так не умею, перечитайте условие')

print(elements)
    