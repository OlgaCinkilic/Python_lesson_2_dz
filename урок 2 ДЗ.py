"""
1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

a = ["Hello", 65, 35.45, "LaLaLa", 0.84, -4.8]
print(type(a))


"""
2. Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().

"""

    
my_list = input("Введите элементы списка: ").split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)


"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict.
"""
#list
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
        print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
        print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
        print(seasons_list[3])
else:
        print("Такого месяца не существует")

#dict

seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
else:
        print("Такого месяца не существует")


"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
 Если слово длинное, выводить только первые 10 букв в слове.
"""
my_text = input("введите предложение ")
my_word = []
number = 1
for element in range(my_text.count(' ') + 1):
    my_word = my_text.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1

"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
 который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. 
 Если в рейтинге существуют элементы с одинаковыми значениями, 
 то новый элемент с тем же значением должен разместиться после них.
 
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг,  - {my_list}")
digit = int(input("Введите число "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el] < digit:
            my_list.insert(el, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))

