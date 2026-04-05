#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

def vocal():

    vowels = {
        "а": 0, "о": 0, "и": 0, "е": 0, "ы": 0,
        "ё": 0, "ю": 0, "я": 0, "э": 0, "у": 0
    }
    
    with open("dump.txt", "rt", encoding="utf-8") as f:
        for line in f:
            for simbol in line:
                simbol_lower = simbol.lower()
                if simbol_lower in vowels:
                    vowels[simbol_lower] += 1
    
    # Вывод результатов
    print(f"Количество букв а - {vowels['а']}")
    print(f"Количество букв о - {vowels['о']}")
    print(f"Количество букв и - {vowels['и']}")
    print(f"Количество букв е - {vowels['е']}")
    print(f"Количество букв у - {vowels['у']}")
    print(f"Количество букв э - {vowels['э']}")
    print(f"Количество букв ю - {vowels['ю']}")
    print(f"Количество букв я - {vowels['я']}")
    print(f"Количество букв ы - {vowels['ы']}")
    print(f"Количество букв ё - {vowels['ё']}")
    
    total = sum(vowels.values())
    print(f"\nВсего гласных букв: {total}")

vocal()