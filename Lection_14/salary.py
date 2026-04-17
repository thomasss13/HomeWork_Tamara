import json
import numpy as np
import matplotlib.pyplot as plt
import os

applicants_file_path = "applicants.json"

vec_Weight = np.array([1000, 2000])
bias = 500
salary = []


def data_applicants():

    with open(applicants_file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        return data


applicants = data_applicants()

def save_json():

    with open(applicants_file_path, 'w', encoding = 'utf-8') as file:
        json.dump(applicants, file, indent = 4, ensure_ascii = False)


def show_menu():

    print('\n===== МЕНЮ =====')
    print("""
    1 - Создать карточку;
    2 - Показать все;
    3 - Вывести прогнозируемую зарплату;
    4 - Фильтрация по заработной плате (от 5000);
    5 - Вывести график зарплат;
    6 - Сохранить на диск (в файл);
    7 - Редактировать карточку;
    8 - Удалить карточку;
    0 - Выход
        """)

def check(applicant):
  
    if applicant['age'] < 18: 
        print('\n===== ОШИБКА =====')
        print('Кандидату должно быть не менее 18 лет!\n') 
        return False

    if applicant['age'] - applicant['experience'] < 18:
        print('\n===== ОШИБКА =====')
        print('Заявленный опыт работы не соответствует действительности!\n')
        return False
    
    if applicant['grade'] not in [1, 2, 3]:
        print('\n===== ОШИБКА =====')
        print('Выберите уровень образования из перечисленных!\n')
        return False
    
    return True


def calculation():

    global salary

    if not applicants:
        print('\n===== ОШИБКА =====')
        print('Список кандидатов пуст!\n')
        salary = []
        return []
    
    ExpGrade = []
    
    for applicant in applicants:
        row = [applicant['experience'], applicant['grade']]
        ExpGrade.append(row)
    
    matrix_ExpGrade = np.array(ExpGrade)

    salary = (matrix_ExpGrade @ vec_Weight) + bias
    
    return salary


def create():

    try:
        inpName = input('\nВведите имя: ')
        inpAge = int(input('Введите возраст: '))
        inpExperience = int(input('Введите опыт работы (в годах): '))
        inpGrade = int(input('Введите уровень образования (1 — школа, 2 — колледж, 3 — университет): '))

        applicant = {
            "name": inpName,
            "age": inpAge,
            "experience": inpExperience,
            "grade": inpGrade
        }

        if not check(applicant): return

        print(f"\n===== КАНДИДАТ {applicant['name']} ДОБАВЛЕН =====\n")
        applicants.append(applicant)

        save_json()
        calculation()
        

    except ValueError:
        print("===== ОШИБКА =====")
        print("Введите числовые значения для возраста, опыта и образования!\n")


def show_all():

    if not applicants:
        print('\n===== ОШИБКА =====')
        print('Список кандидатов пуст!\n')
        return
    
    print('===== СПИСОК КАНДИДАТОВ НА РАБОТУ =====:\n')
        
    for applicant in applicants:
        print(f"Имя: {applicant['name']}")
        print(f"Возраст: {applicant['age']}")
        print(f"Опыт работы: {applicant['experience']}")
        print(f"Уровень образования: {applicant['grade']}\n")


def forecast():

    if len(salary) == 0:
        calculation()
    
    print('===== ПРОГНОЗ РАЗМЕРА ЗАРПЛАТЫ =====\n')

    for i, applicant in enumerate(applicants):
        name = applicant['name']
        forecast_salary = salary[i]
        
        print(f"Имя: {name}")
        print(f"Зарплата: {forecast_salary:,.0f}\n")


def find_by_salary():

    if len(salary) == 0:
        calculation()
    
    high_salary = []
    
    print(f"===== ЗАРПЛАТА ВЫШЕ 5000 =====\n")
    
    found = False
    
    for i, applicant in enumerate(applicants):
        name = applicant['name']
        current_salary = salary[i]
        
        if current_salary > 5000:
            high_salary.append({'name': name, 'salary': current_salary})
            print(f"Имя: {name}")
            print(f"Зарплата: {current_salary:,.0f}\n")
            found = True
    
    if not found:
        print("===== НЕ НАЙДЕНО =====")


def save():
    
    with open("applicants.txt", "w", encoding='utf-8') as file:

        for applicant in applicants:
            file.write(f"Имя: {applicant['name']}\n")
            file.write(f"Возраст: {applicant['age']}\n")
            file.write(f"Опыт работы: {applicant['experience']}\n")
            file.write(f"Уровень образования: {applicant['grade']}\n")
            file.write("\n")

    save_json()
             
    print('\n===== ДАННЫЕ СОХРАНЕНЫ =====\n')


def graph():

    if len(salary) == 0:
        calculation()

    name = []
    forecast_salary = []
    for i, applicant in enumerate(applicants):
        name.append(applicant['name'])
        forecast_salary.append(salary[i])
 
    plt.bar(name, forecast_salary)

    plt.xlabel('Имя')
    plt.ylabel('Зарплата')
    plt.title('Распределение зарплат')
    plt.grid(axis='y', alpha=0.3)

    plt.show()


def delete():

    if not applicants:
        print('\n===== ОШИБКА =====')
        print('Список кандидатов пуст!\n')
        return

    print('===== ВСЕ КАНДИДАТЫ =====\n')
    for i, applicant in enumerate(applicants):
        print(f"Имя: {applicant['name']}")
        print(f"Возраст: {applicant['age']}")
        print(f"Опыт работы: {applicant['experience']}")
        print(f"Уровень образования: {applicant['grade']}\n")
    
    try:
        choice = int(input(f"Введите номер карточки для удаления 1-{len(applicants)}: "))

        if 0 <= choice - 1 < len(applicants):
            deleted_name = applicants[choice - 1]['name']
            confirm = input(f"Подтвердите удаление {deleted_name} (y/n): ")

            if confirm == 'y':
                applicants.pop(choice - 1)
                save_json()
                calculation()
                print("\n===== КАРТОЧКА УДАЛЕНА =====\n")
            elif confirm == 'n':
                print("\n===== УДАЛЕНИЕ ОТМЕНЕНО =====\n")
            else:
                print("\n===== ОШИБКА =====")
                print("Неверный ввод! \n")        

        else:
            print("\n===== ОШИБКА =====")
            print("Неверный номер! \n")

    except ValueError:
        print("\n===== ОШИБКА =====")
        print("Введите число! \n")


def edit():

    if not applicants:
        print('\n===== ОШИБКА =====')
        print('Список кандидатов пуст!\n')
        return

    print('===== ВСЕ КАНДИДАТЫ =====\n')
    for i, applicant in enumerate(applicants):
        print(f"Имя: {applicant['name']}")
        print(f"Возраст: {applicant['age']}")
        print(f"Опыт работы: {applicant['experience']}")
        print(f"Уровень образования: {applicant['grade']}\n")
    
    try:
        choice = int(input(f"Введите номер карточки для редактирования 1-{len(applicants)}: "))

        if 0 <= choice - 1 < len(applicants):
            applicant = applicants[choice - 1].copy()
            print(f"\n{applicant}")

            edit_field = int(input(f"""
    Имя - 1,
    Возраст - 2,
    Опыт работы - 3,
    Уровень образования - 4,
    Отмена - 0\n                
    Выберите поле редактирования: """))
            
            match edit_field:
                case 1:
                    applicant['name'] = input('Введите новое имя: ')
                case 2:
                    applicant['age'] = int(input('Введите новый возраст: '))
                case 3:
                    applicant['experience'] = int(input('Введите новый опыт (в годах): '))
                case 4:
                    applicant['grade'] = int(input('Введите новый уровень образования (1 — школа, 2 — колледж, 3 — университет): '))
                case 0:
                    print('\n===== РЕДАКТИРОВАНИЕ ОТМЕНЕНО =====\n')
                case _:
                    print('\n===== ОШИБКА =====')
                    print('Введите число от 0 до 4!\n')

            if not check(applicant): return

            applicants[choice - 1] = applicant

            print('\n===== РЕДАКТИРОВАНИЕ ЗАВЕРШЕНО =====\n')

            save_json()
            calculation()
    
    except ValueError:
        print('\n===== ОШИБКА =====')
        print('Введите число!\n')


def processing(choise):

    match choise:
        case 1:
            # Создать новую карточку
            create()
        case 2:
            # Показать все
            show_all()
        case 3:
            # Вывести прогнозируемую зарплату
            forecast()
        case 4:
            # Фильтрация по заработной плате (от 5000)
            find_by_salary()
        case 5:
            # Вывести график зарплат
            graph()
        case 6:
            # Сохранить на диск
            save()
        case 7:
            # Редактирование карточки
            edit()
        case 8:
            # Удаление карточки
            delete()
        case 0:
            print('\n===== ВЫХОД =====\n')
            return True
        case _:
            print("\n===== ОШИБКА =====")
            print("Неверный выбор операции!\n")
    return False


def main():

    while True:
        show_menu()

        try:
            choice = int(input("Выберите пункт меню: "))

            if processing(choice):
                break

        except ValueError:
            print("\n===== ОШИБКА =====")
            print("Введите число от 0 до 6!\n")


if not os.path.exists(applicants_file_path):
    print('\n===== ОШИБКА =====')
    print(f"Файл {applicants_file_path} не найден!\n")

    file_create = input('Хотите создать файл? (y/n): ')

    match file_create:
        case 'y':
            file = open(applicants_file_path, "a+", encoding = "utf-8")
            json.dump([], file, indent = 4, ensure_ascii = False)
            file.close()

        case 'n':
            exit()

main()

