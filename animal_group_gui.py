# Final GUI
# Presentes both the analysis of the animals and of the groups

from data_extraction import process_text_data
import tkinter as tk
from tkinter import messagebox
from experiment_analysis import *
from animal_analysis import *
from gui_data_frame import *



class Show_Analysis:
    def __init__(self, experiment: GUI_DataFrame):

        # in order to save the graphs from the gui for usement after closing the gui
        self.graphs = {}

        self.experiment = experiment
        self.root = tk.Tk()
        self.root.title("Animal and Group Analysis Functions")
        self.root.geometry("450x450")
        
        # Create a variable to hold the selected option (Animal or Group)
        self.selected_option = tk.StringVar()
        
        # Create Radio buttons for Animal and Group
        self.animal_radio = tk.Radiobutton(self.root, text="Animal", variable=self.selected_option, value="Animal", command=self.show_animal_buttons)
        self.animal_radio.grid(row=0, column=0, padx=10, pady=10)
        
        self.group_radio = tk.Radiobutton(self.root, text="Group", variable=self.selected_option, value="Group", command=self.show_group_buttons)
        self.group_radio.grid(row=0, column=1, padx=10, pady=10)
        
        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
    def show_animal_buttons(self):
        # Clear the button frame
        self.clear_button_frame()

        # Create buttons for Animal 
        self.button4 = tk.Button(self.button_frame, text="total alcohol intake", command=self.total_alcohol_intake_gui())
        self.button4.pack(side="left", padx=5)

        self.button5 = tk.Button(self.button_frame, text="total of general index", command=self.total_of_general_index_gui())
        self.button5.pack(side="left", padx=5)

        self.button6 = tk.Button(self.button_frame, text="avg lever presses", command=self.avg_lever_presses_gui())
        self.button6.pack(side="left", padx=5)

    
    def show_group_buttons(self):
        # Clear the button frame
        self.clear_button_frame()
        
        # Create options menu for gender selection
        self.gender_var = tk.StringVar()
        self.gender_var.set("All_Genders")
        self.gender_options = ["All_Genders", "Female", "Male"]
        self.gender_menu = tk.OptionMenu(self.button_frame, self.gender_var, *self.gender_options)
        self.gender_menu.pack(side="left", padx=5)

        # Create options menu for metric selection
        self.metric_choice = tk.StringVar()
        self.metric_choice.set("head")
        self.metric_options = ["rewards", "head", "left_lever", "right_lever"]
        self.metric_menu = tk.OptionMenu(self.button_frame, self.metric_choice, *self.metric_options)
        self.metric_menu.pack(side="left", padx=5)
        
        # Create buttons for Group functions
        self.button1 = tk.Button(self.button_frame, text="Plot Average Intake", command=self.plot_avg_intake_gui())
        self.button1.pack(side="left", padx=5)
        
        self.button2 = tk.Button(self.button_frame, text="Plot Metric per Session", command=self.plot_metric_per_session_gui())
        self.button2.pack(side="left", padx=5)

        self.button3 = tk.Button(self.button_frame, text="Plot Group Presses", command=self.plot_group_presses_gui())
        self.button3.pack(side="left", padx=5)

        self.button7 = tk.Button(self.button_frame, text="avg alcohol intake by group", command=self.avg_alcohol_intake_by_group_gui())
        self.button7.pack(side="left", padx=5)

        
    
    def clear_button_frame(self):
        # Clear all buttons from the button frame
        for widget in self.button_frame.winfo_children():
            widget.pack_forget()
        
    def total_alcohol_intake_gui(self):
        messagebox.showinfo("Function", f"Total alcohol intake for {self.selected_option.get()}")
        plot_and_save_total_alcohol_intake()
    
    def total_of_general_index_gui(self):
        messagebox.showinfo("Function", f"Total of general index {self.selected_option.get()}")

    def avg_lever_presses_gui(self):
        messagebox.showinfo("Function", f"Average lever presses for {self.selected_option.get()}")


    def plot_avg_intake_gui(self):
        selected_gender = self.gender_var.get()
        messagebox.showinfo("Function", f"Plot Average Intake for {self.selected_option.get()} ({selected_gender})")
        # Call the plot_avg_intake function with the selected gender
        plot_avg_intake(self.experiment, groups=self.experiment.groups, sex=selected_gender)

    def plot_metric_per_session(self):
        selected_gender = self.gender_var.get()
        metric = self.metric_choice.get()
        messagebox.showinfo("Function", f"Plot Metric per Session for {self.selected_option.get()}")
        plot_metric_per_session(self.experiment, groups=self.experiment.groups, metric=metric , sex=selected_gender)

    def plot_group_presses_gui(self):
        messagebox.showinfo("Function", f"Plot Group Presses for {self.selected_option.get()}")
        plot_group_presses(self.experiment, groups=self.experiment.groups)

    def avg_alcohol_intake_by_group_gui(self):
        messagebox.showinfo("Function", f"Average alchohol intake by group for {self.selected_option.get()}")
        plot_avg_alcohol_intake_by_group(self.experiment, groups=self.experiment.groups)

    def run(self):
        self.root.mainloop()

# Create an instance of the GUI and run it
data_gui = GUI_DataFrame("insert needed values")
gui = Show_Analysis()
gui.run()