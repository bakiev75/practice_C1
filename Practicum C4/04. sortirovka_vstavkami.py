"""
Готовы сами написать сортировку? Никаких сомнений — готовы! Что должен сделать алгоритм?

В начале итерации устанавливается ведущий элемент. На первой итерации — самый первый
элемент и по умолчанию он считается уже отсортированным.
Сохраняем ведущий элемент в дополнительную переменную (красный квадрат в анимации).
Далее происходит поиск места, куда должен встать ведущий элемент в уже отсортированной
(левой) части массива. Можно, например, использовать цикл while с условием достижения
границы и/или успешным нахождением элемента. Пока условие цикла выполняется, происходит
сдвиг каждого элемента вправо.
По завершении цикла сохранённое значение переменной помещается на освободившееся место.
Алгоритм завершается.
Алгоритм сортировки вставками хоть и является также квадратичным по времени (в среднем),
но имеет меньшие множители (в силу уменьшенного количества тяжёлых операций). И к тому же
очень хорошо работает на почти отсортированных массивах.
"""

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print(array)
