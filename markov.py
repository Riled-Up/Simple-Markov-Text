#!/usr/bin/python

from random import randint


def read_text(text):
    list_of_words = text.split()
    list_of_dicts = []
    list_of_dicts.append({'Preceding Word' : ''})
    preceding_word = ''
    should_add = True
    for word in list_of_words:
        for curr_dict in list_of_dicts:
            if curr_dict['Preceding Word'] == preceding_word:
                if curr_dict.has_key(word):
                    curr_dict[word] += 1
                else:
                    curr_dict[word] = 1
            if curr_dict['Preceding Word'] == word:
                should_add = False
        if should_add == True:
            list_of_dicts.append({'Preceding Word' : word})
        for char in word:
            if char == '.' or char == '?' or char == '!':
                word = ''
        preceding_word = word
        should_add = True
    return list_of_dicts


def _pick_from_dict(dictionary):
    sum_of_ints = 0
    for key in dictionary:
        if type(dictionary[key]) is int:
            sum_of_ints += dictionary[key]
    r = randint(0, sum_of_ints - 1)
    sum_of_ints = 0
    for key in dictionary:
        if type(dictionary[key]) is int:
            sum_of_ints += dictionary[key]
            if r < sum_of_ints:
                return key


def generate_markov_chain(list_of_dicts):
    output = '' 
    words_placed = 0
    preceding_word = ''
    while words_placed <= 100:
        for item in list_of_dicts:
            if item['Preceding Word'] == preceding_word:
                if len(item) != 1:
                    preceding_word = _pick_from_dict(item)
                    output += preceding_word + ' '
                    words_placed += 1
                else:
                    preceding_word = ''
        if words_placed == 0:
            return output
    return output
