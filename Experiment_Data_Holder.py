# The database that the GUI can interface with 

from Animal import *
from Experiment import *
from animal_analysis import *
from experiment_analysis import *

# using this file, we create a new data frame that the GUI can interface with
# The first step is initializing the data base, creating a new experiment (by the user in the GUI)
# After the initialization, using the methodes in the project, we fill the other parameters
# Last, we can now analyze the data of the experiment using the GUI  


class ExperimentData:
    """This class will be used to store valubale data across GUI to be reused after windows are destroyed.
        This class will hold multiple values to be used as inputs
        From the Create New experiemnt GUI will load the list of names of researchers and the Experiment Name
        and from the second GUI window - Load file - it will hold the session number the user submitted and the path of the file."""
        
    def __init__(self):
        
        self.exp_name = ""
        self.researchers = []
        self.path = ""
        self.groups = []

    def set_experiment_name(self, exp_name):
        self.exp_name = exp_name

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def set_groups(self, groups):
        self.groups = groups
    
    def creating_experiment_after_receiving_data(self):
        self.experiment = Experiment(groups=self.groups, name=self.exp_name, experimenters=self.researchers)

    def add_session(self, file_path, session_number):
        self.experiment.add_session(file_path=file_path, session_number=session_number)

    def load_sess_path(self, sess_path):
        self.path = sess_path 

    def get_experiment_name(self):
        return self.exp_name

    def get_researchers(self):
        return self.researchers
        

