"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

ask_answ = {"Привет": "Привет",
            "Как дела": "Хорошо!", 
            "Что делаешь?": "Программирую", 
            'Название нашей страны': 'Россия', 
            'Столица России': 'Москва'}


def ask_user_dict(): 
    while True:
        try:
            ask_user = input('Вопрос: ')
            if ask_user in ask_answ.keys():
                print(f'Пользователь: {ask_user}\nПрограмма: {ask_answ[ask_user]}')
        except KeyboardInterrupt:
            print('Пока!')
            break
        

    
if __name__ == "__main__":
    ask_user_dict()
