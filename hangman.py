import random

class HangmanGame:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(words).lower()
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def display_word(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guesses:
                displayed_word += letter + ' '
            else:
                displayed_word += '_ '
        return displayed_word.strip()

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guesses:
            return "You've already guessed that letter."
        elif letter in self.word:
            self.guesses.append(letter)
            if self.check_win():
                return "You win! The word was: " + self.word
            else:
                return "Correct guess! Word: " + self.display_word()
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                return "You lose! The word was: " + self.word
            else:
                return "Incorrect guess! Attempts left: " + str(self.attempts_left)

    def check_win(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

def main():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon']
    hangman = HangmanGame(words)
    
    print("Welcome to Hangman!")
    print("Guess the word:", hangman.display_word())

    while True:
        guess = input("Enter a letter: ")
        result = hangman.guess_letter(guess)
        print(result)

        if hangman.attempts_left == 0 or hangman.check_win():
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == 'yes':
                hangman = HangmanGame(words)
                print("Guess the word:", hangman.display_word())
            else:
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    main()
