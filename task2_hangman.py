import random

words = ["python", "developer", "internship", "programming", "scraper"]

secret_word = random.choice(words)

attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
while attempts > 0:
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

if attempts == 0:
    print("\nGame Over! The word was:", secret_word)