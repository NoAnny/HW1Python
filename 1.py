# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзначное число:'))
sum = 0
if 99 < n <= 999:
    sum = n%10 + n//10%10 + n//100
else:
    print('Проверьте правильность введенных данных')
print(sum)