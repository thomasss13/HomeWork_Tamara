# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_length = 33

def encrypt_line(line, shift):
    result = ""
    for simb in line:
        if simb in alphabet_lower:
            index = alphabet_lower.index(simb)
            new_index = (index - shift) % alphabet_length
            result += alphabet_lower[new_index]
        elif simb in alphabet_upper:
            index = alphabet_upper.index(simb)
            new_index = (index - shift) % alphabet_length
            result += alphabet_upper[new_index]
        else:
            result += simb
    return result


with open("message.txt", "r", encoding="utf-8") as f_in:

    with open("encrypted.txt", "w", encoding="utf-8") as f_out:
        shift = 1
            
        for line in f_in:

            encrypted_line = encrypt_line(line, shift)
                
            f_out.write(encrypted_line)
            print(encrypted_line, end='')
                
            shift += 1
                
print("Шифрование завершено. Результат в файле encrypted.txt")