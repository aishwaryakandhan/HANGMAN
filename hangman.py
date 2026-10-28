import random
words = ["apple", "tiger", "house", "plant", "water"]
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)


wrong_guesses = 0
max_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect guesses.")


while wrong_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_guesses)

    letter = input("Guess a letter: ").lower()

    if letter in secret_word:
        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed_word[i] = letter

    else:
        wrong_guesses += 1
        print("Wrong guess!")


if "_" not in guessed_word:
    print("\nCongratulations! YOU WIN!")
    print("The word was:", secret_word)

else:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)