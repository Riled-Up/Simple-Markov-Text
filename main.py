#!/usr/bin/python

import markov
import Tkinter as tk


class MarkovChainWindow:
    def __init__(self, root):
        root.title("Markov Chain")
        # Makes widgets.
        self.top_frame = tk.Frame(root)
        self.output_text_frame = tk.Frame(root)
        self.output_text_label = tk.Label(self.output_text_frame, text = "Output Text:")
        self.output_text = tk.Text(self.output_text_frame, bd = 2, relief = "ridge", height = 19)
        self.input_text_frame = tk.Frame(self.top_frame)
        self.input_text_label = tk.Label(self.input_text_frame, text = "Input Text:")
        self.input_text = tk.Text(self.input_text_frame, bd = 2, relief = "ridge", height = 19)
        self.archive_frame = tk.Frame(self.top_frame)
        self.archive_current_frame = tk.Frame(self.archive_frame)
        self.archive_current_label = tk.Label(self.archive_current_frame, text = "Current Archive:")
        self.archive_current_string = tk.StringVar()
        self.archive_current_string.set("Placeholder")
        self.archive_current = tk.Entry(self.archive_current_frame, textvariable = self.archive_current_string)
        self.archive_list_frame = tk.Frame(self.archive_frame)
        self.archive_list_scrollbar = tk.Scrollbar(self.archive_list_frame)
        self.archive_list = tk.Listbox(self.archive_list_frame, yscrollcommand = self.archive_list_scrollbar.set)
        self.archive_list_scrollbar.config(command = self.archive_list.yview)
        for line in range(100):
            self.archive_list.insert("end", "This is line number " + str(line))
        self.button_horizontal_frame = tk.Frame(self.archive_frame)
        self.button_new_archive = tk.Button(self.button_horizontal_frame, text = "New", command = 0)
        self.button_delete_archive = tk.Button(self.button_horizontal_frame, text = "Delete", command = 0)
        self.button_generate_output = tk.Button(self.archive_frame, text = "Generate Text from Archive", command = 0)
        self.button_add_to_archive = tk.Button(self.archive_frame, text = "Add Text to Archive", command = 0)
        # Packs widgets.
        self.top_frame.pack(fill = 'x')
        self.output_text_frame.pack(fill = "both", expand = True)
        self.output_text_label.pack()
        self.output_text.pack(fill = "both", expand = True)
        self.archive_frame.pack(side = "right")
        self.archive_current_frame.pack()
        self.archive_current_label.pack()
        self.archive_current.pack(fill = 'x')
        self.archive_list_frame.pack()
        self.archive_list_scrollbar.pack(side = "right", fill = 'y')
        self.archive_list.pack(side = "left")
        self.button_horizontal_frame.pack(fill = 'x')
        self.button_new_archive.pack(side = "left", fill = 'x', expand = True)
        self.button_delete_archive.pack(side = "right", fill = 'x', expand = True)
        self.button_generate_output.pack(side = "bottom", fill = 'x')
        self.button_add_to_archive.pack(side = "bottom", fill = 'x')
        self.input_text_frame.pack(side = "left", fill = "both", expand = True)
        self.input_text_label.pack()
        self.input_text.pack(fill = "both", expand = True)


if __name__ == "__main__":
    root = tk.Tk()
    MarkovChainWindow(root)
    root.mainloop()
