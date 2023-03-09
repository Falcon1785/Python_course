# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# =============Вариант 1

list_1 = [1, 2, 3, 4, 5]
k = int(input())
result = []
for i in list_1:
    result.append(list_1[i - k])
print(*result)

# =============Вариант 2

list = [1, 2, 3, 4, 5]
k = int(input())
for i in range(k - 1):
    list.insert(0, list[len(list) - 1])
    list.pop()
print(*list)

# =============Вариант с семинара 1

list_nums = [1, 2, 3, 4, 5]
k = 3
result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
print(result)

# =============Вариант с семинара 2

list = [1, 2, 3, 4, 5]
k = int(input())
for i in range(k - 1):
    list.insert(0, list.pop(-1))
print(*list)