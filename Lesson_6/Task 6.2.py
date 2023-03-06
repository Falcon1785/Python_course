# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# 1 2 3 2 3
# 2

# list_1 = [1, 2, 3, 2, 3]
# count = 0
# for i in range(len(list_1)):
#     for j in range(i + 1, len(list_1)):
#         if list_1[i] == list_1[j]:
#             count += 1

# print(count)

# =====================

# list_1 = [1, 2, 3, 2, 3]
# print(len([i for i in range(len(list_1)) for j in range(i + 1, len(list_1)) if list_1[i] == list_1[j]]))

# =================================

# list_1 = list(map(int, input("Введите массив:").split()))
# count = 0
# for i in range(len(list_1)):
#     for j in range(i + 1, len(list_1)):
#         if list_1[i] == list_1[j]:
#             count += 1

# print(count)

# ============================

# mas = [1, 2, 3, 2, 3, 4, 4, 4]
mas = [int(input("элементы: ")) for i in range(int(input("кол-во элементов: ")))]
print(mas)
print(sum([mas.count(i) // 2 for i in set(mas)]))