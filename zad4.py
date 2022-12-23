'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
'''

import random
n = int(input('Введи число '))

list1 = [random.randint(-n, n) for i in range(n)]
list2 = [random.randint(-0, n-1) for k in range(2)]

print(list1)
print(list2)
print(list1[list2[0]] * list1[list2[1]])








