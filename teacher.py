from student_database import set_student, set_rating

def add_student():
    """Получение данных ученика от учителя и их передача для записи"""
    metric = input('Введите данные (фамилия, имя, класс через пробел): ').split(' ')
    set_student(metric)

def put_rating():
    """Получение данных об оценке от учителя и их запись"""
    last_name = input('Введите фамилию ученика: ')
    lesson = input('Введите название предмета: ')
    rating = input('Введите оценку или оценки через пробел').split(' ')
    set_rating(last_name, lesson, rating)