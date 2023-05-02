import numpy as np
from tabulate import tabulate

data = [0, 1, 0, 1, 0, 2, 0]


def transition_density_matrix(data):

    num_states = len(set(data))
    transition_matrix = np.zeros((num_states, num_states))
    for i in range(len(data) - 1):
        current_state = data[i]
        next_state = data[i + 1]
        transition_matrix[current_state][next_state] += 1
    # Normalize the rows of the transition matrix to obtain transition probabilities
    transition_matrix = transition_matrix / np.sum(transition_matrix, axis=1, keepdims=True)
    # Define row and column labels
    col_labels = ["To State {}".format(i) for i in range(num_states)]
    row_labels = ["From State {}".format(i) for i in range(num_states)]
    # Add row and column labels to the transition matrix
    transition_matrix = np.vstack([col_labels, transition_matrix])
    transition_matrix = np.hstack([np.array([[""] + row_labels]).T, transition_matrix])
    # Calculate the number of active transition cells
    active_cells = np.count_nonzero(transition_matrix)
    # Calculate the total number of cells
    total_cells = transition_matrix.shape[0] * transition_matrix.shape[1]
    # Calculate the desired quantitative value
    quantitative_value = active_cells / total_cells

    result = f"Number of active transition cells: {active_cells}\nTotal number of cells: {total_cells}\nSingle Quantitative value: {quantitative_value}\n"
    return result


