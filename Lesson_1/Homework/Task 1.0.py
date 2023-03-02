# Задача 1: Найдите сумму цифр трехзначного числа.

num = int(input('Введите число: \n'))
sum = 0

while num > 0:
    x = num % 10
    sum += x
    num //= 10

print(sum)