'''
Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму. для Н=4 // 2 2.25 2.37 2.44
'''

n = int(input('Введи N '))
k = 1
list = []
for i in range(n):
    z = round((1+1/k)**k, 2)
    list.append(z)
    k+=1
print(list)
sum = 0
k = 0
i=0
while i < n:
    sum = sum + list[i]
    i = i+1
print('Сумма равна ', sum)

