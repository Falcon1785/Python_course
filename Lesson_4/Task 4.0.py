# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string = input().split()

for i in range(len(string)):
    count = 1
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            string[j] += "_" + str(count)
            count += 1

print(string)

#==================================

string = input().split()

D = {}.fromkeys(string, 0)
# print(D)

for i in string:
    print(f"{i}_{D[i]}" if D[i] else i, end=" ")
    D[i] += 1

#==============================

chars = input().split()
dict_chars = {}.fromkeys(chars, 0)

for i in chars:
    print(f"{i}_{dict_chars[i]}" if dict_chars[i] else i, end=" ")
    dict_chars[i] += 1


#====================================

sp = input().split()
result = {}
for i in sp:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1