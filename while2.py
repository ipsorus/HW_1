"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

ask_answ = {"Привет": "Привет",
            "Как дела": "Хорошо!", 
            "Что делаешь?": "Программирую", 
            'Название нашей страны': 'Россия', 
            'Столица России': 'Москва'}


def ask_user_dict():
    flag = True  
    while flag:
        ask_user = input('Вопрос: ')
        if ask_user in ask_answ.keys():
            print(f'Пользователь: {ask_user}\nПрограмма: {ask_answ[ask_user]}')
        #print(f'Программа: {ask_answ[ask_user]}')
        else:
            flag = False
            print('Ответа нет')
        

    
if __name__ == "__main__":
    ask_user_dict()
