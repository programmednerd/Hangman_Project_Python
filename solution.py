import random

# Word list and hangman stages
word_list = ["aardvark", "baboon", "camel"]
stages = [
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      -
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / 
      -
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      -
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      -
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      -
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      -
    """,
    """
      ------
      |    |
      |    
      |    
      |    
      -
    """
]


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
attempts = len(stages) - 1 
guessed_letters = []

print("Welcome to Hangman!")

# Game loop
while "_" in display and attempts > 0:
    print(f"\n{' '.join(display)}")
    print(stages[attempts])
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts remaining: {attempts}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Right!")
        for index in range(word_length):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        print("Wrong!")
        attempts -= 1

# End of game results
if "_" not in display:
    print("\nYou win! The word was:", chosen_word)
else:
    print("\nGame over!")
    print(stages[0])  # Show the full hangman
    print("The word was:", chosen_word)
