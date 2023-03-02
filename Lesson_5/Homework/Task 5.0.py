# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def deg(a, b):
    if b == 1:
        return a
    return (a * deg(a, b - 1))

print(deg(3, 5))

#====================

def deg(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / (deg(a, b + 1) * a)
    return deg(a, b - 1) * a

print(deg(2, 3))