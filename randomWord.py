import random


def random_word():
    with open('words.txt', 'r') as words:
        words_list = words.readlines()
        word = random.choice(words_list).upper()
        return word
