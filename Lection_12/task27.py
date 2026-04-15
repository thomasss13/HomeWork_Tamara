import random

generate_field = lambda size: [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

game_field = generate_field(5)

shot_field = [['?' for _ in range(5)] for _ in range(5)]

hits = 0
total_ships = sum(row.count(1) for row in game_field)
attempts = 0

print("=== МОРСКОЙ БОЙ ===")
print(f"Всего кораблей на поле: {total_ships}")
print("Координаты: строка (0-4), столбец (0-4)")
print()


while hits < total_ships:

    print("Поле выстрелов:")
    print("   0 1 2 3 4")
    for i in range(5):
        row_str = f"{i}  "
        for j in range(5):
            row_str += shot_field[i][j] + " "
        print(row_str)
    print()
    
    try:
        i = int(input("Введите номер строки (0-4): "))
        j = int(input("Введите номер столбца (0-4): "))
        
        if i < 0 or i > 4 or j < 0 or j > 4:
            print("Координаты вне поля! Попробуйте снова.\n")
            continue
        
        if shot_field[i][j] != '?':
            print("Вы уже стреляли в эту клетку! Попробуйте снова.\n")
            continue
        
        attempts += 1
        
        if game_field[i][j] == 1:
            shot_field[i][j] = 'X'
            hits += 1
            print(f"✅ ПОПАДАНИЕ! Корабль подбит! ({i}, {j})")
        else:
            shot_field[i][j] = '•'
            print(f"ПРОМАХ! Пустая клетка. ({i}, {j})")
        
        print(f"Попаданий: {hits} из {total_ships} | Попыток: {attempts}\n")
        
    except ValueError:
        print("Ошибка: введите число от 0 до 4!\n")

# Победа
print("=" * 30)
print("ПОБЕДА! Все корабли уничтожены!")
print(f"Всего попыток: {attempts}")
print("=" * 30)

print("Исходное поле (для проверки):")
for row in game_field:
    print(row)