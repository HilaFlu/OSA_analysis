"""
This file holds functions for an animal related analysys
Written by: Tamar Gordon
"""

from Animal import Animal
from data_extraction import process_text_data
import matplotlib.pyplot as plt
import numpy as np
import os

# A few notes:
# To use each of the functions below, see how it was used in the tests document


# F1: This function plots the alcohol intake for a specific animal in each session
# def plot_and_save_total_alcohol_intake(animal, weight_dict, path):
def plot_and_save_total_alcohol_intake(animal: Animal, weight_dict: dict, path: str) -> None:

    """
    Plots the total alcohol intake for a specific animal in each session and saves the plot.

    Parameters
    ----------
    animal : Animal
        The animal object.
    weight_dict : Dict
        A dictionary containing the weights of the animal.
    path : str
        The path where the plot will be saved.

    Returns
    -------
    None
    """
    # Validate animal
    if not isinstance(animal, Animal):
        raise ValueError("Error: animal should be an instance of Animal class.")

    # Validate weight_dict
    if not isinstance(weight_dict, dict):
        raise ValueError("Error: weight_dict should be a dictionary.")

    # Validate path
    if not isinstance(path, str):
        raise ValueError("Error: path should be a string.")
    
    if not os.path.exists(path):
        raise ValueError("Error: The provided path does not exist.")

    df=animal.animal_data
    # extract the most recent weight
    most_recent_date = max(weight_dict.keys())
    animal_weight = weight_dict[most_recent_date]

    # calculate total alcohol intake per session
    total_alcohol_intake = ((0.1 * df['rewards']) / animal_weight) * 1000 

    # session numbers for X-axis
    session_numbers = np.arange(1, len(df) + 1)

    plt.figure(figsize=(10,6))
    plt.plot(session_numbers, total_alcohol_intake, marker='o')
    plt.title(f'Total Alcohol Intake per Session for animal {animal.animal_id}')
    plt.xlabel('Session number')
    plt.ylabel('Total alcohol intake (g/kg)')
    
    # Set xticks to be only the whole numbers in the range of session numbers
    plt.xticks(np.arange(min(session_numbers), max(session_numbers)+1, 1.0))

    # Save the plot as a PNG file
    plt.savefig(os.path.join(path, 'total_alcohol_intake.png'))
    plt.close()  


#------------------------------------------------------------------------------------------------#

#F2: This function plots the alcohol intake over time for a specific animal in a given session
def plot_and_save_alcohol_intake_per_session(animal: Animal, weight_dict: dict, session_number: int, path: str) -> None:
    """
    Plots the total alcohol intake for a specific animal in each session and saves the plot.

    Parameters
    ----------
    animal : Animal
        The animal object.
    weight_dict : Dict
        A dictionary containing the weights of the animal.
    session_number : int
        The session number to plot.
    path : str
        The path where the plot will be saved.

    Returns
    -------
    None
    """    
    # Validate animal
    if not isinstance(animal, Animal):
        raise ValueError("Error: animal should be an instance of Animal class.")

    # Validate weight_dict
    if not isinstance(weight_dict, dict):
        raise ValueError("Error: weight_dict should be a dictionary.")

    # Validate session_number
    if not isinstance(session_number, int) or session_number <= 0:
        raise ValueError("Error: session_number should be a positive integer.")

    # Validate path
    if not isinstance(path, str):
        raise ValueError("Error: path should be a string.")

    if not os.path.exists(path):
        raise ValueError("Error: The provided path does not exist.")


    df=animal.animal_data
    # extract the most recent weight
    most_recent_date = max(weight_dict.keys())
    animal_weight = weight_dict[most_recent_date]

    # decrement session_number by 1 because indexing in Python starts from 0
    session_number -= 1

    if session_number < len(df):
        # convert reward times from seconds to minutes
        reward_times_minutes = np.array(df['times_of_llever'].iloc[session_number]) / 60

        # compute number of rewards per minute
        rewards_per_minute, _ = np.histogram(reward_times_minutes, bins=int(df['minutes'].iloc[session_number]))

        # calculate alcohol intake per minute
        alcohol_intake = ((0.1 * rewards_per_minute) / animal_weight) * 1000 

        # time points for each minute
        time_points = np.arange(len(alcohol_intake))

        plt.figure(figsize=(10,6))
        plt.plot(time_points, alcohol_intake)
        plt.title(f'Alcohol Intake per Minute for Session {session_number + 1} for animal {animal.animal_id}')
        plt.xlabel('Minutes')
        plt.ylabel('Alcohol intake (g/kg)')

        # Save the plot as a PNG file
        plt.savefig(os.path.join(path, f'alcohol_intake_session_{session_number + 1}.png'))
        plt.close()  # close the figure after saving to free up memory
    else:
        print(f"Session {session_number + 1} not found in the dataset.")



#------------------------------------------------------------------------------------------------#


#F3: This function plots chosen parameter for a specific animal in each session
def plot_and_save_total_of_general_index(animal: Animal, measurement: str, path: str) -> None:
    """
    Plots a specified parameter for a specific animal in each session and saves the plot.

    Parameters
    ----------
    animal : Animal
        The animal object.
    measurement : str
        The measurement to plot, one of "rewards", "right_lever", "head", or "left_lever".
    path : str
        The path where the plot will be saved.

    Returns
    -------
    None
    """

    # Validate animal
    if not isinstance(animal, Animal):
        raise ValueError("Error: animal should be an instance of Animal class.")
        
    # Validate measurement
    if not isinstance(measurement, str) or measurement == "":
        raise ValueError("Error: measurement should be a non-empty string.")

    # Validate path
    if not isinstance(path, str):
        raise ValueError("Error: path should be a string.")

    if not os.path.exists(path):
        raise ValueError("Error: The provided path does not exist.")


    df=animal.animal_data
    # dict to convert measurement to its corresponding column name in df
    measurement_to_column = {"rewards": "rewards", "right_lever": "right_lever", "head": "head", "left_lever": "left_lever"}

    # check if the input measurement is valid
    if measurement not in measurement_to_column:
        raise ValueError('measurement should be one of "rewards", "right_lever", "head", or "left_lever"')

    # convert measurement to its corresponding column name in df
    column_name = measurement_to_column[measurement]

    # calculate total per session
    total_measurement_per_session = df[column_name]

    # session numbers for X-axis
    session_numbers = np.arange(1, len(df) + 1)

    plt.figure(figsize=(10,6))
    plt.plot(session_numbers, total_measurement_per_session, marker='o')
    plt.title(f'Total: {measurement} per Session for animal {animal.animal_id}')
    plt.xlabel('Session number')
    plt.ylabel(f'Total {measurement}')
    
    # Set xticks to be only the whole numbers in the range of session numbers
    plt.xticks(np.arange(min(session_numbers), max(session_numbers)+1, 1.0))

    # Set Y-axis to start at 0
    plt.ylim(bottom=0)

    # Save the plot as a PNG file
    plt.savefig(os.path.join(path, f'total_{measurement}.png'))
    plt.close()  # close the figure after saving to free up memory


#------------------------------------------------------------------------------------------------#

#F4: This function plots the avg r lever presses vs l lever presses for all sessions of this animal
def plot_and_save_avg_lever_presses(animal: Animal, path: str) -> None:
    """
    Plots the average number of right lever and left lever presses for a specific animal across all sessions and saves the plot.

    Parameters
    ----------
    animal : Animal
        The animal object.
    path : str
        The path where the plot will be saved.

    Returns
    -------
    None
    """
    # Validate animal
    if not isinstance(animal, Animal):
        raise ValueError("Error: animal should be an instance of Animal class.")

    # Validate path
    if not isinstance(path, str):
        raise ValueError("Error: path should be a string.")

    if not os.path.exists(path):
        raise ValueError("Error: The provided path does not exist.")


    df=animal.animal_data

    avg_right_lever = df['right_lever'].mean()
    avg_left_lever = df['left_lever'].mean()

    # Create a bar plot
    plt.figure(figsize=(10,6))
    plt.title(f'Average Lever Presses for animal {animal.animal_id}')
    bars = plt.bar(['Left Lever', 'Right Lever'], [avg_left_lever, avg_right_lever])
    plt.xlabel('Lever')
    plt.ylabel('Average Presses')

    # Add count above each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom') 

    # Save the plot as a PNG file
    plt.savefig(os.path.join(path, f'avg_lever_presses.png'))
    plt.close()  # close the figure after saving to free up memory

#------------------------------------------------------------------------------------------------#

#Helps us calculate the avg alcohol intake for a chosen animal
def calculate_avg_alcohol_intake(df, animal_weight):
    return ((0.1 * df['Number of Rewards']) / animal_weight) * 1000


def plot_avg_alcohol_intake_by_group(df, groups, save_path):

    # Validate path
    if not isinstance(save_path, str):
        raise ValueError("Error: path should be a string.")

    if not os.path.exists(save_path):
        raise ValueError("Error: The provided path does not exist.")

    avg_intake = {}
    for group in groups:
        group_df = df.loc[df['Group'] == group]
        for animal_id in group_df['Subject'].unique():
            # Getting the animal object from global scope
            animal = globals()[f"animal_{animal_id}"]
            weight = animal.weight
            rewards = group_df.loc[group_df['Subject'] == animal_id]['right_lever'].values[0]
            intake = ((0.1*rewards)/weight)*1000
            avg_intake[f"Group {group} Animal {animal_id}"] = intake

    # Plot
    plt.figure(figsize=(10, 7))
    plt.bar(range(len(avg_intake)), list(avg_intake.values()), align='center')
    plt.xticks(range(len(avg_intake)), list(avg_intake.keys()))
    plt.ylabel('Average Alcohol Intake (g/kg)')
    plt.title('Average Alcohol Intake by Animal Grouped by Groups')
    plt.savefig(os.path.join(save_path, 'average_alcohol_intake.png'))
    plt.close()
