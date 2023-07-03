from Animal import Animal
import pandas as pd
from Experiment import Experiment
from data_extraction import process_text_data
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime
from animal_analysis import plot_and_save_alcohol_intake_per_session, plot_and_save_total_alcohol_intake, plot_and_save_total_of_general_index, plot_and_save_avg_lever_presses, plot_avg_alcohol_intake_by_group
from experiment_analysis import plot_group_presses, plot_avg_intake, plot_metric_per_session
import pytest


class TestAnalysis:
    """
    Unit tests for the analysis class.
    """
    path1 = "./test_data/test_data.rtf"
    path2 = "./test_data/test_data2.rtf"
    path3 = "./test_data/test_data3.rtf"
    path4 = "./test_data/test_data4.rtf"
    my_date = datetime.date(2023, 6, 15)
    animal_1 = Animal(animal_id=2, sex="Male", weight={my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
    animal_1.add_session_to_animal(file_path=path1, session_number=1)
    animal_2 = Animal(animal_id=4, sex="Male", weight={my_date:250.5}, animal_box=4, animal_data=pd.DataFrame())
    animal_2.add_session_to_animal(file_path=path1, session_number=1)
    animal_3 = Animal(animal_id=1, sex="Female", weight={my_date:244.5}, animal_box=3, animal_data=pd.DataFrame())
    animal_3.add_session_to_animal(file_path=path3, session_number=1)
    example1 = animal_1.animal_data
    example2 = animal_2.animal_data
    example3 = animal_3.animal_data
    new_experiment = Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
    new_experiment.add_animal([animal_1, animal_2, animal_3])
    new_experiment.update_experiment_data()
    example4 = new_experiment
    new_experiment.add_experimenter("Daniel")
    new_experiment.add_session(file_path=path2, session_number=2)
    example5= new_experiment

    graph_png_path = "." 
    session_number = 1  # replace with the desired session number

    new_experiment.save_experiment(graph_png_path)
    animal_2.save_animal(graph_png_path)

    # F1 Check if fails when getting not an animal object
    def test_plot_total_alcohol_intake_animal_isanimal(self):
         with pytest.raises(ValueError):
                plot_and_save_total_alcohol_intake("notanimal", self.graph_png_path)
    

    # F1 Check if fails when path not a string
    def test_plot_total_alcohol_intake_path_string(self):
         with pytest.raises(ValueError):
                plot_and_save_total_alcohol_intake(self.animal_3, 333)
    
    #F1 Check if fails when path not exists
    def test_plot_total_alcohol_intake_path_exists(self):
         with pytest.raises(ValueError):
                plot_and_save_total_alcohol_intake(self.animal_3, "notpath")

    # F2 Check if fails when getting not an animal object
    def test_plot_alcohol_intake_person_animal_isanimal(self):
         with pytest.raises(ValueError):
                plot_and_save_alcohol_intake_per_session("animal", self.session_number, self.graph_png_path)
    

    # F2 Check if fails when session number not int
    def test_plot_alcohol_person_intake_session_int(self):
         with pytest.raises(ValueError):
                plot_and_save_alcohol_intake_per_session(self.animal_1, 55.5, self.graph_png_path)
     
     #F2 Check if fails when session number negative
    def test_plot_alcohol_person_intake_session_negative(self):
         with pytest.raises(ValueError):
                plot_and_save_alcohol_intake_per_session(self.animal_1, -4, self.graph_png_path)
    

    # F2 Check if fails when path not string
    def test_plot_alcohol_person_intake_path_string(self):
         with pytest.raises(ValueError):
                plot_and_save_alcohol_intake_per_session(self.animal_1, self.session_number, 555)
    
    #F2 Check if fails when path not exists
    def test_plot_alcohol_intake_person_path_exists(self):
         with pytest.raises(ValueError):
                plot_and_save_alcohol_intake_per_session(self.animal_1, self.session_number, "notpath")


    # F3 Check if fails when getting not an animal object
    def test_plot_total_of_general_index_animal_isanimal(self):
         with pytest.raises(ValueError):
            plot_and_save_total_of_general_index("animal", 'head', self.graph_png_path)

    # F3 Check if fails when path not string
    def test_plot_total_of_general_index_path_string(self):
         with pytest.raises(ValueError):
             plot_and_save_total_of_general_index(self.animal_1, 'head', 555)
    
    #F3 Check if fails when path not exists
    def test_plot_total_of_general_index_path_exists(self):
         with pytest.raises(ValueError):
               plot_and_save_total_of_general_index(self.animal_1, 'head', "notpath")

    #F3 Check if fails when measurement not exists
    def test_plot_total_of_general_index_path_exists(self):
         with pytest.raises(ValueError):
               plot_and_save_total_of_general_index(self.animal_1, "tahat", self.graph_png_path)


    #F4 Check if fails when getting not an animal object
    def test_plot_and_save_avg_lever_presses_is_exp(self):
         with pytest.raises(ValueError):
            plot_and_save_avg_lever_presses("dani", self.graph_png_path)

  
    #F4 Check if fails when is path is not string
    def test_lot_and_save_avg_lever_presses_path_string(self):
         with pytest.raises(ValueError):
             plot_and_save_avg_lever_presses(self.animal_1, 555)
          
    #F4 Check if fails when is path is not exists
    def test_lot_and_save_avg_lever_presses_path_exists(self):
         with pytest.raises(ValueError):
            plot_and_save_avg_lever_presses(self.animal_1, "555")

    # Test for experiment analysis 
   
    #F5 Check if fails when group is not list 
    def test_plot_avg_intake_is_group(self):
         with pytest.raises(ValueError):
            plot_avg_intake(self.example5, 77, sex='Female', save_path=self.graph_png_path)
    
    #F5 Check if fails when sex is not string 
    def test_plot_avg_intake_sex_string(self):
         with pytest.raises(ValueError):
            plot_avg_intake(self.example5, groups=[1, 2], sex=55, save_path=self.graph_png_path)
    
    #F5 Check if fails when is not proper sex 
    def test_plot_avg_intake_proper_sex(self):
         with pytest.raises(ValueError):
            plot_avg_intake(self.example5, groups=[1, 2], sex='hamor', save_path=self.graph_png_path)
    
    #F5 Check if fails when is path is not string
    def test_plot_avg_intake_path_string(self):
         with pytest.raises(ValueError):
            plot_avg_intake(self.example5, groups=[1, 2], sex='Female', save_path=555)

    #F5 Check if fails when is path is not exists
    def test_plot_avg_intake_path_exists(self):
         with pytest.raises(ValueError):
            plot_avg_intake(self.example5, groups=[1, 2], sex='Female', save_path="555")

    
    #F6 Check if fails when group is not list 
    def test_plot_metric_per_session_is_list(self):
         with pytest.raises(ValueError):
            plot_metric_per_session(self.example5, "[1, 2]", 'head', save_path=self.graph_png_path)
    
    #F6 Check if fails when metric is not exists 
    def test_plot_metric_per_session_is_matric(self):
         with pytest.raises(ValueError):
            plot_metric_per_session(self.example5, [1, 2], 'tahat', save_path=self.graph_png_path)
    
    
    #F6 Check if fails when is path is not string
    def test_plot_metric_per_session_path_string(self):
         with pytest.raises(ValueError):
            plot_metric_per_session(self.example5, [1, 2], 'head', save_path=555)

    #F6 Check if fails when is path is not exists
    def test_plot_metric_per_session_path_exists(self):
         with pytest.raises(ValueError):
            plot_metric_per_session(self.example5, [1, 2], 'head', save_path="555")

    
    #F7 Check if fails when group is not list 
    def test_plot_group_presses_group_list(self):
         with pytest.raises(ValueError):
            plot_group_presses(self.example5, groups=99, save_path=self.graph_png_path)
          
    #F7 Check if fails when is path is not string
    def test_plot_group_presses_path_string(self):
         with pytest.raises(ValueError):
            plot_group_presses(self.example5, groups=[1, 2], save_path=77)
          
    #F7 Check if fails when is path is not exists
    def test_plot_group_presses_path_exists(self):
         with pytest.raises(ValueError):
            plot_group_presses(self.example5, groups=[1, 2], save_path="77")
          


if __name__ == '__main__':
    
    e1= Experiment(groups={}, name="PILOT", experimenters=["Tamar"])
    ttests = TestAnalysis()
    methods = ["plot_total_alcohol_intake_animal_isanimal", "plot_total_alcohol_intake_path_string", "plot_total_alcohol_intake_path_exists", 
               "plot_alcohol_intake_person_animal_isanimal", "plot_alcohol_person_intake_session_int", "plot_alcohol_person_intake_session_negative", "plot_alcohol_person_intake_path_string", "plot_alcohol_intake_person_path_exists",
                "plot_total_of_general_index_animal_isanimal", "plot_total_of_general_index_path_string", "plot_total_of_general_index_path_exists","plot_total_of_general_index_path_exists",
                "plot_and_save_avg_lever_presses_is_exp", "plot_and_save_avg_lever_presses_path_string", "lot_and_save_avg_lever_presses_path_exists",
                 "plot_avg_intake_is_group", "plot_avg_intake_sex_string", "plot_avg_intake_proper_sex", "plot_avg_intake_path_string", "plot_avg_intake_path_exists",
                "plot_metric_per_session_is_list", "plot_metric_per_session_is_matric", "plot_metric_per_session_path_string", "plot_metric_per_session_path_exists"
                ,"plot_group_presses_group_list", "plot_group_presses_path_string", "plot_group_presses_path_exists"
               ]
    
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
