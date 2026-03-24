unit = int(input('Выберите единицу измерения: '))
mass = int(input('Введите массу: '))

match unit:
    case 1:
        print(mass, 'кг')
    case 2:
        print(mass * 1e-6, 'кг')
    case 3:
        print(mass * 1e-3, 'кг')
    case 4:
        print(mass * 1e3, 'кг')
    case 5:
        print(mass * 1e2, 'кг')
    case _:
        print('Некорректный ввод')