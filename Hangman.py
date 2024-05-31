import random
import time

# Function to choose a random word from a list of words
def choose_random_word(words):
    random.seed(time.time())  # Seed random number generator
    return random.choice(words)

# Function to display the current state of the guessed word
def display_word_state(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

# Function to check if the user has guessed the word
def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def main():
    words = [
        "programming", "computer", "science", "keyboard", "mouse",
        "monitor", "processor", "memory", "storage", "network",
        "software", "hardware", "database", "algorithm", "function",
        "variable", "constant", "syntax", "debugging", "compiler",
        "developer", "engineer", "technology", "application", "system",
        "interface", "design", "architecture", "encryption", "security",
        "internet", "protocol", "server", "client", "framework",
        "library", "module", "object", "class", "method",
        "attribute", "parameter", "argument", "loop", "condition",
        "array", "pointer", "reference", "exception", "inheritance"
    ]

    word_to_guess = choose_random_word(words)
    guessed_letters = set()
    max_attempts = 15
    attempts_left = max_attempts

    print("Welcome to the Word Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the word.")

    while attempts_left > 0 and not is_word_guessed(word_to_guess, guessed_letters):
        print("\nWord: ", end='')
        display_word_state(word_to_guess, guessed_letters)
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

        input_guess = input("Enter a letter or the full word: ").lower()

        if len(input_guess) == 1:
            # Handle single letter guess
            guess = input_guess

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.add(guess)
                print("Good guess!")
            else:
                guessed_letters.add(guess)
                print("Wrong guess!")
                attempts_left -= 1
        else:
            # Handle full word guess
            if input_guess == word_to_guess:
                guessed_letters.update(word_to_guess)  # This ensures that all letters will be displayed
                break
            else:
                print("Wrong guess!")
                attempts_left -= 1

    if is_word_guessed(word_to_guess, guessed_letters):
        print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
    else:
        print(f"\nSorry, you've run out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    main()
