"""
Следующее решение «в лоб» — каждый раз искать минимальный элемент и ставить его в начало.
"""


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(len(array)):                         # проходим по всему массиву

        idx_min = i                                 # сохраняем индекс предположительно минимального элемента
        for j in range(i+1, len(array)):
                if array[j] < array[idx_min]:
                        idx_min = j
        if i != idx_min:                            # если индекс не совпадает с минимальным, меняем
                array[i], array[idx_min] = array[idx_min], array[i]

print(array)