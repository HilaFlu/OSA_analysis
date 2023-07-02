# running the whole process - the main func

from animal_group_gui import *
from group_GUI import *
from Animal import *
from Experiment import *
from Experiment_Data_Holder import *
from load_data_file_base import *
from data_extraction import *
from new_experiment_GUI_base import *


def process():    
    # step 1 - create a workspace 
    experiment = ExperimentData()

    # step 2 - initialize
    create_exp_window = CreateExperimentGUI(experiment)

    # step 3 - creat groups 
    animal_group_window = AnimalGroupWindow()
    GROUPS = animal_group_window.get_groups()
    experiment.set_groups(GROUPS)

    # step 4 - load files
    experiment = LoadFileWindow(experiment)  # Open the load file window

    # step 5 - analyze the data using different graphs and functions with the GUI
    gui = Show_Analysis(experiment=experiment)
    gui.run()

if __name__ == '__main__':
    process()




