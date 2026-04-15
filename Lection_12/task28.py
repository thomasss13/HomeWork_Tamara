import random

def create_field(n):

    field = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    return field


def count_ships(field):

    count = sum([cell for row in field for cell in row if cell == 1])
    return count


if __name__ == "__main__":
    n = 7
    
    game_field = create_field(n)
    
    print(f"=== ИГРОВОЕ ПОЛЕ {n}x{n} ===\n")
    for row in game_field:
        print(row)
    
    total_ships = count_ships(game_field)
    
    print(f"\n🚢 Всего кораблей на поле: {total_ships}")