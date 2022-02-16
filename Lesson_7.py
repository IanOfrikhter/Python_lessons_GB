import itertools
from abc import ABC, abstractmethod
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
            print('Arg have to be Matrix')
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


class Clothes(ABC):
    # раз параметр все равно один, передадим его тут
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def material_consumption(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def material_consumption (self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def material_consumption(self):
        return self.param * 2 + 0.3


print('Задание_2')
# создаем пальто
Coat_1 = Coat(54)

# создаем костюм
Suit_1 = Suit(1.75)

# Считаем потребление
print(Coat_1.material_consumption)
print(Suit_1.material_consumption)

'''
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его 
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть 
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение 
(__mul__()),деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, 
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше 
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих 
двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: 
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: 
*****\n*****\n*****.
'''


class Cell:
    def __init__(self, cell):

        self.cell = int(cell)
        self.simbol = '*'

    def __str__(self):
        return str(f'Cell_num = {self.cell}')

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell - other.cell < 0:
            print('Cells num could not be < 0')
            raise Exception

        return Cell((self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, count):
        form_str = ''
        for i in range(self.cell // count):
            form_str += count * '*' + '\n'

        if self.cell % count != 0:
            form_str += self.cell % count * '*'

        return form_str


# создадим две клетки
Cell_1 = Cell(25)
Cell_2 = Cell(6)

# произведем все операции и вызовем метод make_order
print('Cell_1 + Cell_2 = ', Cell_1 + Cell_2)
print('Cell_1 - Cell_2 = ', Cell_1 - Cell_2)
print('Cell_1 * Cell_2 = ', Cell_1 * Cell_2)
print('Cell_1 / Cell_2 = ', Cell_1 / Cell_2)
print(Cell_1.make_order(6))









