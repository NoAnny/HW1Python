# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Сколько всего журавликов сделали дети? "))
if s%6 == 0:
    print (f'Катя сделала {4*s//6} шт')
    print (f'Петя и Сережа сделали по {s//6} шт')
else:
    print("Проверьте правильность введенных данных. Число должно сответствовать условию задачи")
