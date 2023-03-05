from messages import (drow_gallows, print_game_over, print_start_game,
                      print_you_win)
from randomWord import random_word


def forca():
    print_start_game()

    word = list(random_word())[:-1]
    letter_hide = list('_' * len(word))

    right_letters = {}
    wrong_letters = {}

    count_err = 0
    count_win = 0

    while True:
        if count_win == len(word):
            print_you_win(word)
            break

        print(letter_hide)
        letter_choice = input('Escolha uma letra: ').upper()
        print(30 * '\n')

        if len(letter_choice) > 1 or len(letter_choice) == 0:
            print(
                f'Você digitou "{letter_choice}" e deve digitar uma letra por vez!')

        elif letter_choice in right_letters or letter_choice in wrong_letters:
            print(f'Voce já digitou "{letter_choice}" Anteriormente')

        elif letter_choice.upper() in word:
            for indice, letter in enumerate(word):
                if letter_choice == letter:
                    letter_hide[indice] = letter_choice
                    right_letters[letter_choice] = letter_choice
                    count_win += 1
        else:
            wrong_letters[letter_choice] = letter_choice
            count_err += 1

            print('ErrrrrrrrÔouuuuuu')
            print(f'Restam {7 - count_err} chances')
            drow_gallows(count_err)
            if count_err == 7:
                print_game_over(word)
                break
    resp = input('Deseja jogar novamente? [S]im ou [N]ão:  ').upper()
    if resp in ('S', 'SIM'):
        forca()
    else:
        print('Ate a proxima!!!')
