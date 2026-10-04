import random
def play_game():
    #List of words to guess
    words = ["python","vscode","github","coding","computer "]

    # Randomly select a secret word
    secret_word = random.choice(words)

    # Store guessed letters
    guessed_Letters =[]

    # Number of attempts allowed
    attempts = 6

    print("==================================")
    print("Welcome to the Word Guessing Game!")
    print("==================================")
    print(f"The word has {len(secret_word)} letters.")
    print(f"YOu have {attempts} attempts.\n")

    while attempts > 0: 
        #  Display the current word progress (e.g., p _ t h o n)
        display_word =""
        for letter in secret_word:
            if letter in guessed_Letters:
                display_word += letter + ""
            else:
                display_word += "_ "

        print("Current word:", display_word)

        # Win condition check 
        if "_" not in display_word:
            print("\nCongratulations! You've guessed the word:", secret_word)
            break

        # Take user input 
        guess = input("Guess a Letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only.\n")
            continue

        if guess in guessed_Letters:
            print("You already guessed that letter. Try another one!\n")
            continue

        guessed_Letters.append(guess)

        # Check if the guess is correct
        if guess in secret_word:
            print("Correct!\n")
        else:
            attempts -= 1
            print(f"Wrong! YOu have {attempts} attempts left.\n")

        if attempts == 0:
            print("=================================")
            print(f"Game over! The correct word was '{secret_word}'.")
            print("=================================")

if __name__ == "__main__":
    play_game()
