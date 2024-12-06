# 1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()# Вывод значений параметров
print('================')

# Вызываем функцию print_params с разным количеством аргументов и без аргументов.
print_params('день', False, 1)
print_params("ночь", 9)
print_params(a='non', b= 3, c='три')
print_params(a='сто', b='два')
print_params(b='два', c='три')
print_params(c=1)
print('================')

#Проверьте, работают ли вызовы
print_params(b = 25)
print_params(c=[1, 2, 3])
print('================')

# 2.Распаковка параметров:
#Создайте список values_list с тремя элементами разных типов.
values_list = [1.1,'str', False]
#Создайте словарь values_dict с тремя ключами,и значениями разных типов.
values_dict = {'a':'dictionary','b': True ,'c': 8 }
# Передаем values_list и values_dict в функцию print_params,
print_params(*values_list)
print_params(**values_dict)
print('================')

#Передайте values_list и values_dict в функцию print_params
values_list_1 = [1]
values_dict_1 = {'b': 'строка','c': True}
print_params(*values_list_1,**values_dict_1)
print('================')

# Исходный код:
values_list_2  = ['Задача',11.1]
print_params(*values_list_2, 77)
print('================')




















