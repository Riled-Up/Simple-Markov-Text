#!/usr/bin/python

# IMPORTANT: If you messed around with the location of this file, make sure this variable
# is set to the relative path of the "archives" directory.
RELATIVE_PATH_TO_ARCHIVE_DIR = './archives/'

import markov
import Tkinter as tk
import tkMessageBox
import pickle
import os

class MarkovChainWindow:
    """Contains all the widgets and methods for the program."""
    def __init__(self, root):
        """Creates widgets, packs them, and initializes the archive list."""
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
        self.archive_current = tk.Entry(self.archive_current_frame)
        self.archive_current.bind("<Key>", self.archive_entry_changed) # Calls function when user types in field.
        self.archive_list_frame = tk.Frame(self.archive_frame)
        self.archive_list_scrollbar = tk.Scrollbar(self.archive_list_frame)
        self.archive_list = tk.Listbox(self.archive_list_frame, yscrollcommand = self.archive_list_scrollbar.set, selectmode = 'single')
        self.archive_list.bind("<<ListboxSelect>>", self.archive_list_clicked) # Calls function when user selects item.
        self.archive_list_scrollbar.config(command = self.archive_list.yview)
        self.update_archive_list()
        self.archive_list.activate('anchor') # Activates last item in archive_list.
        self.archive_current.insert(0, self.archive_list.get('active')) # Puts name of selected archive in archive_current.
        self.button_horizontal_frame = tk.Frame(self.archive_frame)
        self.button_new_archive = tk.Button(self.button_horizontal_frame, text = "New", command = self.new_archive)
        self.button_delete_archive = tk.Button(self.button_horizontal_frame, text = "Delete", command = self.delete_archive)
        self.button_generate_output = tk.Button(self.archive_frame, text = "Generate Text from Archive", command = self.generate_output)
        self.button_add_to_archive = tk.Button(self.archive_frame, text = "Add Text to Archive", command = self.add_text_to_archive)
        # Packs widgets.
        self.top_frame.pack(fill = 'x')
        self.output_text_frame.pack(fill = "both", expand = True)
        self.output_text_label.pack()
        self.output_text.pack(fill = "both", expand = True)
        self.archive_frame.pack(side = "right")
        self.archive_current_frame.pack() 
        self.archive_current_label.pack()
        self.archive_current.pack(fill = 'x') 
        self.archive_list_frame.pack(fill = 'both', expand = True)
        self.archive_list_scrollbar.pack(side = "right", fill = 'y')
        self.archive_list.pack(side = "left", fill = 'both', expand = True)
        self.button_horizontal_frame.pack(fill = 'x')
        self.button_new_archive.pack(side = "left", fill = 'x', expand = True)
        self.button_delete_archive.pack(side = "right", fill = 'x', expand = True)
        self.button_generate_output.pack(side = "bottom", fill = 'x')
        self.button_add_to_archive.pack(side = "bottom", fill = 'x')
        self.input_text_frame.pack(side = "left", fill = "both", expand = True)
        self.input_text_label.pack()
        self.input_text.pack(fill = "both", expand = True)
    
    def save_obj(self, obj, name):
        """Saves .pkl objects."""
        with open(RELATIVE_PATH_TO_ARCHIVE_DIR + name + '.pkl', 'wb') as f: # Saves it in archive directory
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    
    def load_obj(self, name):
        """Loads .pkl objects."""
        with open(RELATIVE_PATH_TO_ARCHIVE_DIR + name + '.pkl', 'rb') as f: # Opens it in archive directory
            return pickle.load(f)
    
    def archive_list_clicked(self, event):
        """Called when user selects something in the listbox."""
        if self.archive_list.curselection() == (): # Returns 1 if nothing in archive_list is selected.
            return 1
        self.archive_current.delete(0, 'end') # Clears archive_current.
        self.archive_current.insert(0, self.archive_list.get(self.archive_list.curselection())) # Inserts title of selected archive.
    
    def archive_entry_changed(self, event):
        """Checks to see if anything in archive_list matches user input. Activates the input if input matches."""
        self.update_archive_list()
        index = 0 # Tracks position in archive_list.
        for archive in self.archive_list.get(0, 'end'): # Searches through name of items.
            if archive == self.archive_current.get() + event.char: # Activates if name matches user input.
                self.archive_list.activate(index)
            else: # Increments index if name of item did not match.
                index += 1
    
    def update_archive_list(self):
        """Updates the items in the archive_list. Useful if user puts in .pkl file in archives directory manually."""
        self.archive_list.delete(0, 'end') # Deletes all items 
        for archive in os.listdir(RELATIVE_PATH_TO_ARCHIVE_DIR): # Inserts any files with .pkl extension into archive_list.
            if archive[-4:] == '.pkl':
                self.archive_list.insert('end', archive[:-4])
                
    def new_archive(self):
        """Adds blank archive to archives directory."""
        self.update_archive_list()
        if self.archive_current.get() == '': # Checks if archive_current is blank.
            tkMessageBox.showwarning("Nothing entered", "You didn't type anything in the text box.")
            return 1
        for archive in os.listdir(RELATIVE_PATH_TO_ARCHIVE_DIR):
            if archive[:-4] == self.archive_current.get(): # Checks if archive already exists.
                tkMessageBox.showwarning("Archive already exists", "The archive '%s' already exists." % archive[:-4])
                return 1
        self.save_obj([], self.archive_current.get()) # Saves blank archive.
        self.archive_list.insert('end', self.archive_current.get()) # Inserts into archive_list.
        self.archive_list.activate('end') # Activates it in archive_list.
        
    
    def delete_archive(self):
        """Deletes archive in archives directory."""
        archive_exists = False
        # Reaffirms user decision and checks if archive exists.
        for archive in os.listdir(RELATIVE_PATH_TO_ARCHIVE_DIR):
            if archive[:-4] == self.archive_current.get():
                if tkMessageBox.askyesno("Archive deletion", "Are you sure you want to delete the '%s' archive?" % self.archive_current.get()):
                    os.remove('RELATIVE_PATH_TO_ARCHIVE_DIR%s' % archive)
                archive_exists = True
        if archive_exists == False:
            tkMessageBox.showwarning("No archive named '%s'" % self.archive_current.get(), "There is currently no archive named '%s'." % self.archive_current.get())
        self.archive_list.activate('end') # Activates last item in archive_list.
        self.update_archive_list()
        self.archive_current.delete(0, 'end') # Deletes text inside archive_current.
        self.archive_current.insert(0, self.archive_list.get('end')) # Inserts name of last archive in archive_list.
    
    
    def add_text_to_archive(self):
        """Adds data to archive."""
        self.update_archive_list()
        # Checks if an archive is selected and if the archive exists.
        if self.archive_current.get() == '':
            tkMessageBox.showwarning("No archive selected", "Please select an archive.")
            return 1
        pickle_file_exists = False
        for archive in self.archive_list.get(0, 'end'):
            if archive == self.archive_current.get():
                pickle_file_exists = True
        if pickle_file_exists == False:
            tkMessageBox.showwarning("No archive named '%s'" % self.archive_current.get(), "There is currently no archive named '%s'." % self.archive_current.get())
            return 1
        new_list_of_dicts = markov.read_text(self.input_text.get(1.0, "end-1c")) # Creates new archive from input_text.
        old_list_of_dicts = self.load_obj(self.archive_current.get()) # Gets old archive.
        # Merges the old archive with the new one.
        should_add = True
        for curr_old_dict in old_list_of_dicts: # Sorts through old archive to find matching preceding words in the new one.
            for curr_new_dict in new_list_of_dicts:
                if curr_old_dict['Preceding Word'] == curr_new_dict['Preceding Word']:
                    should_add = False
                    for old_word in curr_old_dict:
                        if curr_new_dict.has_key(old_word) and old_word != 'Preceding Word': # Adds total to word if they match.
                            curr_new_dict[old_word] += curr_old_dict[old_word]
                        else: # Otherwise, add the word to the dictionary.
                            curr_new_dict[old_word] = curr_old_dict[old_word]
            if should_add: # Adds dictionary to the new archive if an identical preceding word is not found.
                new_list_of_dicts.append(curr_old_dict)
            should_add = True
        self.save_obj(new_list_of_dicts, self.archive_current.get()) # Saves the merged archive.
        self.input_text.delete('1.0', 'end') # Clears input.


    def generate_output(self):
        """Generates text from archive."""
        self.update_archive_list()
        # Checks if current archive is blank and if it exists.
        if self.archive_current.get() == '':
            tkMessageBox.showwarning("No archive selected", "Please select an archive.")
            return 1
        pickle_file_exists = False
        for archive in self.archive_list.get(0, 'end'):
            if archive == self.archive_current.get():
                pickle_file_exists = True
        if pickle_file_exists == False:
            tkMessageBox.showwarning("No archive named '%s'" % self.archive_current.get(), "There is currently no archive named '%s'." % self.archive_current.get())
            return 1
        self.output_text.delete('1.0', 'end') # Clears output_text.
        self.output_text.insert('1.0', markov.generate_markov_chain(self.load_obj(self.archive_current.get()))) # Inserts whatever generate_markov_chain returns.


if __name__ == "__main__": # Only perform if this file is being run directly.
    root = tk.Tk() # Creates window.
    MarkovChainWindow(root) # Initializes the window.
    root.mainloop() # Enters the main loop of the window.
