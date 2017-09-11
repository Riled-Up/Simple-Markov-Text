#!/usr/bin/python

from random import randint

_list_of_dicts = []
_word_frequency = {}


def read_text(text):
    global _word_frequency
    global _list_of_dicts
    curr_dict = {"Preceding Word": ""}
    start_of_word = 0
    prev_word = ""
    should_add = True
    curr_char = 0
    index = 0
    while curr_char != len(text):
        if text[curr_char] != ' ' or text[curr_char] != '\t':
            start_of_word = curr_char
            while text[curr_char] != ' ' or text[curr_char] != '\t':
                curr_char += 1
            if prev_word != "":
                while index != len(_list_of_dicts):
                    curr_dict = _list_of_dicts[index]
                    if curr_dict["Preceding Word"] == prev_word:
                        should_add = False
                        break
                    index += 1
                if should_add:
                    curr_dict = {"Preceding Word": prev_word}
                    _list_of_dicts.append(curr_dict)
                should_add = True
                curr_dict = _list_of_dicts[index]
                index = 0
                if curr_dict.has_key(text[start_of_word:curr_char]):
                    curr_dict[text[start_of_word:curr_char]] += 1
                else:
                    curr_dict[text[start_of_word:curr_char]] = 1
                curr_dict = {"Preceding Word": ""}
            if _word_frequency.has_key(text[start_of_word:curr_char]):
                _word_frequency[text[start_of_word:curr_char]] += 1
            else:
                _word_frequency[text[start_of_word:curr_char]] = 1
            prev_word = text[start_of_word:curr_char]
        curr_char += 1


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


