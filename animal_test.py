from Animal import *
import datetime
import pytest
import pandas as pd

class TestAnimal:
    """
    Unit tests for the Animal class.
    """
    path1 = "./test_data/test_data.rtf"
    path2 = "./test_data/test_data2.rtf"
    path3 = "./test_data/test_data3.rtf"
    path4 = "./test_data/test_data4.rtf"
    path5= "./test_data/populations.txt"
    my_date = datetime.date(2023, 6, 15)

    # Test constractor with all parameters
    def test_init_full_params(self):
        assert Animal(animal_id=1, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
     
    # Should Fail : Animal_id type is int
    def test_id_integer(self): 
        with pytest.raises(ValueError):
            Animal(animal_id=1.5, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())

    # Test that negative animal_id fails
    def test_id_negative(self):
        with pytest.raises(ValueError):
            Animal(animal_id=-2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())

    # Test that not string sex fail
    def test_string_sex(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex=123, weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())

    # Test that not proper sex fail (Female or Male : string)
    def test_proper_sex(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Hamor", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
    
 # Check if fails when weight is not dictionary
    def test_weight_dict(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Male", weight=55, animal_box=2, animal_data=pd.DataFrame())

    # Check if fails or set a default value to 0?
    def test_weight_negative(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Male", weight={self.my_date:-230.5}, animal_box=2, animal_data=pd.DataFrame())
    
    # Check if fails when weight is not float?
    def test_weight_float(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Male", weight={self.my_date:230}, animal_box=2, animal_data=pd.DataFrame())
    
    # Check if fail when date is in the future
    def test_future_date(self):
        future_date = datetime.date(2025, 6, 15)
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Male", weight={future_date:230.5}, animal_box=2, animal_data=pd.DataFrame())

    # Check if fail  when date is not datetime
    def test_datetime_date(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Male", weight={33:230.5}, animal_box=2, animal_data=pd.DataFrame())

    # Check if fails when animal data is not df
    def test_animal_data_df(self):
        with pytest.raises(ValueError):
            Animal(animal_id=1, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=6)

    # Check if fails when file path is not string
    def test_session_path_string(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(ValueError) as e_info:
            animal_1.add_session_to_animal(file_path=555, session_number=1)

    # Check if fails when file path is not exist
    def test_file_exist(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(FileNotFoundError):
            animal_1.add_session_to_animal(file_path="tamar", session_number=1)

    # Check if fails when file path is not string----------
    def test_session_path_string(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(ValueError):
            animal_1.add_session_to_animal(file_path=555, session_number=1)

   # Check if fails when session_number is not int
    def test_session_number_int(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(ValueError):
            animal_1.add_session_to_animal(file_path=self.path1, session_number=1.2)
   
   # Check if fails when session_number value <= 0 
    def test_session_number_negative(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(ValueError):
            animal_1.add_session_to_animal(file_path=self.path1, session_number=-555)

    # Check if fails when add not float weight
    def test_add_weight_float(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(ValueError):
            animal_1.add_weight(self.my_date, "55")

    # Check if fails when path not string
    def test_save_path_string(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(ValueError):
            animal_1.save_animal(555)

     # Check if fails when path not exists
    def test_save_path_exists(self):
        animal_1 = Animal(animal_id=2, sex="Male", weight={self.my_date:230.5}, animal_box=2, animal_data=pd.DataFrame())
        with pytest.raises(FileNotFoundError):
            animal_1.save_animal("notpath")
            
if __name__ == '__main__':
    ttests = TestAnimal()
    methods = ["init_full_params",
               "id_negative" ,"id_integer",
                "string_sex", "proper_sex",
               "weight_dict","weight_negative","weight_float",
               "future_date", "datetime_date"
               "animal_data_df","session_path_string", 
               "session_number_int", "session_number_negative",
               "add_weight_float", "save_path_string" , "save_path_exists"]
    
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
