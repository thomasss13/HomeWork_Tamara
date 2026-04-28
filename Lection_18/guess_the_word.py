import random


class GuessTheWord:
    
    MAX_TRIES = 10
    
    def __init__(self, words, descriptions):

        self.word_dict = {}
        for i in range(len(words)):
            self.word_dict[words[i]] = descriptions[i]
        
        self.secret_word = random.choice(list(self.word_dict.keys()))
        self.description = self.word_dict[self.secret_word]
        
        self.field = ['*'] * len(self.secret_word)
        
        self.tries = self.MAX_TRIES
        self.guessed_letters = []
        self.is_game_over = False
        self.is_win = False
    
    def show_description(self):
        print(self.description)
    
    def show_field(self):
        print(" ".join(self.field))
    
    def guess_letter(self, letter):
        if len(letter) != 1:
            print("Нужно ввести одну букву!")
            return None
        
        if letter in self.guessed_letters:
            print("Вы уже называли эту букву!")
            return None

        self.guessed_letters.append(letter)
        
        matched = False
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == letter:
                self.field[i] = letter
                matched = True

        if matched:
            print(" ".join(self.field))
            self._check_win()
            return True
        else:
            self.tries -= 1
            print("Нет такой буквы.")
            if self.tries > 0:
                print(f"У вас осталось {self.tries} попыток!")
            else:
                self.is_game_over = True
                self.is_win = False
                print(f"Загаданное слово было: {self.secret_word}")
            return False
    
    def _check_win(self):
        if '*' not in self.field:
            self.is_game_over = True
            self.is_win = True
    
    def get_remaining_tries(self):
        return self.tries
    
    def is_finished(self):
        return self.is_game_over
    
    def is_winner(self):
        return self.is_win
    
    def get_secret_word(self):
        return self.secret_word
    
    def run(self):
        while not self.is_finished():
            letter = input("\nВведите букву: ")
            self.guess_letter(letter)

        print("\n===== ИГРА ОКОНЧЕНА =====")
        if self.is_winner():
            print("Поздравляем! Вы победили!")
        else:
            print("Не расстраивайтесь, попробуйте ещё раз!")


words = ["оператор", "конструкция", "объект"]
descriptions = [
    "Это слово обозначает наименьшую автономную часть языка программирования",
    "Это совокупность объявлений данных и функций, объединенных в единую структуру",
    "Это сущность в программировании, обладающая собственным состоянием и поведением"
]

game = GuessTheWord(words, descriptions)

game.show_description()
game.show_field()
game.run()
