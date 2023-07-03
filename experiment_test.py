from Experiment import *
import datetime
import pytest

class TestExperiment:

    """
    Unit tests for the Experiment class.
    """
    path1 = "./test_data/test_data.rtf"
    path2 = "./test_data/test_data2.rtf"
    path3 = "./test_data/test_data3.rtf"
    path4 = "./test_data/test_data4.rtf"
    expected_results= "./test_data/expected_res.csv"

    my_date = datetime.date(2023, 6, 15)
    animal_1 = Animal(animal_id=2, sex="Male", weight={my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
    animal_1.add_session_to_animal(file_path=path1, session_number=1)
    animal_2 = Animal(animal_id=4, sex="Male", weight={my_date:250.5}, animal_box=4, animal_data=pd.DataFrame())
    animal_2.add_session_to_animal(file_path=path1, session_number=1)
    animal_3 = Animal(animal_id=1, sex="Female", weight={my_date:244.5}, animal_box=3, animal_data=pd.DataFrame())
    animal_3.add_session_to_animal(file_path=path3, session_number=1)

    # Test constractor with all parameters
    def test_init_full_params(self):
        assert Experiment(groups={}, name="PILOT", experimenters=["Tamar"])

    # Check if fails when group is not a dict
    def test_group_dict(self):
        with pytest.raises(ValueError):
            Experiment(groups=2, name="PILOT", experimenters=["Tamar"])

    # Check if fails when name is not a string
    def test_name_string(self):
        with pytest.raises(ValueError):
            Experiment(groups={}, name=555, experimenters=["Tamar"])

    # Check if fails when experimenters is a empty list
    def test_experimenters_empty_list(self):
        with pytest.raises(ValueError):
            Experiment(groups={}, name="PILOT", experimenters=[])

    # Check if fails when animals is not list 
    def test_add_animal_is_list(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        with pytest.raises(ValueError):
            new_experiment.add_animal(self.animal_1)

    # Check if fails when animal list is not instance of animal
    def test_add_animal_is_animal(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        with pytest.raises(ValueError):
            new_experiment.add_animal(["notanimal", self.animal_2, self.animal_3])

    # Check if fails when file path is not exists
    def test_path_not_exiss(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        new_experiment.add_animal([self.animal_1, self.animal_2, self.animal_3]) 
        with pytest.raises(FileNotFoundError):
            new_experiment.add_session(file_path="notpath", session_number=2)

    # Check if fails when session number is negative
    def test_session_number_negative(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        new_experiment.add_animal([self.animal_1, self.animal_2, self.animal_3])
        with pytest.raises(ValueError):
            new_experiment.add_session(file_path=self.path2, session_number=-2)
    
    # Check if fails when session number is float
    def test_session_number_float(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        new_experiment.add_animal([self.animal_1, self.animal_2, self.animal_3]) 
        with pytest.raises(ValueError):
            new_experiment.add_session(file_path=self.path3, session_number=2.0)

    # Check if fails when save path is not string
    def test_save_experimet_string(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        new_experiment.add_animal([self.animal_1, self.animal_2, self.animal_3]) 
        with pytest.raises(ValueError):
            new_experiment.save_experiment(000)

    # Check if fails when save path is not exists
    def test_save_experimet(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        new_experiment.add_animal([self.animal_1, self.animal_2, self.animal_3]) 
        with pytest.raises(FileNotFoundError):
            new_experiment.save_experiment("notpath")

    # Check if expected data equals to result
    def test_expected_results(self):
        new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
        new_experiment.add_animal([self.animal_1, self.animal_2, self.animal_3])
        new_experiment.update_experiment_data() 
        new_experiment.add_session(file_path=self.path2, session_number=2)
        example= new_experiment.experiment_data
        data= pd.read_csv(self.expected_results,index_col=0)
        example.to_csv("example.csv")
        data_example= pd.read_csv("example.csv", index_col=0)
        assert data.equals(data_example)


if __name__ == '__main__':
   
    e1= Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
    ttests = TestExperiment()
    methods = ["init_full_params","group_dict", "name_string",
               "experimenters_empty_list",
               "add_animal_is_list", "add_animal_is_animal",
               "path_not_exists", "session_number_negative","session_number_float",
               "save_experimet_string","save_experimet", "expected_results"]
    
    errors = []

    for method in methods:
        try:
            getattr(ttests, "test_" + method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")

    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")
