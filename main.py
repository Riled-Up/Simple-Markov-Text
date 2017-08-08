#!/usr/bin/python

import markov
from Tkinter import *

# Creates window.
root = Tk()

# Makes input widget with label.
input_text_label_string = StringVar()
input_text_label = Label(root, textvariable = input_text_label_string)
input_text_label_string.set("Input Text:")
input_text_label.pack(side = LEFT)
input_text = Text(root)
input_text.pack(side = LEFT)

# Enters the main loop of the GUI
root.mainloop()
