#!/usr/bin/python

from random import randint


def read_text(text):
    list_of_words = text.split()
    word_frequency = {}
    list_of_dicts = []
    preceding_word = ''
    should_add = True
    for word in list_of_words:
        if word_frequency.has_key(word):
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
        for curr_dict in list_of_dicts:
            if curr_dict['Preceding Word'] == preceding_word:
                should_add = False
        if should_add:
            list_of_dicts.append({'Preceding Word': preceding_word})
        for curr_dict in list_of_dicts:
            if curr_dict['Preceding Word'] == preceding_word:
                if curr_dict.has_key(word):
                    curr_dict[word] += 1
                else:
                    curr_dict[word] = 1
        preceding_word = word
        should_add = True
    return word_frequency, list_of_dicts


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


def gen_markov_chain(amount_of_sentences):
    count = 0
    last_word_placed = "."
    output_text = ""
    while count != amount_of_sentences:
        while '.' in last_word_placed:
            last_word_placed = _pick_from_dict(_word_frequency)
        output_text += last_word_placed.capitalize() + ' '
        while '.' not in last_word_placed:
            for curr_dict in _list_of_dicts:
                if curr_dict["Preceding Word"] == last_word_placed:
                    last_word_placed = _pick_from_dict(curr_dict)
                    output_text += last_word_placed + ' '
                    break
        count += 1
    return output_text


