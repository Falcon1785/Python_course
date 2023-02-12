# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

print('Enter the number of watermelons:')
w_mel = int(input())
max_weight = min_weight = weight_1 = int(input('first:'))
for i in range(w_mel - 1):
    weight = int(input())
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight
print(min_weight, max_weight)
