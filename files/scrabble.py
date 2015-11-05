#!/usr/bin/env python

"""
Scrabble Checker.

This is a pretty rudimentary implementation - I'm sure that there are
much better ways to do the same thing. Oh well.

Do whatever you want with it.
"""


import os.path


def anagrams(word):
    """ Generate all of the anagrams of a word. """
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            if letter not in word[:i]:    # Avoid duplicating earlier words
                for j in anagrams(word[:i]+word[i+1:]):
                    yield j + letter


# Standard Scrabble scores
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


words = open(os.path.join(os.path.dirname(__file__), '', 'possible-words.txt'))


list = [i.strip() for i in words]    # All valid scrabble words to a list
rack = input("Enter the letters in your rack: ")
rack = rack.upper()
valid_words = []


for word in list:    # Iterate through valid Scrabble words
    candidate = True
    rack_letters = [x for x in rack]

    for letter in word:
        if letter not in rack_letters:
            candidate = False
            break    # No need to keep checking letters.

        else:
            rack_letters.remove(letter)    # Remove unnecessary letters

    if candidate:
        total = 0

        for letter in word:    # Get the Scrabble scores for each word.
            total = total + scores[letter.lower()]

        valid_words.append([total, word])


valid_words.sort()


for entry in valid_words:
    score = entry[0]
    word = entry[1]
    print(str(score) + " - " + word)


print('\n')
input("Enter to close")
