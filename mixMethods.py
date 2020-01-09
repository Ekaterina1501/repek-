import random
import numpy as np
from solver import *

# генерируем начальную матрицу, удовлетворяющую условиями игры судоку
def getStartMatrix():
    table = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 3, 4, 5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1, 2, 3, 4], [8, 9, 1, 2, 3, 4, 5, 6, 7],
             [3, 4, 5, 6, 7, 8, 9, 1, 2], [6, 7, 8, 9, 1, 2, 3, 4, 5], [9, 1, 2, 3, 4, 5, 6, 7, 8]]
    return table

# далее описаны методы перетасовки изначальной матрицы для генерирования уникальной игры

# метод 1: транспонирование матрицы
def transposing(table):
    table = np.array(table)
    table = table.transpose()
    return table.tolist()


# метод 2: обмен двух строк в пределах одного района
def swapTwoLines(table):
    n = 3
    area = random.randrange(0, n)
    line1 = random.randrange(0, n)
    # получение случайного района и случайной строки
    N1 = area * n + line1  # номер 1 строки для обмена
    line2 = random.randrange(0, n, 1)
    while (line1 == line2):
        line2 = random.randrange(0, n, 1)
    N2 = area * n + line2  # номер 2 строки для обмена
    table[N1], table[N2] = table[N2], table[N1]
    return table


# метод 3: обмен двух столбцов в пределах одного района
def swapTwoColumn(table):
    table = transposing(table)
    table = swapTwoLines(table)
    table = transposing(table)
    return table

# метод 4: обмен двух районов по горизонтали
def swapTwoHorizontalBlock(table):
    n = 3
    area1 = random.randrange(0, n)
    area2 = random.randrange(0, n)
    while (area1 == area2):
        area2 = random.randrange(0, n)
    for i in range(0, n):
        N1, N2 = area1 * n + i, area2 * n + i
        table[N1], table[N2] = table[N2], table[N1]
    return table


# метод 5: обмен двух районов по вертикали
def swapTwoVerticalBlock(table):
    table = transposing(table)
    table = swapTwoHorizontalBlock(table)
    table = transposing(table)
    return table

# запускаем несколько раз вышеописанные методы в случайном порядке
def mix(table, numberOfiteration = 10):
    func = [transposing, swapTwoLines, swapTwoColumn, swapTwoHorizontalBlock, swapTwoVerticalBlock]
    for i in range(1, numberOfiteration):
        id = random.randrange(0, len(func))
        current = func[id]
        return current(table)

# удаление элементов из ячеек
def deleteElements(table, iterator = 0, n = 3, difficult = 81): # difficult - колличество чисел в судоку
    flook = [[0 for j in range(n * n)] for i in range(n * n)]
    while iterator < n ** 4:
        # выбираем случайную ячейку
        i, j = random.randrange(0, n * n, 1), random.randrange(0, n * n, 1)
        # если её не смотрели
        if flook[i][j] == 0:
            iterator += 1
            flook[i][j] = 1  # Посмотрим

            # сохраним элемент на случай если без него нет решения или их слишком много
            temp = table[i][j]
            table[i][j] = 0
            # усложняем, если убрали элемент
            difficult -= 1

            # cкопируем в отдельный список
            table_solution = []
            for copy_i in range(0, n * n):
                table_solution.append(table[copy_i][:])

            # cчитаем количество решений
            i_solution = 0
            for solution in solve_sudoku((n, n), table_solution):
                i_solution += 1

            # eсли решение не одинственное, то нужно вернуть все обратно
            if i_solution != 1:
                table[i][j] = temp
                # облегчаем
                difficult += 1

    # заменяем на пустоту
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                table[i][j] = ""
    return table, difficult