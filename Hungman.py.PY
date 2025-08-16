import random


words = ["field", "robot", "table", "foots", "books"]
secret_word = random.choice(words)


guessed_letters = []
wrong_guess= 0
max_guess= 6


display_word = ["_" for _ in secret_word]


while wrong_guess < max_guess and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Wrong guesses left: {max_guess - wrong_guess}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")


if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game over! The word was:", secret_word)

           