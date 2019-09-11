"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string1, string2):
    if type(string1) == str and type(string2) == str:
        if string1 == string2:
            return '1'
        elif len(string1) > len(string2) and string2 != 'learn':
            return '2'
        elif string1 != string2 and string2 == 'learn':
            return '3'
        else:
            return '4'
    else:
        return '0'

    
    
if __name__ == "__main__":

    test_1 = main(123, 'string') #Передана НЕстрока (0)
    test_2 = main('learn', 'learn') #Одинаковые строки (1)
    test_3 = main('looong_string', 'short') #Первая строка длиннее второй (2)
    test_4 = main('testtest', 'learn') #Вторая строка 'learn' (3)
    test_5 = main('spider', 'superman_the_best') #Вторая строка длиннее первой (4)

    print("test_1 OK") if test_1 == '0' else print("test_1 Fail")
    print("test_2 OK") if test_2 == '1' else print("test_2 Fail")
    print("test_3 OK") if test_3 == '2' else print("test_3 Fail")
    print("test_4 OK") if test_4 == '3' else print("test_4 Fail")
    print("test_5 OK") if test_5 == '4' else print("test_5 Fail")