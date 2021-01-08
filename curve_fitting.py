"""Module for finding various curve fits for given datasets."""
from typing import List, Tuple
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import Axes

from scipy.optimize import curve_fit
import plotting_data_with_pandas as pd_with_pandas


def linear_function(x: float, m: float, b: float) -> float:
    """Return the model linear function that will be used as a parameter in the curve_fit function
    """
    return m * x + b


def quadratic_function(x: float, a: float, b: float, c: float) -> float:
    """Return the model quadratic function that will be used as a parameter in the
    curve_fit function
    """
    return (a * x) + (b * x ** 2) + c


def cubic_function(x: float, a: float, b: float, c: float, d: float) -> float:
    """Return the model quadratic function that will be used as a parameter in the
    curve_fit function
    """
    return (a * x) + (b * x ** 2) + (c * x ** 3) + d


def exponential_function(x: float, a: float, b: float) -> float:
    """Return the model exponential function that will be used as a parameter in the
    curve_fit function
    """
    return a ** x + b


def linear_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> Axes:
    """Graph a scatter plot and a linear curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(linear_function, ind_list, dep_list)
    for i in range(n):
        y_value = linear_function(ind_list[i], variables[0][0], variables[0][1])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    ax = plotting_data_with_curve(independent_name, variables)

    return ax


def quadratic_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> Axes:
    """Graph a scatter plot and a quadratic curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(quadratic_function, ind_list, dep_list)
    for i in range(n):
        y_value = quadratic_function(ind_list[i], variables[0][0], variables[0][1], variables[0][2])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    ax = plotting_data_with_curve(independent_name, variables)

    return ax


def cubic_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> Axes:
    """Graph a scatter plot and a cubic curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(cubic_function, ind_list, dep_list)

    for i in range(n):
        y_value = cubic_function(ind_list[i], variables[0][0], variables[0][1], variables[0][2],
                                 variables[0][3])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    ax = plotting_data_with_curve(independent_name, variables)

    return ax


def exponential_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> Axes:
    """Graph a scatter plot and an exponential curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively.
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(exponential_function, ind_list, dep_list)
    for i in range(n):
        y_value = exponential_function(ind_list[i], variables[0][0], variables[0][1])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    ax = plotting_data_with_curve(independent_name, variables)
    return ax


def plotting_data_with_curve(independent_name: str, variables: Tuple[List, List, List]) -> Axes:
    """Plot the data in a scatter plot together with the curve of best fit
    Preconditions:
        - independent_name != ''
        - variables != ()
    """
    fig, ax = plt.subplots()
    plt.scatter(variables[0], variables[1])  # line connecting dots with matplotlib
    plt.plot(variables[0], variables[2], '--', color='red')
    plt.show()
    # creating title and axes titles
    plt.figtext(.5, .9, independent_name + ' Against Global Mean Sea Level Changes from '
                '1993 to 2014', fontsize=7.5, ha='center')
    plt.xlabel(independent_name)
    plt.ylabel('Global Mean Sea Level Change (inches)')

    return ax


if __name__ == '__main__':
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # Leave this code uncommented when you submit your files.
    import python_ta

    python_ta.check_all(config={
        'allowed-io': ['read_csv_data'],
        'extra-imports': ['python_ta.contracts', 'csv', 'datetime',
                          'plotly.graph_objects', 'plotly.subplots',
                          'matplotlib.pyplot', 'mpl_toolkits.axisartist',
                          'plotting_data_with_pandas', 'scipy.optimize'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
