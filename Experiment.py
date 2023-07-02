#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: flomin
"""

from Animal import Animal
import pandas as pd
from data_extraction import process_text_data
from pathlib import Path
from datetime import timedelta
import os


class Experiment:
    def __init__(self,
                 groups: dict,
                 name: str,
                 experimenters: list) -> None:
        """
        Initializes an instance of the Experiment class.

        Parameters
        ----------
        groups: Dictionary of lists
            A dictionary of lists representing animal groups.
        name: String
            The name of the experiment.
        experimenters: List
            A list of experimenters' names.
        parameters_dict: Dictionary
            A dictionary with the raw data parameters as keys and actual
            parameters as values

        Raises
        ------
        ValueError:
            If any of the parameters are not the correct type or do not exist.
        """
        if not isinstance(groups, dict):
            raise ValueError("'groups' must be a dictionary.")

        if not isinstance(name, str):
            raise ValueError("'name' must be a string.")

        if not isinstance(experimenters, list):
            raise ValueError("'experimenters' must be a list.")

        self.name = name
        self.groups = groups
        self.experimenters = experimenters
        self.experiment_data = pd.DataFrame()

    def add_animal(self,
                   animals: list) -> None:
        """
        Adds Animal objects from list to the appropriate group.

        Parameters
        ----------
        animals: list
            A list of Animal objects.

        Raises
        ------
        ValueError:
            If 'animal' is not an instance of the Animal class.
        """
        if not isinstance(animals, list):
            raise ValueError("'animals' must be an instance of list.")

        for animal in animals:
            if not isinstance(animal, Animal):
                raise ValueError("'animal' must be an instance of class Animal.")

            group_key = animal.animal_data.loc[:, "Group"].iloc[0]
            if group_key in self.groups.keys():
                self.groups[group_key].append(animal)
            else:
                self.groups[group_key] = [animal]

    def add_session(self,
                    file_path: str,
                    session_number: int) -> None:
        """
        Adds a session to the appropriate group's animals.

        Parameters
        ----------
        file_path: String
            The path to the text data file.
        session_number: Integer
            The session number.

        Raises
        ------
        ValueError:
            If 'file_path' is not a string or 'session_number' is not an integer.
        FileNotFoundError:
            If the file specified by 'file_path' does not exist.
        ValueError:
            If the experimental group specified in the session does not exist.
        """
        if not isinstance(file_path, str) or not isinstance(session_number, int):
            raise ValueError("'file_path' should be a string and 'session_number' should be an integer.")

        # Check if the file path exists
        if not Path(file_path).is_file():
            raise FileNotFoundError("File not found.")

        # Process the text data file to get the session DataFrame
        session_df = process_text_data(file_path)

        # Get the 'Group' value from the first row of the session DataFrame
        group_key = session_df.loc[1, 'Group']

        # Check if the experimental group exists
        if group_key not in self.groups:
            raise ValueError("Experimental group doesn't exist.")

        # Add the session number as a column to the session DataFrame
        session_df['session_number'] = session_number

        # Update the animal_data of each animal in the group
        for animal in self.groups[group_key]:
            # update session weight and sex
            weight = 0
            for weight_date in animal.weight.keys():
                if weight_date <= session_df.loc[1, "Start Date"] < (weight_date + timedelta(days=7)):
                    weight = animal.weight[weight_date]
            session_df["weight"] = weight
            session_df["sex"] = animal.sex
            session_df["animal_id"] = animal.animal_id
            row = session_df.loc[[animal.animal_box]]
            row.set_index('session_number', inplace=True, drop=False)
            animal.animal_data = pd.concat([animal.animal_data, row], ignore_index=True)

        self.update_experiment_data()

    def update_experiment_data(self) -> None:
        """
        Updates the experiment data DataFrame.

        Returns
        ------
        None
        """
        experiment_data = pd.DataFrame()

        for group_key, animals in self.groups.items():
            for animal in animals:
                if not animal.animal_data.empty:
                    animal_data = animal.animal_data
                    experiment_data = pd.concat([experiment_data, animal_data])

        self.experiment_data = experiment_data

    def add_experimenter(self,
                         experimenter: str) -> None:
        """
        Adds an experimenter to the list of experimenters.

        Parameters
        ----------
        experimenter: string
            The name of the experimenter.

        Raises
        ------
        ValueError:
            If 'experimenter' is not a string.
        """
        if not isinstance(experimenter, str):
            raise ValueError("'experimenter' must be a string.")

        self.experimenters.append(experimenter)

    def save_experiment(self, save_path: str) -> None:
        """
        This method saves the csv of the experiment to a chosen folder.

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

        save_path = '/Users/flomin/Desktop/Personal/python_class/final_project/tamar_update'

        self.experiment_data.to_csv(os.path.join(save_path, "experiment_data.csv"))
