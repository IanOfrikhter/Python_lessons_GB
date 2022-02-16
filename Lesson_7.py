import itertools
'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix 
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с 
первым элементом первой строки второй матрицы и т.д.
'''
class Matrix:
    def __init__(self, data):
        # Проверка что все элементы итерируемы
        try:
            for row in data:
                try:
                    _ = (i for i in row)
                except TypeError as te:
                    print(row, 'is not iterable')
                    raise TypeError
        except TypeError:
            print(data, 'is not iterable')
            raise TypeError

        # Проверка того, что все строки одинаковой длины
        colomns = len(data[0])
        for row in data:
            if not len(row) == colomns:
                print(f'{row} have {len(row)} elements, {colomns} was expected')
                raise TypeError

        # Проверка того, что все элементы могут быть float
        try:
            [float(i) for i in itertools.chain(*data)]
        except TypeError:
            print(f'{i} is not digit')
            raise TypeError

        self.matrix_data = data

    def __str__(self):
        format_string = '{:^7}' * len(self.matrix_data[0])

        formated_str = ''
        for i in self.matrix_data:
            formated_str += format_string.format(*i) + '\n'

        return formated_str

    def __add__(self, matrix):
        # Хочу проверить является ли объект классом Matrix, правильно ли?
        if not isinstance(matrix, Matrix):
            raise Exception


        # складываем элементы матриц
        result_matrix = []
        for row_1, row_2 in zip(self.matrix_data, matrix.matrix_data):
            result_martix_row = [el_1 + el_2 for el_1, el_2 in zip(row_1, row_2)]
            result_matrix.append(result_martix_row)

        result_matrix = Matrix(result_matrix)  # результатом должен быть объект класса Matrix

        return result_matrix


# Создаем матрицу 1
martix_1 = Matrix([[1, 2, 6], [1, 3, 10]])
print(martix_1)

# Создаем матрицу 2
martix_2 = Matrix([[8, 11, 1], [10, 2, 7]])
print(martix_2)

# Складываем матрицы
print(martix_1 + martix_2)


'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта 
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих 
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, 
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма 
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные 
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''


class Dress:










