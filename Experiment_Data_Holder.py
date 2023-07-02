class ExperimentData:
    """This class will be used to store valubale data across GUI to be reused after windows are destroyed.
        This class will hold multiple values to be used as inputs
        From the Create New experiemnt GUI will load the list of names of researchers and the Experiment Name
        and from the second GUI window - Load file - it will hold the session number the user submitted and the path of the file."""
        
    def __init__(self):
        
        self.exp_name = ""
        self.researchers = []
        self.path = ""
        self.session_number = ""

    def set_experiment_name(self, exp_name):
        self.exp_name = exp_name

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def load_session_number(self, session_number):
        self.session_number = session_number

    def load_sess_path(self, sess_path):
        self.path = sess_path

    def get_experiment_name(self):
        return self.exp_name

    def get_researchers(self):
        return self.researchers
