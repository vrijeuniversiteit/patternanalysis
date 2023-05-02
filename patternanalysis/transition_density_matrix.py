import numpy as np

def transition_density_matrix(data):
    number_of_states = len(set(data))
    transition_matrix = np.zeros((number_of_states, number_of_states))
    for i in range(len(data) - 1):
        current_state = data[i]
        next_state = data[i + 1]
        transition_matrix[current_state][next_state] += 1

    probabilities = transition_matrix / np.sum(transition_matrix, axis=1, keepdims=True)
    
    col_labels = ["To State {}".format(i) for i in range(number_of_states)]
    row_labels = ["From State {}".format(i) for i in range(number_of_states)]
    probabilities = np.vstack([col_labels, probabilities])
    probabilities = np.hstack([np.array([[""] + row_labels]).T, probabilities])
    active_cells = np.count_nonzero(probabilities)
    total_cells = probabilities.shape[0] * probabilities.shape[1]
    quantitative_value = active_cells / total_cells

    result = f"Number of active transition cells: {active_cells}\nTotal number of cells: {total_cells}\nSingle Quantitative value: {quantitative_value}\n"
    return result


