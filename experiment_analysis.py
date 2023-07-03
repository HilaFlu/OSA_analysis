"""
This file holds functions for an experiment related analysys
Written by: Tamar Gordon
"""

from Animal import Animal
import pandas as pd
from Experiment import Experiment
from data_extraction import process_text_data
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.ticker as ticker


# This function plots the avg intake for a selected group(s) with an option to filter by sex
# to learn how to use this func please refer to the test file
# an example of how to call this func: 'plot_avg_intake(df, groups=[1, 2], sex='Female')'

#F5
def plot_avg_intake(df: pd.DataFrame, groups: list, sex: str = None, save_path: str = '.') -> None:
    """
    Plots the average alcohol intake for each animal in each session, for the specified groups, and saves the plot.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the animal data.
    groups : List[Any]
        The groups to include in the plot.
    sex : str, optional
        The sex to include in the plot. If None, includes all sexes.
    save_path : str, optional
        The path where the plot will be saved. If not provided, defaults to the current directory.

    Returns
    -------
    None
    """
    # Validate df
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Error: df should be a pandas DataFrame.")
        
    # Validate groups
    if not isinstance(groups, list):
        raise ValueError("Error: groups should be a list.")

    if not all(isinstance(group, int) for group in groups):
        raise ValueError("Error: all elements in groups should be integers.")

    # Validate sex
    if sex is not None and not isinstance(sex, str):
        raise ValueError("Error: sex should be a string.")

    # Validate save_path
    if not isinstance(save_path, str):
        raise ValueError("Error: save_path should be a string.")

    if not os.path.exists(save_path):
        raise ValueError("Error: The provided save_path does not exist.")


    # Filter the DataFrame to include only the chosen groups
    df = df[df['Group'].isin(groups)]
    
    # If specific sex is provided, filter the DataFrame to include only that sex
    if sex is not None:
        df = df[df['sex'] == sex]
    
    # Calculate alcohol intake
    df['intake'] = ((0.1 * df['rewards']) / df['weight']) * 1000

    # Calculate average intake for each animal in each session
    avg_intake = df.groupby(['animal_id', 'session_number'])['intake'].mean().reset_index()

    plt.figure(figsize=(10, 6))

    # Plot a line for each animal
    for animal_id in avg_intake['animal_id'].unique():
        animal_data = avg_intake[avg_intake['animal_id'] == animal_id]
        plt.plot(animal_data['session_number'], animal_data['intake'], marker='o', label=f'Animal {animal_id}')

    plt.xlabel('Session')
    plt.ylabel('Average Alcohol Intake')
    plt.title('Average Alcohol Intake per Session')
    
    # Ensure that we only have integer values on the x-axis
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    
    plt.legend()

    # Save the figure to a PNG file
    plt.savefig(os.path.join(save_path, 'average_alcohol_intake.png'))

    # Close the figure to free up memory
    plt.close()

#------------------------------------------------------------------------------------------------#

# This funct plots a chosen metric for a selected group(s) with an option to filter by sex
# to learn how to use this func please refer to the test file
# the supported metrics are: rewards, head, left_lever, right_lever

#F6
def plot_metric_per_session(df: pd.DataFrame, groups: list, metric: str, sex: str = None, save_path: str = '.') -> None:
    """
    Plots the average value of a specified metric for each animal in each session, for the specified groups, and saves the plot.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the animal data.
    groups : List[Any]
        The groups to include in the plot.
    metric : str
        The metric to plot.
    sex : str, optional
        The sex to include in the plot. If None, includes all sexes.
    save_path : str, optional
        The path where the plot will be saved. If not provided, defaults to the current directory.

    Returns
    -------
    None
    """
    # Validate df
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Error: df should be a pandas DataFrame.")

    # Validate groups
    if not isinstance(groups, list):
        raise ValueError("Error: groups should be a list.")

    if not all(isinstance(group, int) for group in groups):
        raise ValueError("Error: all elements in groups should be integers.")

    # Validate metric
    if not isinstance(metric, str):
        raise ValueError("Error: metric should be a string.")

    # Validate sex
    if sex is not None and not isinstance(sex, str):
        raise ValueError("Error: sex should be a string.")

    # Validate save_path
    if not isinstance(save_path, str):
        raise ValueError("Error: save_path should be a string.")

    if not os.path.exists(save_path):
        raise ValueError("Error: The provided save_path does not exist.")


    # Filter the DataFrame to include only the chosen groups
    df = df[df['Group'].isin(groups)]
    
    # If specific sex is provided, filter the DataFrame to include only that sex
    if sex is not None:
        df = df[df['sex'] == sex]
    
    # Calculate average metric for each animal in each session
    avg_metric = df.groupby(['animal_id', 'session_number'])[metric].mean().reset_index()

    plt.figure(figsize=(10, 6))

    # Plot a line for each animal
    for animal_id in avg_metric['animal_id'].unique():
        animal_data = avg_metric[avg_metric['animal_id'] == animal_id]
        plt.plot(animal_data['session_number'], animal_data[metric], marker='o', label=f'Animal {animal_id}')

    plt.xlabel('Session')
    plt.ylabel(f'Average {metric.capitalize()}')
    plt.title(f'Average {metric.capitalize()} per Session')
    
    # Ensure that we only have integer values on the x-axis
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    
    plt.legend()

    # Save the figure to a PNG file
    plt.savefig(os.path.join(save_path, f'average_{metric}_per_session.png'))

    # Close the figure to free up memory
    plt.close()

#-------------------------------------------------------------------------------------------------#

# This funct plots the right and left lever presses per a selected group(s)
# to learn how to use this func please refer to the test file
#F7
def plot_group_presses(df: pd.DataFrame, groups: list = None, save_path: str = '.') -> None:
    """
    Plots the average number of left and right lever presses for each group, and saves the plot.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the animal data.
    groups : List[Any], optional
        The groups to include in the plot. If None, includes all groups.
    save_path : str, optional
        The path where the plot will be saved. If not provided, defaults to the current directory.

    Returns
    -------
    None
    """

    # Validate df
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Error: df should be a pandas DataFrame.")

    # Validate groups
    if groups is not None:
        if not isinstance(groups, list):
            raise ValueError("Error: groups should be a list.")

        if not all(isinstance(group, int) for group in groups):
            raise ValueError("Error: all elements in groups should be integers.")

    # Validate save_path
    if not isinstance(save_path, str):
        raise ValueError("Error: save_path should be a string.")

    if not os.path.exists(save_path):
        raise ValueError("Error: The provided save_path does not exist.")


    # Reset the index to avoid ambiguity
    df = df.reset_index()

    # If specific groups are provided, filter the DataFrame to include only those groups
    if groups is not None:
        df = df[df['Group'].isin(groups)]

    # Perform groupby operation and calculate the average
    group_averages = df.groupby('Group')[['left_lever', 'right_lever']].mean()

    # Plotting the bar graph
    x = group_averages.index.values
    left_presses = group_averages['left_lever']
    right_presses = group_averages['right_lever']

    # Define the width of the bars and the positions
    width = 0.35
    x_positions = np.arange(len(x))

    fig, ax = plt.subplots()

    # Ensure that we only have integer values on the x-axis
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    ax.bar(x_positions - width/2, left_presses, width, label='Left Lever Presses')
    ax.bar(x_positions + width/2, right_presses, width, label='Right Lever Presses')

    # Add some text for labels, title and custom x-axis tick labels
    ax.set_xlabel('Group')
    ax.set_ylabel('Presses')
    ax.set_title('Average Left and Right Lever Presses by Group')
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x)
    ax.legend()

    # Save the figure to a PNG file
    plt.savefig(os.path.join(save_path, 'average_lever_presses_by_group.png'))

    # Close the figure to free up memory
    plt.close()








