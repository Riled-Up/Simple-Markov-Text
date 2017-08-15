#!/usr/bin/python

import markov
import Tkinter as tkinter

# Creates window.
root = tkinter.Tk()
root.title("Markov Chain")

# Creates bottom, left, and top frames.
output_text_frame = tkinter.Frame(root)
output_text_frame.pack(side = "bottom", fill = 'x')
archive_frame = tkinter.Frame(root)
archive_frame.pack(side = "right")
input_text_frame = tkinter.Frame(root)
input_text_frame.pack(side = "left", fill = "both", expand = True)

# Makes input widget with label.
input_text_label_string = tkinter.StringVar()
input_text_label = tkinter.Label(input_text_frame, textvariable = input_text_label_string)
input_text_label_string.set("Input Text:")
input_text_label.pack()
input_text = tkinter.Text(input_text_frame)
input_text.pack(fill = "both", expand = True)

# Makes output widget with label.
output_text_label_string = tkinter.StringVar()
output_text_label = tkinter.Label(output_text_frame, textvariable = output_text_label_string)
output_text_label_string.set("Output Text:")
output_text_label.pack()
output_text = tkinter.Text(output_text_frame)
output_text.pack(fill = "both")

# Makes archive list, label, and scrollbar.
archive_label_string = tkinter.StringVar()
archive_label = tkinter.Label(archive_frame, textvariable = archive_label_string)
archive_label_string.set("Archives:")
archive_label.pack()
archive_scrollbar = tkinter.Scrollbar(archive_frame)
archive_scrollbar.pack(side = "right", fill = "y")
archive_list = tkinter.Listbox(archive_frame, yscrollcommand = archive_scrollbar.set)
for line in range(100):
    archive_list.insert("end", "This is line number " + str(line))
archive_list.pack(side = "left")
archive_scrollbar.config(command = archive_list.yview)

# Enters the main loop of the GUI
root.mainloop()
