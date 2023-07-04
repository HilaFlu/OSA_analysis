import tkinter as tk
from tkinter import ttk
from Animal import Animal
import datetime
import pandas as pd


class AnimalGroupWindow:
    """This GUI is designed to handle attribute input from the user.
    asking for :
    Group name: - float 
    Once entered , using the "Create new group" Button, the user is given the 
    ability to grant the Animal attributes such as:
    Animal ID :int
    Animal box : int
    Animal weight : int 
    Year of weight (YYYY):int
    Month of weight (MM) : int
    Day of weight (DD) : int
    Sex : communication box (Male /Female).
    after entering all those the user adds the animal to the group via the "Add to group"
    button. where it is saved as an Animal instance a part of a list that 
    is a value for a key which is the name of the group.
    """
    def __init__(self):
        self.groups = {}

        self.animal_group_window = tk.Tk()
        self.animal_group_window.title("Animal Group")
        self.animal_group_window.geometry("800x600")

        self.group_name_label = tk.Label(self.animal_group_window, text="Group Name:")
        self.group_name_label.pack(pady=10)

        self.group_name_entry = tk.Entry(self.animal_group_window, width=50)
        self.group_name_entry.pack()

        self.create_group_button = tk.Button(self.animal_group_window, text="Add New Group",
                                             command=self.add_group)
        self.create_group_button.pack(pady=10)

        self.animals_frame = tk.Frame(self.animal_group_window)
        self.animals_frame.pack()

        self.Done_button = tk.Button(self.animal_group_window, text="Done", command=self.Done)
        self.Done_button.pack()
        self.animal_group_window.mainloop()

    def add_group(self):
        """command for add group
        this command will create an instance of Animal() with the input of the user
        append it to a list. afterwards the field are emptied allowing the user to 
        input a new instance."""
        group_name = float(self.group_name_entry.get())
        self.group_name_entry.delete(0, tk.END)

        group_label = tk.Label(self.animals_frame, text=f"Group Name: {group_name}")
        group_label.pack(pady=5)

        animal_frame = tk.Frame(self.animals_frame)
        animal_frame.pack()

        animal_id_label = tk.Label(animal_frame, text="Animal ID:")
        animal_id_label.pack(side="left", padx=5, pady=5)

        animal_id_entry = tk.Entry(animal_frame, width=10)
        animal_id_entry.pack(side="left", padx=5, pady=5)

        animal_box_label = tk.Label(animal_frame, text="Animal Box:")
        animal_box_label.pack(side="left", padx=5, pady=5)

        animal_box_entry = tk.Entry(animal_frame, width=10)
        animal_box_entry.pack(side="left", padx=5, pady=5)

        animal_weight_label = tk.Label(animal_frame, text="Animal Weight:")
        animal_weight_label.pack(side="left", padx=5, pady=5)

        animal_weight_entry = tk.Entry(animal_frame, width=10)
        animal_weight_entry.pack(side="left", padx=5, pady=5)

        animal_weight_date_year_label = tk.Label(animal_frame, text="Year of Animal Weigh (foramt YYYY):")
        animal_weight_date_year_label.pack(side="top", padx=5, pady=5)

        animal_weight_date_year_entry = tk.Entry(animal_frame, width=10)
        animal_weight_date_year_entry.pack(side="top", padx=5, pady=5)

        animal_weight_date_month_label = tk.Label(animal_frame, text="Month of Animal Weigh (format MM):")
        animal_weight_date_month_label.pack(side="top", padx=5, pady=5)

        animal_weight_date_month_entry = tk.Entry(animal_frame, width=10)
        animal_weight_date_month_entry.pack(side="top", padx=5, pady=5)

        animal_weight_date_day_label = tk.Label(animal_frame, text="Day of Animal Weigh (format DD):")
        animal_weight_date_day_label.pack(side="top", padx=5, pady=5)

        animal_weight_date_day_entry = tk.Entry(animal_frame, width=10)
        animal_weight_date_day_entry.pack(side="top", padx=5, pady=5)

        animal_sex_label = tk.Label(animal_frame, text="Animal Sex:")
        animal_sex_label.pack(side="left", padx=5, pady=3)

        animal_sex_label = tk.Label(animal_frame)
        animal_sex_combobox = ttk.Combobox(animal_frame, values=["", "Male", "Female"])

        animal_sex_label.pack()
        animal_sex_combobox.pack(side="left", padx=5, pady=5)
        # animal_sex_entry = tk.Entry(animal_frame, width=10)
        # animal_sex_entry.pack(side="left", padx=5, pady=5)

        # BY GEORGE: I hashed your code here, and wrote a code that adds it to groups as group_name for key and list of animals as value :)
        # group = {
        #    "name": group_name,
        #    "animals": [],
        #    "textbox": None  # Placeholder for the group's textbox
        # }

        # THIS IS BY HILA:
        self.groups[group_name] = []

        def add_animal():
            # BY GEORGE:
            # animal = {
            #    "id": animal_id_entry.get(),
            #    "box": animal_box_entry.get(),
            #    "weight": animal_weight_entry.get(),
            #    "sex": animal_sex_combobox.get()
            # }
            # group["animals"].append(animal)

            # BY HILA:
            weight_date = datetime.date(int(animal_weight_date_year_entry.get()),
                                        int(animal_weight_date_month_entry.get()),
                                        int(animal_weight_date_day_entry.get()))
            animal = Animal(animal_id=int(animal_id_entry.get()),
                            animal_box=int(animal_box_entry.get()),
                            sex=str(animal_sex_combobox.get()),
                            weight={weight_date: float(animal_weight_entry.get())},
                            animal_data=pd.DataFrame())

            self.groups[group_name].append(animal)

            animal_id_entry.delete(0, tk.END)
            animal_box_entry.delete(0, tk.END)
            animal_weight_entry.delete(0, tk.END)
            animal_weight_date_day_entry.delete(0, tk.END)
            animal_weight_date_year_entry.delete(0, tk.END)
            animal_weight_date_month_entry.delete(0, tk.END)
            animal_sex_combobox.delete(0, tk.END)

            # Create the group's textbox if it doesn't exist
            # if not group["textbox"]:
            #    group["textbox"] = tk.Text(self.animals_frame, height=4, width=60)
            #    group["textbox"].pack()

            # Display the animal's information in the same line in the textbox
            # group["textbox"].insert(tk.END, f"Animal ID: {animal['id']} | ")
            # group["textbox"].insert(tk.END, f"Animal Box: {animal['box']} | ")
            # group["textbox"].insert(tk.END, f"Animal Weight: {animal['weight']} | ")
            # group["textbox"].insert(tk.END, f"Animal Sex: {animal['sex']} | ")
            # group["textbox"].insert(tk.END, "[Remove]\n")

        def remove_animal():
            if self.groups[group_name]:
                self.groups[group_name].pop()

        #     group["textbox"].delete("end-2l", "end-1l")  # Remove the last line from the textbox

        add_animal_button = tk.Button(animal_frame, text="Add to Group", command=add_animal)
        add_animal_button.pack(side="left", padx=5, pady=5)

        remove_animal_button = tk.Button(animal_frame, text="Remove from Group", command=remove_animal)
        remove_animal_button.pack(side="left", padx=5, pady=5)

        # By George
        # self.groups.append(group)

    def Done(self):
        # self.animal_group_window.withdraw()
        print(self.groups)



if __name__ == '__main__':
    animal_group_window = AnimalGroupWindow()
    # print(animal_group_window.groups[1] )