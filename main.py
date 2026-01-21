import os

word = input("Make a string for hangman: ")
guessed = False

guessed_word = []

os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------HANGMAN-----------------")
print("Enter a letter to try to guess a word")
print("Every instance of the letter will appear in the blanks if it's right")
print("If you hit 6 incorrect guesses, you lose")
print("Good luck!")
print() 

for letter in word:
    guessed_word.append("_")
    print("_", end=" ")

incorrect_guesses = 0
guesses = []

print()

while not guessed:
    guess = input("Make a guess for a letter in the word: ")

    if len(guess) != 1:
        print("Please enter one single letter", end="\n")
        continue
    
    if guess in guesses:
        print("You already guessed that letter!", end="\n")
        continue

    guesses.append(guess)

    correct = False
    for i in range(len(word)):
        if word[i].upper() == guess.upper():
            guessed_word[i] = guess
            correct = True
    
    if not correct and incorrect_guesses < 5:
        print(f"Sorry, there is no {guess.lower()} in the word")
        incorrect_guesses += 1
    elif not correct and incorrect_guesses >= 5:
        print(f"Sorry, you could not get the word! The word was: {word}")
        break

    print(f"Incorrect guesses: {incorrect_guesses}")
    print("\n")
    
    if "_" not in guessed_word:
        guessed = True
        break

    for letter in guessed_word:
        print(letter, end=" ")
    
    print()

if guessed:
    print(f"You got it! The word was: {word}")

print()