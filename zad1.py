'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
'''

a = float(input('введите число '))
sum = int()
while a != int(a):
    a *= 10
while a != 0:
    x = a % 10
    sum+=x
    a = a // 10
print('сумма равна', sum)


