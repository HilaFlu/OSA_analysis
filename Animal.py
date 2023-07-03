#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: flomin
"""

from data_extraction import process_text_data
import pandas as pd
from pathlib import Path
import datetime
import os


class Animal:
    def __init__(self,
                 animal_id: int,
                 sex: str,
                 weight: dict,
                 animal_box: int,
                 animal_data: pd.DataFrame) -> None:
        """
        Initializes an instance of the Animal class.

        Parameters
        ----------
        animal_id: Integer
            The ID of the animal.
        sex: String
            The sex of the animal.
        weight: Dictionary
            A dictionary containing the weight data by date.
        animal_box: Integer
            The box number of the animal.
        animal_data: pd.DataFrame
            A DataFrame containing the animal data from each session.

        Raises
        ------
        ValueError:
            If any of the parameters are not the correct type or do not exist or don't match their description.
        """
        if animal_id is not None and not isinstance(animal_id, int) or animal_id < 0:
            raise ValueError("'animal_id' must be a positive integer.")

        if sex is not None and not isinstance(sex, str) or sex not in ["Male", "Female"]:
            raise ValueError("'sex' must be a string of either male or female.")

        if weight is not None and not isinstance(weight, dict):
            raise ValueError("'weight' must be a dictionary.")

        if animal_box is not None and not isinstance(animal_box, int):
            raise ValueError("'animal_box' must be an integer.")

        if animal_data is not None and not isinstance(animal_data, pd.DataFrame):
            raise ValueError("'animal_data' must be a DataFrame.")

        for date_weight in weight.keys():
            if not isinstance(date_weight, datetime.date):
                raise ValueError("Date should be datetime")
            if date_weight > datetime.datetime.now().date():
                raise ValueError("Date is in the future, should be in the past or present")

        for value_weight in weight.values():
            if value_weight < 0 or not isinstance(value_weight, float):
                raise ValueError("Weight must by float and has to be positive")

        self.animal_id = animal_id
        self.sex = sex
        self.weight = weight
        self.animal_box = animal_box
        self.animal_data = animal_data

    def add_session_to_animal(self,
                              file_path: str,
                              session_number: int) -> None:
        """
        Adds a session to the animal's data.

        Parameters
        ----------
        file_path: String
            The path to the text data file.
        session_number: Integer
            The session number.


        Raises
        ------
        ValueError:
            If 'file_path' is not a string or 'session_number' is not a positive integer.
        FileNotFoundError:
            If the file specified by 'file_path' does not exist.
        """
        if not isinstance(file_path, str) or not isinstance(session_number, int) or session_number <= 0:
            raise ValueError("'file_path' should be a string and 'session_number' should be an integer.")

        # Check if the file path exists
        if not Path(file_path).is_file():
            raise FileNotFoundError("File not found.")

        # Process the text data file to get the session DataFrame
        session_df = process_text_data(file_path)

        # Add a column called "session_number" with the given session number
        session_df["session_number"] = session_number

        # update session weight and sex
        weight = 0
        for weight_date in self.weight.keys():
            if weight_date <= session_df.loc[1, "Start Date"] < (weight_date + datetime.timedelta(days=7)):
                weight = self.weight[weight_date]
        session_df["weight"] = weight
        session_df["sex"] = self.sex
        session_df["animal_id"] = self.animal_id

        # Add only the row that matches the 'animal_box' parameter to 'animal_data'
        self.animal_data = pd.concat([self.animal_data, session_df.loc[[self.animal_box]]], ignore_index=True)

    def add_weight(self,
                   weight_date: datetime.datetime.date,
                   weight_value: float) -> None:
        """
        Adds weight data to the animal's weight dictionary.

        Parameters
        ----------
        weight_date: datetime.Date
            The date of the weight measurement.
        weight_value: Float
            The weight value.

        Raises
        ------
        ValueError:
            If 'weight_date' is not a date object from the past/present or 'weight_value' is not a positive float.
        """
        if not isinstance(weight_date, datetime.date):
            raise ValueError("'weight_date' must be a date object.")

        if not isinstance(weight_value, type(float)):
            raise ValueError("'weight_value' must be a float.")

        if self.weight is None:
            self.weight = {}

        self.weight[weight_date] = weight_value

    def save_animal(self, save_path: str) -> None:
        """
        This method saves the csv of the animal to a chosen folder.

        Parameters
        ----------
        save_path : string
            The path to the folder where it saves the csv.

        Raises
        ------
        ValueError:
            If 'file_path' is not a string.
        FileNotFoundError:
            If the folder specified by 'file_path' does not exist.

        Returns
        -------
        None
        """

        # Check if save_path is string
        if not isinstance(save_path, str):
            raise ValueError("'save_path' should be a string.")

        # Check if the save path exists
        if not os.path.isdir(save_path):
            raise FileNotFoundError("Folder not found.")

        self.animal_data.to_csv(os.path.join(save_path, "animal_" + str(self.animal_id) + ".csv"))
