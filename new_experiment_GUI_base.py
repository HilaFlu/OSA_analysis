import tkinter as tk
from Experiment_Data_Holder import ExperimentData
from load_data_file_base import LoadFileWindow


class CreateExperimentGUI:
    """A first window GUI for the experiment. In this GUI we initiallize the expiremnt and the user enters 
        the details of the experiment sush as Names of the researchers and the experiment name. This class takes a Experiment data instance to hold the variables after
        the GUI window is destroyed
        
        Two buttons : 
            1.Add researcher button - this will append the input to a list of researchers already initiallized
            2."Create new experiment" Button - this will print the name of the list of researchers and the experiment name in the Terminal
            before Destorying the current GUI window and openning a new GUI window called LoadFileWindow """
    def __init__(self, experiment_data):
        self.experiment_data = experiment_data

        self.create_exp_window = tk.Tk()
        self.create_exp_window.title("Start New Experiment")
        self.create_exp_window.geometry("400x400")

        self.experiment_name_label = tk.Label(self.create_exp_window, text="Experiment Name:")
        self.experiment_name_label.pack(pady=10)

        self.experiment_name_entry = tk.Entry(self.create_exp_window, width=30)
        self.experiment_name_entry.pack(pady=10)

        self.researcher_name_label = tk.Label(self.create_exp_window, text="Researcher Name:")
        self.researcher_name_label.pack(pady=10)

        self.researcher_name_entry = tk.Entry(self.create_exp_window, width=30)
        self.researcher_name_entry.pack(pady=10)

        self.add_button = tk.Button(self.create_exp_window, text="Add", command=self.add_researcher, bg="#e0e0e0",
                                    height=3, width=15)
        self.add_button.pack(pady=10)

        self.researchers_text = tk.StringVar()
        self.researchers_label = tk.Label(self.create_exp_window, textvariable=self.researchers_text)
        self.researchers_label.pack(pady=10)

        self.create_exp_button = tk.Button(self.create_exp_window, text="Create New Experiment",
                                           command=self.create_experiment, bg="#e0e0e0", height=3, width=20)
        self.create_exp_button.pack(pady=20)

        self.create_exp_window.mainloop()

    def add_researcher(self):
        """ command for the add researcher button to get the entry from the text box and append it to the experiment_data instance """
        researcher = self.researcher_name_entry.get()
        if researcher:
            self.experiment_data.add_researcher(researcher)
            self.researcher_name_entry.delete(0, tk.END)
            self.update_researchers_label()

    def update_researchers_label(self):
        researchers_str = ", ".join(self.experiment_data.get_researchers())
        self.researchers_text.set(researchers_str)

    def create_experiment(self):
        """command for the Start New Experiment Button.
        This button should also print out the names of the researchers and experiment name in the terminal.
        In addition to saving them in their respective __init__ variables in ExperimenData instance
        This button will also close this window and open a new window - Load File GUI"""
        self.experiment_data.set_experiment_name(self.experiment_name_entry.get())
        
        # Use the experiment name and researchers as variables for further processing
        experiment_name = self.experiment_data.get_experiment_name()
        researchers = self.experiment_data.get_researchers()
        print("New Experiment:", experiment_name)
        print("Researchers:", researchers)
       
        # Call your desired method/function with experiment name and researchers as inputs
        # Example: process_experiment(experiment_name, researchers)
        
        # print("New Experiment:", experiment_name)
        # print("Researchers:", researchers) 
        self.create_exp_window.destroy()
        load_file_window = LoadFileWindow(experiment_data)  # Open the load file window
        


if __name__ == '__main__':
    experiment_data = ExperimentData()
    create_exp_window = CreateExperimentGUI(experiment_data)
    print(experiment_data.researchers , experiment_data.exp_name , experiment_data.path , experiment_data.session_number)