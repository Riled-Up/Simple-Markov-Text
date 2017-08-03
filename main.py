#!/home/riley/Projects/markov-chain

import markov

markov.read_text(open("input.txt").read())
print markov.gen_markov_chain(7)
