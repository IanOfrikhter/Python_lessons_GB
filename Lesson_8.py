'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Date:

    def __init__ (self, date):
        self.date = date

    def __str__ (self):
        return self.date

    # return True, if date if viable
    @staticmethod
    def check_date (date, date_type='NL'):
        date_list = Date.date_to_digit(date, date_type = date_type)

        return date_list


    @classmethod
    def date_to_digit (cls, date, date_type='NL'):
        date_list = date.split('-')

        # different date expressions
        if date_type == 'NL':
            date_list = int(date_list[0]), int(date_list[1]), int(date_list[2])
        else:
            print('Unknown date format')
            date_list = False

        return date_list


date_1 = Date('10-02-1995')

print(date_1)

print(date_1.date)

print(Date.date_to_digit('23-04-2010'))


'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, 
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не 
завершиться с ошибкой.
'''


class ZeroDiv(ZeroDivisionError):

    pass



'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить 
работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на 
экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем 
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При 
этом работа скрипта не должна завершаться.
'''


class NotNumber(ValueError):
    pass


print('Задание 3')
result_list = []
while True:
    try:
        value = input('Введите число, или stop: ')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        else:
            result_list.append(int(value))

    except NotNumber as err:
        print(f'{err} не является числом')

print(result_list)

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, 
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу 
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для 
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''

class Storage:
    location_list = []  # список адресов всех складов

    def __init__(self, area, location):
        if location in self.location_list:
            print('Склад по этому адресу уже есть')
            raise ValueError
        else:
            self.location_list.append(location)
            self.max = area
            self.av_area = area  # доступная площадь склада умноженная на коэф, для создания проходов
            self.storage = {}
            self.location = location

    def __str__(self):
        return f'Склад на {self.location}, {self.max} м2'

    # метод __add__ не трогаем, он может пригодится для объединения складов или пристроев,
    # для добавления техники создаем add
    def add(self, equipt, count = 1):
        if not type(count) == int:
            print('Count have to be int > 0')
            raise Exception

        if count < 0:
            print('Count have to be int > 0')
            raise Exception

        equipt_storage_data = {'mass': equipt.mass,
                               'area': equipt.box_area * equipt.mov_coff,
                               'add_data': equipt.add_data}

        if self.av_area - equipt.box_area * equipt.mov_coff < 0:
            print('На складе не хватает места')
            raise Exception

        if equipt.model in self.storage.keys():
            self.storage[equipt.model]['num'] += count
        else:
            self.storage.update({equipt.model: {'num': count,
                                                'mass': equipt.mass,
                                                'area': equipt.box_area * equipt.mov_coff,
                                                'add_data': equipt.add_data}})

    def take_item(self, model, count = 1): #достаточно наименования
        if not type(count) == int:
            print('Count have to be int > 0')
            raise Exception

        if count < 0:
            print('Count have to be int > 0')
            raise Exception

        if model in self.storage.keys():
            if self.storage[model]['num'] >= count:
                self.storage[model]['num'] -= count # не удаляем всю запись, чтобы помнить что попадало на склад
            else:
                print('Недостаточно товаров на складе')
        else:
            print('Таких товаров на складе нет, и не было')

    def show_storage_data(self):
        return self.storage


class OfficeEq:
    def __init__(self, model, mass, box_area):
        try:
            float(mass)
        except:
            print(f'масса - {mass} для модели {model} указана не корректно')
            raise ValueError

        try:
            float(box_area)
        except:
            print(f'занимаемая площадь {box_area} для модели {model} указана не корректно')
            raise ValueError

        self.model = model
        self.mass = mass            # масса коробки
        self.box_area = box_area    # занимаемая площадь коробки (c учетом многоярусности)

    pass


class Printer(OfficeEq):
    def __init__(self, model, mass, box_area, add_data = [], mov_coff=0.8):
        super().__init__(model, mass, box_area)

        self.mov_coff = mov_coff # запас по площади (0.5 - 1), создание удобного для перемещения пространста
        self.add_data = add_data  # контейнер для любой другой информации
    pass


class Scanner(OfficeEq):
    def __init__(self, model, mass, box_area, add_data = [], mov_coff=0.7):
        super().__init__(model, mass, box_area)
        self.mov_coff = mov_coff   # запас по площади (0.5 - 1), создание удобного для перемещения пространста
        self.add_data = add_data   # контейнер для любой другой информации
    pass


# создадим склад - 1
Storage_1 = Storage(25, 'Крупская 15')
print(Storage_1)

# потытаемся создать склад 2 на том же адресе, что не получится
try:
    Storage_2 = Storage(50, 'Крупская 15')
except ValueError:
    pass
# print(Storage_2) # <--- попытка обратиться к несуществующему складу

# Создадим склад 2 на соседнем адресе
Storage_2 = Storage(50, 'Крупская 16')

# Проверим список созданных складов:
print(Storage_2.location_list)

# создадим немного оргтехники
prt_HP = Printer('107wr', 7.1, 0.15)
scn_Espada = Scanner('EC717', 2.2, 0.1)

# выведем состав склада 1:
print(Storage_1.show_storage_data())

# добавим на склад один несколько 2 сканера и принтер и выведем состав склада 1::
Storage_1.add(prt_HP)
Storage_1.add(scn_Espada, 2)
print(Storage_1.show_storage_data())

# удалим со склада один товар (несуществующий):
Storage_1.take_item('1099er')

# заберем 2  товара, когда есть только 1
Storage_1.take_item('107wr', 2)

# удалим 1  товар
Storage_1.take_item('107wr')

# выведем состав склада 1:
print(Storage_1.show_storage_data())



'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса 
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного 
результата.
'''


class ComNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComNum(1, -2)
z_2 = ComNum(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)








