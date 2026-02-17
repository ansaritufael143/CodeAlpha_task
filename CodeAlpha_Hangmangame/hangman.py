import random

words = ["python", "laptop", "keyboard", "internet", "gaming"]

secret_word = random.choice(words)

display_word = []
for letter in secret_word:
    display_word.append("_")

incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.\n")

while incorrect_guesses < max_attempts and "_" in display_word:
    
    print("Word:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed this letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Correct guess!\n")
        
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_attempts - incorrect_guesses, "\n")

if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("❌ Game Over! The correct word was:", secret_word)
