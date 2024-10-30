from adivinanzas_de_palabras import generate_hint, check_guess, select_random_word
import pytest
import tkinter as tk

def test_generate_hint():
    guess = 'prima'
    secret_word = 'tarea'
    hint = generate_hint(guess, secret_word)

    assert hint == ' _ r _ _ A '

    guess = 'falso'
    secret_word = 'tarea'
    hint = generate_hint(guess, secret_word)
    assert hint == ' _ A _ _ _ '


def test_check_guess():
    root = tk.Tk()
    entry = ''
    guesses = []
    secret_word = 'tarea'
    checked_guess = check_guess(root, entry, guesses, secret_word)
    assert checked_guess == 'Por favor adivine y ponga su respuesta aquí.'

    entry = 'manzana'
    assert checked_guess == 'La respuesta deberá tener 5 letras.'


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])