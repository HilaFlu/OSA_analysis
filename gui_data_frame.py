# The database that the GUI can interface with 

from Animal import *
from Experiment import *
from animal_analysis import *
from experiment_analysis import *
from Load_Data_File_Base import *
from New_Experiment_GUI_Base import *


# using this file, we create a new data frame that the GUI can interface with
# The first step is initializing the data base, creating a new experiment (by the user in the GUI)
# After the initialization, using the methodes in the project, we fill the other parameters
# Last, we can now analyze the data of the experiment using the GUI  

class GUI_DataFrame():
    def __init__(self, 
                 experiment_name: str, 
                 Animals: list[Animal], 
                 base_data: pd.DataFrame) -> None:
        

