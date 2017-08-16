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
# Makes input widget with label and "add to archive" button.
input_text_label_string = tkinter.StringVar()
input_text_label = tkinter.Label(input_text_frame, textvariable = input_text_label_string)
input_text_label_string.set("Input Text:")
input_text_label.pack()
input_text = tkinter.Text(input_text_frame)
input_text.pack(fill = "both", expand = True)
add_to_archive_button = tkinter.Button(input_text_frame, text = "Add to Archive", command = 0)
add_to_archive_button.pack(side = "bottom")
# Makes output widget with label.
output_text_label_string = tkinter.StringVar()
output_text_label = tkinter.Label(output_text_frame, textvariable = output_text_label_string)
output_text_label_string.set("Output Text:")
output_text_label.pack()
output_text = tkinter.Text(output_text_frame)
output_text.pack(fill = "both")
# Makes archive list, label, and scrollbar.
current_archive_frame = tkinter.Frame(archive_frame)
current_archive_frame.pack()
archive_list_frame = tkinter.Frame(archive_frame)
archive_list_frame.pack()
archive_label_string = tkinter.StringVar()
archive_label = tkinter.Label(current_archive_frame, textvariable = archive_label_string)
archive_label_string.set("Current Archive:")
archive_label.pack(side = "top")
archive_current_string = tkinter.StringVar()
archive_current_string.set("Placeholder")
archive_current = tkinter.Entry(current_archive_frame, textvariable = archive_current_string)
archive_current.pack(fill = "x")
archive_list_scrollbar = tkinter.Scrollbar(archive_list_frame)
archive_list = tkinter.Listbox(archive_list_frame, yscrollcommand = archive_list_scrollbar.set)
archive_list_scrollbar.config(command = archive_list.yview)
for line in range(100):
    archive_list.insert("end", "This is line number " + str(line))
archive_list.pack(side = "left")
archive_list_scrollbar.pack(side = "right", fill = "y")
# Enters the main loop of the GUI
root.mainloop()
