print()
print('Welcome to the word guessing game!')
print()
print('Your hint is: _ _ _ _ _ _ _ _')
print()
secret_word = 'dinosaur'
guess = input('What is your guess? ')

while guess.lower() != 'dinosaur':
    if guess == '':
        print('Sorry, you need to input a guess.')
    elif guess.lower() != secret_word:
        if len(guess) != len(secret_word):
            print()
            print('Sorry, the guess must have the same number of letters as the secret word.')
            print()
        else:
            hint = ''
            i = 0
            while i < len(secret_word):
                if guess[i] == secret_word[i]:
                    hint += guess[i].upper()  # Uppercase letter indicates correct letter at the correct position
                elif guess[i] in secret_word:
                    hint += guess[i].lower()  # Lowercase letter indicates correct letter at the wrong position
                else:
                    hint += ' _ '  # Underscore indicates incorrect letter
                i += 1
            print()
            print('Your hint is: ', hint)
            print()
    
    # Prompt the user for the next guess
    guess = input('What is your guess? ')

print()
print("Congratulations! You guessed it!")
print()