from time import sleep

'''
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на
ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и 
завершать скрипт.
'''
print('----------------------Задание 3')


class TrafficLight:

    def __init__(self):
            self.__color = False

    def running(self, green_time = 10):
        prev_color = None
        if not self.__color:
            self.__color == 'red'
            sleep(7)
        elif self.__color == 'red':
            self.__color = 'yellow'
            sleep(2)
        elif self.__color == 'yellow':
            self.__color = 'green'
            sleep(green_time)



# Переключим 10 раз
TL = TrafficLight()
print(TL._TrafficLight__color)
TL.running()

print(TL._TrafficLight__color)

TL.running()
print(TL._TrafficLight__color)

'''
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число 
см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''
print('----------------------Задание 3')


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def __str__(self):
        return f'Длина дороги - {self._length}м, ширина дороги - {self._width}м'

    def road_mass(self, density, thickness):
        if not 1.4 <= density <= 1.7:
            print('Плотность асфальта обычно в диапазоне 1.4-1.7 т/м3,', f'у вас - {density}')
        if not 0.05 <= thickness <= 0.4:
            print(f'Принятая толщина асфальта составила {thickness}м')
        mass = self._length * self._width * density * thickness

        return mass

# Создаем асфальтовое покрытие 1600м в длину и 8м в ширину
R_1 = Road(1600, 8)

# считаем массу при плотности асфальта 1.5т/м3 и толщине покрытия 0.08м
print(f'Масса асфальтового покрытия - {R_1.road_mass(1.5, 0.08)} тонн')



'''
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров.
'''
print('----------------------Задание 3')


class Worker:
    def __init__(self, first_name, surname, position, wage, bonus):
        self.first_name = first_name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, first_name, surname, position, wage, bonus):
        super().__init__(first_name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.first_name + ' ' + self.surname

    def get_total_income(self):
        return self._income['Wage'] + self._income['bonus']
        # return f'{sum(self._income.values())}'


# Создадим экзепляр работника
Po = Position('Вася', 'Баширов', 'Тренер', 50000, 1000000)

# ФИО
print(Po.get_full_name())

# полный доход
print(Po.get_total_income())


'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите 
методы и покажите результат.
'''
print('----------------------Задание 4')


class Car:
    max_speed = 90  # speed считаю базовой скоростью, присвоенной создании экземпляра

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    # для метода go определим атрибут прироста скорости, если его нет, то speed = max_speed
    def go(self, acceleration=False):
        if not acceleration:
            self.speed = self.max_speed
        else:
            self.speed += acceleration
        print(f'{self.name} accelerated')

    # Зануляем скорость
    def stop(self):
        self.speed = 0
        print(f'{self.name} have stopped')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}km/h')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed is {self.speed}km/h, it is higher than allowed')
        else:
            print(f'{self.name} speed is {self.speed}km/h')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed is {self.speed}km/h, it is higher than allowed')
        else:
            print(f'{self.name} speed is {self.speed}km/h')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


# создадим town car
town_car = TownCar(0, 'red', 'Toyota')

# скорость при создании:
town_car.show_speed()

# добавим скорость и проверим скорость (с предупреждением)
town_car.go(100)
town_car.show_speed()

# Проверим скорость через доступ к атрибуту
print(f'Проверим скорость через доступ к атрибуту - {town_car.speed}')

# Поворот налево
town_car.turn('left')

# остановка и повторная проверка скорости
town_car.stop()
town_car.show_speed()


'''
5. Реализовать класс Stationery (канцелярская принадлежность). определить в нём атрибут title (название) и метод draw 
(отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Рисование {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисование ручкой {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисование карандашем {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисование маркером {self.title}'


print('----------------------Задание 5')
# Создаем экземпляры
pen = Pen('Parker')
pencil = Pencil('HB')
handle = Handle('Promarker')


print(pen.draw())
print(pencil.draw())
print(handle.draw())
