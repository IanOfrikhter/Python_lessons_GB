'''
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных будет свидетельствовать пустая строка.
'''


def tik_1():
    with open("tik_1_file.txt", 'w') as f:
        while True:
            data_str = input('Введите что нибудь, для остановки ввода оставьте пустою строку '
                            'и нажмите Enter ')
            if data_str == '':
                f.write(data_str)
                break
            else:
                f.write(data_str + '\n')


'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой 
строке.
'''

# Имя фаила
with open("tik_1_file.txt", 'r') as f:
    strings_list = f.read().split(sep='\n')   # разбивка построчно

    report_data = {str_num: word_count for str_num, data in  strings_list}

    print('Колличество строк - ', len(strings_list))

    print()






