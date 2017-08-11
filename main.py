#!/usr/bin/python

import markov
from Tkinter import *

# Creates window.
root = Tk()

# Creates bottom, left, and top frames.
output_text_frame = Frame(root)
output_text_frame.pack(side = BOTTOM, fill = X)
input_text_frame = Frame(root)
input_text_frame.pack(side = LEFT, fill = X, expand = True)
archive_frame = Frame(root)
archive_frame.pack(side = RIGHT)

# Makes input widget with label.
input_text_label_string = StringVar()
input_text_label = Label(input_text_frame, textvariable = input_text_label_string)
input_text_label_string.set("Input Text:")
input_text_label.pack()
input_text = Text(input_text_frame)
input_text.pack(fill = BOTH)

# Makes output widget with label.
output_text_label_string = StringVar()
output_text_label = Label(output_text_frame, textvariable = output_text_label_string)
output_text_label_string.set("Output Text:")
output_text_label.pack()
output_text = Text(output_text_frame)
output_text.pack(fill = BOTH)

# Makes archive list, label, and scrollbar.
archive_label_string = StringVar()
archive_label = Label(archive_frame, textvariable = archive_label_string)
archive_label_string.set("Archives:")
archive_label.pack()
archive_scrollbar = Scrollbar(archive_frame)
archive_scrollbar.pack(side = RIGHT, fill = Y)
archive_list = Listbox(archive_frame, yscrollcommand = archive_scrollbar.set)
for line in range(100):
    archive_list.insert(END, "This is line number " + str(line))
archive_list.pack(side = LEFT)
archive_scrollbar.config(command = archive_list.yview)

# Enters the main loop of the GUI
root.mainloop()
