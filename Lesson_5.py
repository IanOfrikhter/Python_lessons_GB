from functools import reduce
from random import randint
import re
import json


'''
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных будет свидетельствовать пустая строка.
'''

def tik_1():
    with open("lesson_5_files/tik_1_file.txt", 'w', encoding='utf-8') as f:
        while True:
            data_str = input('Введите что нибудь, для остановки ввода оставьте пустою строку '
                            'и нажмите Enter ')
            if data_str == '':
                f.write(data_str)
                break
            else:
                f.write(data_str + '\n')

print('Задание 1')
tik_1()

'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой 
строке.
'''


def tik_2():
    with open("lesson_5_files/tik_2_file.txt", 'r', encoding='utf-8') as f:
        strings_list = f.read()

        # заголовок мини-отчета
        report = {'№ строки': 'Кол-во слов'}

        # соберем отчет из номеров строк и колличества слов в них
        report_data = {i+1: len(val.split()) for i, val in enumerate(strings_list.split('\n'))}
        report.update(report_data)

        #  выведем мини-отчет
        for i, val in report.items():
            print("{:<12} {:<12}".format(i, val))

print('Задание 2')
tik_2()

'''
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов 
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
'''


def tik_3():
    with open("lesson_5_files/tik_3_file.txt", 'r', encoding='utf-8') as f:
        data = {line.split()[0]: float(line.split()[1]) for line in f}
    # все данные из файла мы уже взяли, можно его закрыть
    # Посчитаем среднюю ЗП, разбив на строки для читаемости
    total_salary = reduce(lambda x, y: x+y, [val for val in data.values()])
    print('Средняя ЗП -', total_salary / len(data.keys()))

    # Выведем работников с ЗП менее 20 тыс.
    print('Работники с ЗП менее 20тыс - ', end = '')
    print(*[key for key, val in data.items() if val < 20000], sep=', ')


print('Задание 3')
tik_3()


'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны 
заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''


def tik_4():
    with open('lesson_5_files/tik_4_english.txt', 'r', encoding='utf-8') as f:
        # нам все равно обратно записывать тем же блоком, разбивать не будем
        text = f.read()

    # можно конечно воспользоваться API переводчика, но пока оставим так
    text = text.replace('One', 'Один')
    text = text.replace('Two', 'Два')
    text = text.replace('Three', 'Три')
    text = text.replace('Four', 'Четыре')

    # старый фаил не трогаем, создаем новый
    with open('lesson_5_files/tik_4_ru.txt', 'w', encoding='utf-8') as f:
        f.write(text)


print('Задание 4')
tik_4()
'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна 
подсчитывать сумму чисел в файле и выводить её на экран.
'''


def tik_5():
    # создаем строку со случайными числами
    string = [str(randint(1, 100)) for i in range(randint(10, 30))]
    string = ' '.join(string)

    # запишем в фаил
    with open('lesson_5_files/tik_5.txt', 'w', encoding='utf-8') as f:
        f.write(string)

    # прочитаем
    with open('lesson_5_files/tik_5.txt', 'r', encoding='utf-8') as f:
        num_list = f.read().split()

    num_list = [int(i) for i in num_list]
    print(sum(num_list))


print('Задание 5')
tik_5()

'''
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие 
лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, 
чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''


def tik_6():
    with open('lesson_5_files/tik_6.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    # многое зависит от того, как записали фаил
    strings = data.split('\n')  # разные строки это точно разные предметы

    # раз нам нужна просто сумма, удалим все личшее
    strings = [dis.split(' ') for dis in strings]

    # для читаемости завернем в for
    keys = []; num_list = []
    for dis_list in strings:
        keys.append(dis_list[0])
        numbers = [float(re.sub("[^0-9]", "", num)) for num in dis_list[1:] if not re.sub("[^0-9]", "", num) == '']
        num_list.append(numbers)

    # соберем результат из списка ключей и часов
    result_dict = {key: sum(hours) for key, hours in zip(keys, num_list)}
    print(result_dict)


print('Задание 6')
tik_6()

'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о 
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

def tik_7():
    with open('lesson_5_files/tik_7.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    firm_lists = [firm_list.split() for firm_list in data.split('\n')]

    # соберем имена и прибыль
    company_names = data.split()[::4]
    company_profit = [float(rev) - float(pay) for rev, pay in zip(data.split()[2::4], data.split()[3::4])]

    # Составим словари
    firm_data_dict = {firm_name: firm_profit for firm_name, firm_profit in zip(company_names, company_profit)}
    average_dict = {"average_profit": sum(company_profit) / len(firm_lists)}

    # Итоговый список из двух словарей
    to_json_result_list = [firm_data_dict, average_dict]

    with open("lesson_5_files/tik_7_json.json", "w") as f:
        json.dump(to_json_result_list, f)

print('Задание 7')
tik_7()



















