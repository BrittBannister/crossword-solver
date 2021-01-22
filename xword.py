#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Britt Bannister"


def check_word(word, word_dict):
    '''checks our word against words in dict to find a match'''
    word_list = []
    for w in word_dict:
        if len(w) == len(word):
            word_list.append(w)
    for i, char in enumerate(word):
        if char != ' ':
            word_list = [w for w in word_list if w[i] == char]
    for w in word_list:
        print(w)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
        # print(words)

    test_word = input(
        'Please enter a word to solve.\n'
        'Use spaces to signify unknown letters: ').lower()

    check_word(test_word, words)
    # raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
