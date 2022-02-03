import re  # только для удобства в 6-ом задании

"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
 элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
  явно, в программе.
"""
print('Задание 1')
task_1_list = [1, 1.2, 'string', True, [1, 2], (1, 2), {'a': 1, 'b': 3}, type('3')]

for element in task_1_list:
    print(f'{element} is {type(element)}')

"""
2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и
т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно
использовать функцию input().
"""
print('Задание 2')
task_2_list = input('Введите значения в список, разделяя их пробелом - ').split()
task_2_list[:-1:2], task_2_list[1::2] = task_2_list[1::2], task_2_list[:-1:2]

print(task_2_list)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
 весна, лето, осень). Напишите решения через list и dict.
"""

print('Задание 3')
task_3_input = int(input('Введите номер месяца (от 1 до 12)'))

if task_3_input == 12:
    task_3_input = 0  # Декабрь мешает ровно разделить на сезоны, отправим его в зиму
elif task_3_input < 12:
    task_3_input = int(task_3_input//3)

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}

print('Из списка мы получим, что это ', seasons_list[task_3_input])
print('Из словаря мы получим, что это ', seasons_dict[task_3_input])

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
"""
print('Задание 4')

task_4_input = input('Введите строку из нескольких слов разделенных пробелами ').split()
for word in task_4_input:
    print(word[:10])

"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

print('Задание 5')

my_list = [7, 5, 3, 3, 2]

print('Сейчас последовательность выглядит так:', str(my_list)[1:-1])
for input_round in range(3):  # отстанем от пользователя после трех запросов
    input_num = int(input('введите еще одно натуральное число - '))
    my_list.append(input_num)
    my_list.sort(reverse=True)
    print('Пользователь ввел число ', input_num, '. ', 'Результат: ', str(my_list)[1:-1], '.', sep='')

"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть
характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно, 
запросив все данные у пользователя. Пример готовой структуры:

[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, 
название. Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

#  Спросим про параметры которые хотим учитывать
param_input = re.split(',| ', input('Введите параметры товаров разделяя пробелом или запятой '))

# спросим про колличество товаров которые хотим занести в структуру
goods_num = int(input('Введите колличество товаров которые хотите записать '))

# генерим сруктуру, пока что не храня в кореже
product_list_full = [[i+1, {param: None for param in param_input}] for i in range(goods_num)]

# начинам опрашивать нашего пользователя:

for product in product_list_full:
    for param in product[1].keys():
        product[1][param] = input(f'Введите {param} у товара №{product[0]}')

print(product_list_full)

# теперь сохраняем с кортежами, и делаем анатилику:
product_list_full = [tuple(product_list) for product_list in product_list_full]

# Выводим наши данные
print(product_list_full)

# Для аналитики используем уже котовую структуру, просто чтобы не тратить время на ввод
product_list_full = [
                    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
                    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
                    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]


# предполагая что это не те данные которые только что собрали,(игнорируя param_input, соберем ключи в словаре):
# собираем так, как будето в товарах, могут быть разные ключи
list_of_params = []
for product in product_list_full:                               # Тут явно можно сделать лучше...
    for param in product[1].keys():
        list_of_params.append(param)
list_of_params = list(set(list_of_params))

# составляем конечный отчет:
Full_report = {}
for param in list_of_params:
    report_list = [product[1][param] for product in product_list_full if product[1][param]]
    report_list = list(set(report_list))
    Full_report.update({param: report_list})

# Выводим отчет
print(Full_report)
