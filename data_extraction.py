#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: flomin
"""

import pandas as pd
from datetime import datetime
from pathlib import Path


def process_text_data(file_path: str) -> pd.DataFrame:
    """
    This script takes a file containing the raw data generated from "Med-PC-IV"
    at the end of each session, converts the data into a data frame and returns
    it.

    Parameters
    ----------
    file_path : String
        File path of the text data file ment to be converted and analysed.


    Raises
    -------
    ValueError:
        If 'file_path' is not a string.
    FileNotFoundError:
        If the file specified by 'file_path' does not exist.

    Returns
    -------
    session_df : pd.DataFrame
        The data frame containing all of the data from the session, where each row
        represents a box and each column a data parameter.

    """

    # Check if file_path is indeed a string
    if not isinstance(file_path, str):
        raise ValueError("'file_path' should be a string and 'session_number' should be an integer.")

    # Check if the file path exists
    if not Path(file_path).is_file():
        raise FileNotFoundError("File not found.")

    # Dictionary with values of plan 1
    parameters_fr1_60 = {"E": "rewards", "R": "right_lever", "M": "head", "S": "minutes",
                         "B": "times_of_rlever", "C": "times_of_reward",
                         "D": "times_of_head", "L": "left_lever",
                         "A": "times_of_llever"}

    # Dictionary with values of plan 2
    parameters_fr1_night = {"M": "rewards", "J": "right_lever", "O": "rewards", "T": "seconds",
                            "F": "times_of_rlever", "N": "times_of_reward",
                            "G": "right_lever", "D": "left_lever",
                            "C": "times_of_llever", "K": "left_lever"}

    # Read the text data file
    file_path = Path(file_path)
    with file_path.open('r') as file:
        data = file.read()

    # Split the data for each box
    box_data = data.split('\n\n')
    box_data = box_data[2:]

    # Initialize an empty dictionary to store box data
    box_dict = {}

    # Process data for each box
    for box in box_data:
        box_lines = box.strip().split('\n')
        box_lines = list(filter(lambda x: x != "\\", box_lines))
        box_lines = list(filter(lambda x: x != "}", box_lines))

        # Initialize empty lists to store parameter values
        parameters = dict()
        last_key = ""

        # Match the plan to the inserted raw data file
        if "MSN: Rat_FR1-60" in box_lines:
            parameter_names = parameters_fr1_60
        elif "MSN: Rat_FR1_night_Ronly" in box_lines or "MSN: Rat_FR1_night" in box_lines:
            parameter_names = parameters_fr1_night
        else:
            parameter_names = dict()

        # Go over each pramater and add it as the right type to the df
        for line in box_lines:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Replace unwanted keys from the raw data with the wanted key from parameter_names
            if key in parameter_names.keys():
                key = parameter_names[key]

            # Make sure sub-parameters are not listed as main parameters
            is_list = False
            if key.isnumeric():
                key = last_key
                is_list = True
            else:
                last_key = key

            if 'Date' in key:
                # Convert date to datetime object
                parameters[key] = datetime.strptime(value, '%m/%d/%y').date()
            elif "Time" in key:
                # Convert time to datetime object
                parameters[key] = datetime.strptime(value, '%H:%M:%S').time()
            elif key == "Box":
                parameters[key] = int(value)
            elif (value.isalpha() and len(value.split()) == 1) or key == "MSN" or key == "Subject":
                parameters[key] = str(value)
            elif value == "":
                parameters[key] = 0
            elif is_list:
                if key in parameters.keys() and type(parameters[key]) == list and sum(
                        float(x) for x in value.split()) > 0:
                    # Convert values parameters containing several items into a list
                    parameters[key].extend([float(x) for x in value.split()])
                elif sum(float(x) for x in value.split()) > 0:
                    # Convert values parameters containing several items into
                    # a list, if they are the first values inserted to the parameter
                    parameters[key] = [float(x) for x in value.split()]
                else:
                    parameters[key] = []
            else:
                parameters[key] = float(value)

        box_dict[parameters["Box"]] = parameters

    # Convert dictionary to pandas DataFrame
    session_df = pd.DataFrame.from_dict(box_dict, orient='index')

    return session_df


