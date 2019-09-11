"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

my_school = [{'school_class': '1а', 'scores': [3,4,4,5,2,5,5]},
            {'school_class': '1б', 'scores': [5,4,3,5,2,3,4,5,2,5,4,4]}, 
            {'school_class': '1в', 'scores': [5,5,5,3,2,4,5]}, 
            {'school_class': '2a', 'scores': [5,4,5,4,5,4,2,2,3]}, 
            {'school_class': '2б', 'scores': [4,4,4,4,4,3,3,5,5]}, 
            {'school_class': '2в', 'scores': [4,3,4,5,4,5,4,5]},
            {'school_class': '3a', 'scores': [5,4,5,4,5,4,5,3,2,5,4,2,2,3]}, 
            {'school_class': '3б', 'scores': [4,5,3,4,4,4,5,2,3,4,4,3,3,5,5]}, 
            {'school_class': '3в', 'scores': [5,5,5,2,2,4,3,4,5,4,5,4,5]}]

def main(class_name, class_scores):
    class_average = 0
    for score in class_scores:
        class_average += score
    return class_average / len(class_scores)

    
if __name__ == "__main__":
    all_school_score = 0
    for group in my_school:
        class_name = group['school_class']
        class_scores = group['scores']

        res = main(class_name, class_scores)
        all_school_score +=res  #Подсчет суммы средних баллов всех классов
        all_school_average = all_school_score / len(my_school) #Средний балл по всей школе
        print(f'{class_name} имеет средний балл: {res}')
    print(f'Средний балл по школе: {all_school_average}')


