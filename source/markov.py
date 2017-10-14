#!/usr/bin/python

from random import randint


def read_text(text):
    """Generates archive based on text."""
    list_of_words = text.split() # Splits text up into individual words.
    list_of_dicts = [{'Preceding Word' : ''}] # Makes the blank preceding word.
    preceding_word = ''
    should_add = True
    for word in list_of_words: # Sorts through every word in the input text.
        for curr_dict in list_of_dicts: # Searches for a matching preceding word in all the available dictionaries.
            if curr_dict['Preceding Word'] == preceding_word:
                if curr_dict.has_key(word): # Adds 1 to value of word in dictionary if it exists.
                    curr_dict[word] += 1
                else: # Otherwise, create it with a value of 1.
                    curr_dict[word] = 1
            if curr_dict['Preceding Word'] == word: # Don't add a dictionary for the current word if one already exists.
                should_add = False
        if should_add == True: # If the word did not have a dictionary for it, make one.
            list_of_dicts.append({'Preceding Word' : word})
        for char in word: # Make the preceding word blank if the word had punctuation in it.
            if char == '.' or char == '?' or char == '!':
                word = ''
        preceding_word = word
        should_add = True
    return list_of_dicts


def _pick_from_dict(dictionary):
    """Randomly picks key from dictionary based on its value."""
    sum_of_ints = 0
    for key in dictionary: # Adds value of every key in dictionary together.
        if type(dictionary[key]) is int:
            sum_of_ints += dictionary[key]
    r = randint(0, sum_of_ints - 1) # Makes a random number in between 0 and sum_of_ints.
    sum_of_ints = 0
    for key in dictionary: # I can't really explain this, but it works.
        if type(dictionary[key]) is int:
            sum_of_ints += dictionary[key]
            if r < sum_of_ints:
                return key


def generate_markov_chain(list_of_dicts):
    """Generates archive based on text."""
    output = ''
    words_placed = 0
    preceding_word = ''
    while words_placed <= 100: # Keep going until 100 words have been placed.
        for item in list_of_dicts: # Search for a matching preceding word in the archive.
            if item['Preceding Word'] == preceding_word:
                if len(item) != 1:
                    preceding_word = _pick_from_dict(item)
                    output += preceding_word + ' '
                    words_placed += 1
                else: # If there are no other options, set preceding word to blank.
                    preceding_word = ''
        if words_placed == 0: # Prevents any infinite loops.
            return output
    return output
