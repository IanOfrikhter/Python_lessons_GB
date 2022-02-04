import sys
from decimal import Decimal
from functools import reduce
from itertools import count, cycle

'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в 
нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо 
запускать скрипт с параметрами.
'''

from scr import TIK_1
print('Задание 1 - ', TIK_1(10, 5, 100))

# для запуска через терминал scr_2.py 10 5 100

# не понял как передать параметры используя exec() и можно ли вообще, использую
#  exec(open('scr_2.py').read())


'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''


def tik_2(irrerable_2):
    return [val for ind, val in enumerate(irrerable_2[1:]) if val > irrerable_2[ind]]


assert [12, 44, 4, 10, 78, 123] == tik_2([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])


"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор."""


print('Задание 3 - ', [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])


'''
4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел, 
соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания 
обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''


def tik_3(itter):
    return [i for i in itter if itter.count(i) == 1]


assert [23, 1, 3, 10, 4, 11] == tik_3([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])


'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные 
числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''


def tik_4():
    gen_list = [i for i in range(100, 1001) if i % 2 == 0]
    result = reduce(lambda x, y: x * y, gen_list)
    return result


print('Задание 4 - ','{:.4e}'.format(Decimal(tik_4())))

'''
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и 
cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его 
завершения. #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. 
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
'''

print('Задание 6, часть 1-------------------------------------------------------------------------------')
for i in count(3):
    if i <= 10:
        print(i)
    else:
        break

print('Задание 6, часть 2-------------------------------------------------------------------------------')
c = 0
for i in cycle([3, 6, 9, 12]):
    if c < 6:
        c += 1
        print(i)
    else:
        break


'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции 
должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение 
факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
'''


def factorial(n):
    for itr in range(1, n+1):
        fact = reduce(lambda x, y: x * y, range(1, itr+1), 1)
        yield fact

print('Задание 7 - ')
for i in factorial(5):
    print(i)