import tkinter as tk
from tkinter import ttk

GROUPS = []

class AnimalGroupWindow:
    """This GUI's purpose is to allow the User to create groups of animals,
    and input the details of each animal, in addition to adding animals as needed.
    Variables are :
    1. Animal id
    2. Animal box
    3. weight
    4. Animal sex (Male/Female)
    
    the groups are saved in a dictionary with the group name as the key and the animals as values
    """
    def __init__(self):
        self.groups = []

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

        self.animal_group_window.mainloop()

    def add_group(self):
        group_name = self.group_name_entry.get()
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

        animal_sex_label = tk.Label(animal_frame, text="Animal Sex:")
        animal_sex_label.pack(side="left", padx=5, pady=3)

        animal_sex_label = tk.Label(animal_frame)
        animal_sex_combobox = ttk.Combobox(animal_frame, values=["", "Male", "Female"])
    
        animal_sex_label.pack()
        animal_sex_combobox .pack(side="left", padx=5, pady=5)
        # animal_sex_entry = tk.Entry(animal_frame, width=10)
        # animal_sex_entry.pack(side="left", padx=5, pady=5)

        group = {
            "name": group_name,
            "animals": [],
            "textbox": None  # Placeholder for the group's textbox
        }

        def add_animal():
            """allows to add another animal to the desired group"""
            animal = {
                "id": animal_id_entry.get(),
                "box": animal_box_entry.get(),
                "weight": animal_weight_entry.get(),
                "sex": animal_sex_combobox.get()
            }
            group["animals"].append(animal)

            animal_id_entry.delete(0, tk.END)
            animal_box_entry.delete(0, tk.END)
            animal_weight_entry.delete(0, tk.END)
            animal_sex_combobox.delete(0, tk.END)

            # Create the group's textbox if it doesn't exist
            if not group["textbox"]:
                group["textbox"] = tk.Text(self.animals_frame, height=4, width=60)
                group["textbox"].pack()

            # Display the animal's information in the same line in the textbox
            group["textbox"].insert(tk.END, f"Animal ID: {animal['id']} | ")
            group["textbox"].insert(tk.END, f"Animal Box: {animal['box']} | ")
            group["textbox"].insert(tk.END, f"Animal Weight: {animal['weight']} | ")
            group["textbox"].insert(tk.END, f"Animal Sex: {animal['sex']} | ")
            group["textbox"].insert(tk.END, "[Remove]\n")

        def remove_animal():
            """In case of wrong input and submission of animal, the user can remove the animal,
            and retype the variables accordingly"""
            if group["animals"]:
                group["animals"].pop()
                group["textbox"].delete("end-2l", "end-1l")  # Remove the last line from the textbox
        
        
        ##Add Animal Button setup
        add_animal_button = tk.Button(animal_frame, text="Add to Group", command=add_animal)
        add_animal_button.pack(side="left", padx=5, pady=5)
        ##remove Animal Button setup
        remove_animal_button = tk.Button(animal_frame, text="Remove from Group", command=remove_animal)
        remove_animal_button.pack(side="left", padx=5, pady=5)

        self.groups.append(group)

    def get_groups(self):
        return self.groups

if __name__ == '__main__':
    animal_group_window = AnimalGroupWindow()
