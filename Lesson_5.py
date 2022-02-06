from functools import reduce

'''
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных будет свидетельствовать пустая строка.
'''


def tik_1():
    with open("tik_1_file.txt", 'w', encoding='utf-8') as f:
        while True:
            data_str = input('Введите что нибудь, для остановки ввода оставьте пустою строку '
                            'и нажмите Enter ')
            if data_str == '':
                f.write(data_str)
                break
            else:
                f.write(data_str + '\n')


tik_1()

'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой 
строке.
'''


def tik_2():
    with open("tik_2_file.txt", 'r', encoding='utf-8') as f:
        strings_list = f.read()

        # заголовок мини-отчета
        report = {'№ строки': 'Кол-во слов'}

        # соберем отчет из номеров строк и колличества слов в них
        report_data = {i+1: len(val.split()) for i, val in enumerate(strings_list.split('\n'))}
        report.update(report_data)

        #  выведем мини-отчет
        for i, val in report.items():
            print("{:<12} {:<12}".format(i, val))

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
    with open("tik_3_file.txt", 'r', encoding='utf-8') as f:
        data = {line.split()[0]: float(line.split()[1]) for line in f}
    # все данные из файла мы уже взяли, можно его закрыть
    print('Работники с ЗП менее 20тыс - ', str([key for key, val in data.items() if val < 20000]))

tik_3()












