import tkinter as tk
from tkinter import Frame, Entry, Label, Button
import random

def main():
    # Create the Tk root object.
    root = tk.Tk()
    root.title("Adivinanzas de Palabras")  # Set the title

    # Initialize game variables
    word = select_random_word()
    guesses = []

    # Create the main frame
    frm_main = Frame(root)
    frm_main.pack()

    # Entry box for user guess
    enter_guess = Entry(frm_main)
    enter_guess.pack(padx=10, pady=10)

    # Use Enter key to submit guess
    enter_guess.bind('<Return>', lambda event: check_guess(root, enter_guess, word, guesses))

    # Button to submit guess
    guess_button = Button(frm_main, text='Adivines', command=lambda: check_guess(root, enter_guess, word, guesses))
    guess_button.pack()

    # Label for displaying hints
    hint_label = Label(frm_main, text="")
    hint_label.pack()

    # Store labels for guesses and hints
    global guess_labels
    global hint_labels
    guess_labels = []
    hint_labels = []

    root.mainloop()

def select_random_word():
    with open('adivinanzas_de_palabras.txt', 'r') as file:
        words = file.read().split()
    return random.choice(words)

def check_guess(root, entry, secret_word, guesses):
    guess = entry.get()
    entry.delete(0, tk.END)  # Clear the entry box

    if not guess:  # Check for empty guess
        show_hint(root, "Por favor adivine y ponga su respuesta aquí.")
        return

    if len(guess) != len(secret_word):
        show_hint(root, f"La respuesta deberá tener {len(secret_word)} letras.")
        return

    guesses.append(guess)
    hint = generate_hint(guess, secret_word)
    show_guess_and_hint(root, guess, hint)

    if guess.lower() == secret_word.lower():
        show_hint(root, "¡Lo adivinaste!")

def generate_hint(guess, secret_word):
    hint = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += f' {guess[i].upper()} '  # Correct letter and position
        elif guess[i] in secret_word:
            hint += f' {guess[i].lower()} '  # Correct letter, wrong position
        else:
            hint += ' _ '  # Incorrect letter
    return hint

def show_hint(root, hint):
    # Update hint label
    hint_label = root.children['!frame'].children['!label']  # Get the hint label
    hint_label.config(text=hint)

def show_guess_and_hint(root, guess, hint):
    # Add new labels for the guess and the hint
    guess_label = Label(root, text=guess)
    guess_label.pack()
    guess_labels.append(guess_label)

    hint_label = Label(root, text=hint)
    hint_label.pack()
    hint_labels.append(hint_label)

if __name__ == "__main__":
    main()