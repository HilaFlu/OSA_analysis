import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from AnimalGroupWindow import AnimalGroupWindow
from Animal import Animal
import pandas as pd
from data_extraction import process_text_data
from pathlib import Path
from datetime import timedelta
import os
from Analysis_GUI import AnalysisGUI
<<<<<<< HEAD
from Experiment import *
=======

>>>>>>> fd27a5500d5c2e47165fd8b5265e94b0402b9273

class ExperimentDetailsGUI:
    """This is a starting GUI class.
    It initiallizes an instance of a GUI windows the accepts input for :
    Experiment name : str
    Researchers : list 
    
    |||
    
    It can upload an rtf. file and asks the user to input a session number.
    upon pressing the "Load file " button the path of the session 
    and file path are saved as key and value respectively for future use. 
    
    "Save file data" button will save the name of researchers and the name of the experiment 
    and print them in the terminal ", in addition , it opens a new GUI window where we can create
    our groups of animals
    """
    def __init__(self):
        self.exp = Experiment(groups={}, name="", experimenters=['base'])
        self.researchers = []
        self.files = {}
        self.groups = []
        self.exp_name = ""
        self.root = tk.Tk()
        self.root.title("Experiment Details")
        self.root.geometry("600x400")

        
        # Experiment Name AND entry box for text
        self.experiment_name_label = tk.Label(self.root, text="Experiment Name:")
        self.experiment_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.experiment_name_entry = tk.Entry(self.root, width=30)
        self.experiment_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Researchers Text label and text box to hold the names.
        self.researchers_label = tk.Label(self.root, text="Researchers:")
        self.researchers_label.grid(row=1, column=1, padx=3, pady=5, sticky=tk.E)
        self.researchers_text = tk.Text(self.root, height=3, width=22)
        self.researchers_text.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        
        ##Add researcher Buttton and entry box.
        self.add_researcher_button = tk.Button(self.root, text="Add Researcher", command=self.add_researcher)
        self.add_researcher_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.researcher_name_entry = tk.Entry(self.root, width=20)
        self.researcher_name_entry.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W)

        # Upload File button 
        self.upload_file_button = tk.Button(self.root, text="Upload .rtf File", command=self.upload_file)
        self.upload_file_button.grid(row=3, column=2, padx=10, pady=20, sticky=tk.S)

        ## File path label and Entry box
        self.file_path_label = tk.Label(self.root, text="File Path:")
        self.file_path_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.file_path_entry = tk.Entry(self.root, width=30, state='readonly')
        self.file_path_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        #Session Number label and entrybox
        self.session_number_label = tk.Label(self.root, text="Session Number:")
        self.session_number_label.grid(row=4, column=0, padx=10, pady=15, sticky=tk.N)
        self.session_number_entry = tk.Entry(self.root, width=10)
        self.session_number_entry.grid(row=4, column=1, padx=10, pady=15, sticky=tk.N)

        ##Load button for file path and entry 
        self.load_file_button = tk.Button(self.root, text="Load File", command=self.load_file)
        self.load_file_button.grid(row=4, column=2, padx=10, pady=15, sticky=tk.N)

        
        ##Save button
        self.save_button = tk.Button(self.root, text = "Save File Data" ,command = self.save_exp_data )
        self.save_button.grid(row=5, column=1, padx=10, pady=15, sticky=tk.E)
        
        # #Analysis Button
        
        # self.save_button = tk.Button(self.root, text = "Start Analysis" ,command = self.start_analysis )
        # self.save_button.grid(row=6, column=1, padx=10, pady=15, sticky=tk.E)
        
        # # Animal Groups
        # self.Creat_group_label = tk.Label(self.root, text="Groups")
        # self.Creat_group_label.grid(row=6, column=3, padx=10, pady=5, sticky=tk.N)

        # self.group_name_label = tk.Label(self.root, text="Group Name:")
        # self.group_name_label.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        # self.group_name_entry = tk.Entry(self.root, width=50)
        # self.group_name_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.E)

        # self.create_group_button = tk.Button(self.root, text="Add New Group", command=self.add_group)
        # self.create_group_button.grid(row=7, column=4, padx=10, pady=5, sticky=tk.W)

        # self.animals_frame = tk.Frame(self.root)
        # self.animals_frame.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)

         # Hide the animal group window initially

        self.root.mainloop()

    def add_researcher(self):
        """ command for add reasercher button - append the researchers name
        to the list"""
        researcher_name = self.researcher_name_entry.get()
        if researcher_name:
            self.researchers.append(researcher_name)
            self.researcher_name_entry.delete(0, tk.END)
            self.update_researchers_text()
            self.exp.add_experimenter(researcher_name)

    def update_researchers_text(self):
        self.researchers_text.config(state='normal')
        self.researchers_text.delete(1.0, tk.END)
        for researcher in self.researchers:
            self.researchers_text.insert(tk.END, f"{researcher}\n")
        self.researchers_text.config(state='disabled')

    def upload_file(self):
        """ command for "Upload rtf file" , asks the user to choose an .rtf file 
        off of his computer and and displays the path"""
        file_path = filedialog.askopenfilename(filetypes=[("RTF Files", "*.rtf")])
        if file_path:
            self.file_path_entry.config(state='normal')
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(tk.END, file_path)
            self.file_path_entry.config(state='readonly')

    def load_file(self):
        """command for the load data button"""
        file_path = self.file_path_entry.get()
        session_number = self.session_number_entry.get()
        if file_path and session_number.isdigit():
            self.files[session_number] =  file_path
            self.session_number_entry.delete(0, tk.END)
            self.file_path_entry.config(state='normal')
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.config(state='readonly')
            messagebox.showinfo("File Loaded", "File loaded successfully.")
        else:
            messagebox.showerror("Error", "Please provide a valid file path and session number.")
        self.exp.add_session(file_path, session_number)

    def save_exp_data(self):
        """saves The exp name and opens the Animal group GUI for group creation"""
        self.exp_name = self.experiment_name_entry.get()
        print("Experiment -",self.exp_name, "has been initiallized by", str(self.researchers))  
        print("the dict for the files is " , self.files  )
        self.exp.name = self.exp_name
        """ this saves the name of the of the Experiment and the olist of researchers"""
        Creat_groups_gui = AnimalGroupWindow()  
    
    
    # def add_group(self):
    #     group_name = self.group_name_entry.get(
    #     self.group_name_entry.delete(0, tk.END)

    #     group_label = tk.Label(self.animals_frame, text=f"Group Name: {group_name}")
    #     group_label.pack(pady=5)

    #     animal_frame = tk.Frame(self.animals_frame)
    #     animal_frame.pack()

    #     animal_id_label = tk.Label(animal_frame, text="Animal ID:")
    #     animal_id_label.pack(side="left", padx=5, pady=5)

    #     animal_id_entry = tk.Entry(animal_frame, width=10)
    #     animal_id_entry.pack(side="left", padx=5, pady=5)

    #     animal_box_label = tk.Label(animal_frame, text="Animal Box:")
    #     animal_box_label.pack(side="left", padx=5, pady=5)

    #     animal_box_entry = tk.Entry(animal_frame, width=10)
    #     animal_box_entry.pack(side="left", padx=5, pady=5)

    #     animal_weight_label = tk.Label(animal_frame, text="Animal Weight:")
    #     animal_weight_label.pack(side="left", padx=5, pady=5)

    #     animal_weight_entry = tk.Entry(animal_frame, width=10)
    #     animal_weight_entry.pack(side="left", padx=5, pady=5)

    #     animal_sex_label = tk.Label(animal_frame, text="Animal Sex:")
    #     animal_sex_label.pack(side="left", padx=5, pady=3)

    #     animal_sex_combobox = ttk.Combobox(animal_frame, values=["", "Male", "Female"])
    #     animal_sex_combobox.pack(side="left", padx=5, pady=5)

    #     group = {
    #         "name": group_name,
    #         "animals": [],
    #         "textbox": None  # Placeholder for the group's textbox
    #     }

    #     def add_animal():
    #         animal = {
    #             "id": animal_id_entry.get(),
    #             "box": animal_box_entry.get(),
    #             "weight": animal_weight_entry.get(),
    #             "sex": animal_sex_combobox.get()
    #         }
    #         group["animals"].append(animal)

    #         animal_id_entry.delete(0, tk.END)
    #         animal_box_entry.delete(0, tk.END)
    #         animal_weight_entry.delete(0, tk.END)
    #         animal_sex_combobox.delete(0, tk.END)

    #         # Create the group's textbox if it doesn't exist
    #         if not group["textbox"]:
    #             group["textbox"] = tk.Text(self.animals_frame, height=4, width=60)
    #             group["textbox"].pack()

    #         # Display the animal's information in the same line in the textbox
    #         group["textbox"].insert(tk.END, f"Animal ID: {animal['id']} | ")
    #         group["textbox"].insert(tk.END, f"Animal Box: {animal['box']} | ")
    #         group["textbox"].insert(tk.END, f"Animal Weight: {animal['weight']} | ")
    #         group["textbox"].insert(tk.END, f"Animal Sex: {animal['sex']} | ")
    #         group["textbox"].insert(tk.END, "[Remove]\n")

    #     def remove_animal():
    #         if group["animals"]:
    #             group["animals"].pop()
    #             group["textbox"].delete("end-2l", "end-1l")  # Remove the last line from the textbox

    #     add_animal_button = tk.Button(animal_frame, text="Add to Group", command=add_animal)
    #     add_animal_button.pack(side="left", padx=5, pady=5)

    #     remove_animal_button = tk.Button(animal_frame, text="Remove from Group", command=remove_animal)
    #     remove_animal_button.pack(side="left", padx=5, pady=5)

    #     self.groups.append(group)

if __name__ == '__main__':
    gui = ExperimentDetailsGUI()
    exp = gui.exp
    

