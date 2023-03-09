# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

#=====С циклом while

num = int((input("Enter a ticket number: \n")))
S1 = 0
S2 = 0
num1 = num // 1000
num2 = num % 1000
while num1 > 0 and num2 > 0:
    x1 = num1 % 10
    S1 = S1 + x1
    x2 = num2 % 10
    S2 = S2 + x2
    num1 = num1 // 10
    num2 = num2 // 10
if S1 == S2:
    print('Lucky ticket')
else:
    print('Not a lucky ticket')

#======= Со строками

num = (input("Enter a ticket number: \n"))
S1 = int(num[0]) + int(num[1]) + int(num[2])
S2 = int(num[3]) + int(num[4]) + int(num[5])
print(S1, S2)
if S1 == S2:
    print('Lucky ticket')
else:
    print('Not a lucky ticket')
