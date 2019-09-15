"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

from statistics import mean

my_school = [{'school_class': '1а', 'scores': [3,4,4,5,2,5,5]},
            {'school_class': '1б', 'scores': [5,4,3,5,2,3,4,5,2,5,4,4]}, 
            {'school_class': '1в', 'scores': [5,5,5,3,2,4,5]}, 
            {'school_class': '2a', 'scores': [5,4,5,4,5,4,2,2,3]}, 
            {'school_class': '2б', 'scores': [4,4,4,4,4,3,3,5,5]}, 
            {'school_class': '2в', 'scores': [4,3,4,5,4,5,4,5]},
            {'school_class': '3a', 'scores': [5,4,5,4,5,4,5,3,2,5,4,2,2,3]}, 
            {'school_class': '3б', 'scores': [4,5,3,4,4,4,5,2,3,4,4,3,3,5,5]}, 
            {'school_class': '3в', 'scores': [5,5,5,2,2,4,3,4,5,4,5,4,5]}]

def main():
    all_school_score = []
    for group in my_school:
        class_name = group['school_class']
        class_scores = group['scores']
        res = mean(class_scores)
        all_school_score.append(res)#Складываем в список средние баллы всех классов
        print('{} имеет средний балл: {:.2f}'.format(class_name,res))
    all_school_average = mean(all_school_score) #Средний балл по всей школе
    print('Средний балл по школе: {:.2f}'.format(all_school_average))
        

if __name__ == "__main__":
    main()