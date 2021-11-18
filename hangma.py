import random, sys
from typing import List

# TODO try to load these from a text file
WORD_LIST = [
"aleksandrija", "televizor", "paradajz", "viktor", "onomatopeja", "tigrica", "paradigma", "severozapad",
 "tikvica", "deponija", "laboratorija", "uzvicnik", "bukvar", "ogledalce", "poligraf"
           ]

GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) 
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def print_word_to_guess(letters: List) -> None:
    """Utility function to print the current word to guess"""
    print("Rec za pogadjanje: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    """Prints how many chances the player has used"""
    print("vi ste na koraku {0}/{1}.".format(current, total))


# funkcija za igru

def beginning() -> None:
    """Starts the game"""
    print("CAOS OVO JE IGRA VESALA!\n")
    while True:
        name = input("Unesi svoje ime \n").strip()
        if name == '':
            print("Eej, lepo unesi ime ")
        else:
            break


def ask_user_to_play() -> None:
    """Ask user if they want to play"""
    print("Ovo je savrsen trenutak za igranje igre \n")
    while True:
        gameChoice = input("Zelis li da igras? \n").upper()
        if gameChoice == "DA" or gameChoice == "D":
            break
        elif gameChoice == "NE" or gameChoice == "N":
            sys.exit("Steta, uzivaj u ostatku dana")
        else:
            print("Molim te napisi samo Da ili Ne")
            continue


def prepare_secret_word() -> None:
    """Prepare secret word and inform user of it"""
    for character in SECRET_WORD: # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    print("Dobro, rec koju treba da pogodis ima ", LENGTH_WORD, " slova")
    print("Budi oprezan, mozes da napises samo jedno slovo od a do z\n\n")
    print_word_to_guess(GUESS_WORD)


def guessing() -> None:
    """
    Main game loop to have user guess letters
    and inform them of the results
    """
    guess_taken = 1
    MAX_GUESS = 5
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Odaberi slovo\n").lower()
        if not guess in ALPHABET: #checking input
            print("Odaberi slovo  a-z ALFABET")
        elif guess in letter_storage: #checking if letter has been already used
            print("To slovo si vec probao, odaberi neko drugo")
        else:
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("Pogodio si!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("Svaka cast, pobedio si, bilo je sjajno igrati s tobom")
                    print("Kraj igre!")
                    break
            else:
                print("Slovo nije deo reci, pokusaj opet!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 5:
                    print(" Izvini, izgubio si, vise srece drugi put :<! Tajna rec je bila {0}".format(SECRET_WORD))


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()