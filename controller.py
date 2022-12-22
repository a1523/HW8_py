from student import see_rating
from teacher import add_student
from teacher import put_rating
from student_database import load_db
from student_database import save_db



def controller():
    load_db() # выгрузка данных из файла db_students.json
    match input('Укажите себя: 1 - учитель; 2 - ученик: '):
        case '1': # Блок кода для учителя
            flag = 1
            while flag == 1:
                print('Что хотите сделать?')
                act = input('1 - записать ученика; 2 - выставить оценку; 0 - выйти из программы.\nВвод: ')
                if act == '1':
                    add_student()
                elif act == '2':
                    put_rating()
                elif act == '0':
                    flag = 0
            else:
                save_db() # сохранение данных в файле db_students.json
        case '2': # Блок кода для ученика     
            flag = 1
            while flag == 1:
                last_name = input('Введите фамилию ученика или 0 для выхода из программы\nВвод: ')
                if last_name == '0':
                    flag = 0
                else:
                    see_rating(last_name)
