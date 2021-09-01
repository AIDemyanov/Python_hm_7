# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        a = []
        for i in range(len(self.list)):
            a.append([])
            for j in range(len(self.list[0])):
                a[i].append((self.list[i][j] + other.list[i][j]))
        return '\n'.join(map(str, a))


list_1 = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1]]
list_2 = [[5, 6, 7, 8], [8, 7, 6, 5], [1, 4, 3, 2]]

matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)

print(matrix_1 + matrix_2)
