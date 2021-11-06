{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "В первом варианте массив занимает 92 байта \n",
      "Во втором варианте массив занимает 452 байта \n",
      "В третьем варианте массив занимает 44 байта\n",
      "Вывод: чем больше массив, тем больше занимает памяти.\n"
     ]
    }
   ],
   "source": [
    "# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. \n",
    "# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.\n",
    "# По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:\n",
    "# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;\n",
    "# b. написать 3 варианта кода (один у вас уже есть); проанализировать 3 варианта и выбрать оптимальный;\n",
    "# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. \n",
    "# указать версию и разрядность вашей ОС и интерпретатора Python;\n",
    "# d. написать общий вывод: какой из трёх вариантов лучше и почему.\n",
    "# --------------------------------------------------------------------------------------------------------------------------\n",
    "\n",
    "import sys\n",
    "import random\n",
    "# 3.8.5 (default, Sep  4 2020, 00:03:40) [MSC v.1916 32 bit (Intel)] win32 \n",
    "\n",
    "# Задание для анализа 1: задача 3.3 (обмен максимального и мимимального элементов случайного массива)\n",
    "# ПЕРВЫЙ ВАРИАНТ: (0, 99) in range(10)\n",
    "def max_to_min1(A):\n",
    "    A = [random.randint(0, 99) for _ in range(10)]\n",
    "    maximum = A[0]\n",
    "    minimum = A[0]\n",
    "\n",
    "    for el in A:\n",
    "        if el > maximum:\n",
    "            maximum = el\n",
    "        elif el < minimum:\n",
    "            minimum = el\n",
    "\n",
    "    index_min = A.index(minimum)\n",
    "    index_max = A.index(maximum)\n",
    "    A[index_max], A[index_min] = A[index_min], A[index_max]\n",
    "    return A\n",
    "\n",
    "\n",
    "# ВТОРОЙ ВАРИАНТ: (0, 10) in range(99)\n",
    "def max_to_min_2(B):\n",
    "    B = [random.randint(0, 25) for _ in range(10)]\n",
    "    mn, mx = min(A), max(B)\n",
    "    ind_mn, ind_mx = B.index(mn), B.index(mx)\n",
    "    B[ind_mx], B[ind_mn] = B[ind_mn], B[ind_mx]\n",
    "    return B\n",
    "\n",
    "\n",
    "# ТРЕТИЙ ВАРИАНТ: (0, 99) in range(3)\n",
    "def max_to_min_3(C):\n",
    "    C = [random.randint(0, 99) for _ in range(3)]\n",
    "    mn, mx = min(C), max(C)\n",
    "    ind_mn, ind_mx = C.index(mn), C.index(mx)\n",
    "    C[ind_mx], C[ind_mn] = C[ind_mn], C[ind_mx]\n",
    "    return C\n",
    "\n",
    "\n",
    "A = [random.randint(0, 99) for _ in range(10)]\n",
    "B = [random.randint(0, 10) for _ in range(99)]\n",
    "C = [random.randint(0, 99) for _ in range(3)]\n",
    "\n",
    "print(f'В первом варианте массив занимает {sys.getsizeof(A)} байта','\\n'\n",
    "    f'Во втором варианте массив занимает {sys.getsizeof(B)} байта','\\n'\n",
    "    f'В третьем варианте массив занимает {sys.getsizeof(C)} байта')\n",
    "print('Вывод: чем больше массив, тем больше занимает памяти.')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
