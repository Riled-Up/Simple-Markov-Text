import markov
import Tkinter as tkinter

# Creates window.
root = tkinter.Tk()
root.title("Markov Chain")

# Creates widgets.
top_frame = tkinter.Frame(root)
output_text_frame = tkinter.Frame(root)
output_text_label = tkinter.Label(output_text_frame, text = "Output Text:")
output_text = tkinter.Text(output_text_frame, bd = 2, relief = "ridge", height = 19)
archive_frame = tkinter.Frame(top_frame)
archive_current_frame = tkinter.Frame(archive_frame)
archive_current_label = tkinter.Label(archive_current_frame, text = "Current Archive:")
archive_current_string = tkinter.StringVar()
archive_current_string.set("Placeholder")
archive_current = tkinter.Entry(archive_current_frame, textvariable = archive_current_string)
archive_list_frame = tkinter.Frame(archive_frame)
archive_list_scrollbar = tkinter.Scrollbar(archive_list_frame)
archive_list = tkinter.Listbox(archive_list_frame, yscrollcommand = archive_list_scrollbar.set)
archive_list_scrollbar.config(command = archive_list.yview)
for line in range(100):
    archive_list.insert("end", "This is line number " + str(line))
button_horizontal_frame = tkinter.Frame(archive_frame)
button_new_archive = tkinter.Button(button_horizontal_frame, text = "New", command = 0)
button_delete_archive = tkinter.Button(button_horizontal_frame, text = "Delete", command = 0)
button_generate_output = tkinter.Button(archive_frame, text = "Generate Text from Archive", command = 0)
button_add_to_archive = tkinter.Button(archive_frame, text = "Add Text to Archive", command = 0)
input_text_frame = tkinter.Frame(top_frame)
input_text_label = tkinter.Label(input_text_frame, text = "Input Text:")
input_text = tkinter.Text(input_text_frame, bd = 2, relief = "ridge", height = 19)

# Packs widgets.
top_frame.pack(fill = 'x')
output_text_frame.pack(fill = "both", expand = True)
output_text_label.pack()
output_text.pack(fill = "both", expand = True)
archive_frame.pack(side = "right")
archive_current_frame.pack()
archive_current_label.pack()
archive_current.pack(fill = 'x')
archive_list_frame.pack()
archive_list_scrollbar.pack(side = "right", fill = 'y')
archive_list.pack(side = "left")
button_horizontal_frame.pack(fill = 'x')
button_new_archive.pack(side = "left", fill = 'x', expand = True)
button_delete_archive.pack(side = "right", fill = 'x', expand = True)
button_generate_output.pack(side = "bottom", fill = 'x')
button_add_to_archive.pack(side = "bottom", fill = 'x')
input_text_frame.pack(side = "left", fill = "both", expand = True)
input_text_label.pack()
input_text.pack(fill = "both", expand = True)

# Enters the main loop of the GUI.
root.mainloop()
