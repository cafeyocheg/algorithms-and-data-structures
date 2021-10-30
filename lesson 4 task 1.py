# **1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.**
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# ОЦЕНИТЬ АЛГОРИТМ ЗАДАЧИ 3
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import timeit
import cProfile

# ПЕРВЫЙ ВАРИАНТ: с помощью условия
def max_to_min_1(a):
    a = [random.randint(0, 99) for _ in range(10)]
    print(a)
    maximum = a[0]
    minimum = a[0]

    for el in a:
        if el > maximum:
            maximum = el
        elif el < minimum:
            minimum = el

    index_min = a.index(minimum)
    index_max = a.index(maximum)

    a[index_max], a[index_min] = a[index_min], a[index_max]
    print(a)
    return a

# ВТОРОЙ ВАРИАНТ: при помощи функций max() и min()
def max_to_min_2(A):
    A = [random.randint(0, 99) for _ in range(10)]
    print(A)
    mn, mx = min(A), max(A)
    ind_mn = A.index(mn)
    ind_mx = A.index(mx)
    A[ind_mx], A[ind_mn] = A[ind_mn], A[ind_mx]
    print(A)
    return A

# АНАЛИЗ АЛГОРИТМОВ ПО ВРЕМЕНИ
test_executions = 1
test_value = 1000

time1 = timeit.timeit(f'max_to_min_1({test_value})',
                      setup='from __main__ import max_to_min_1',
                      number=test_executions)

time2 = timeit.timeit(f'max_to_min_2({test_value})',
                      setup='from __main__ import max_to_min_2',
                      number=test_executions)

print(f'Программа первая выполняется за {round(time1 * 1000, 5)} миллисекунд.\n'
      f'Программа вторая выполняется за {round(time2 * 1000, 5)} миллисекунд.\n'
      f'Вторая быстрее первой в {round(time1 / time2, 2)} раза')

