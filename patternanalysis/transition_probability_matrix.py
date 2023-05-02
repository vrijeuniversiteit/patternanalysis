from tabulate import tabulate

import numpy as np

def transition_matrix(arr, order=1):
    """"
    Computes the transition matrix from Markov chain sequence of order `order`.

    :param arr: Discrete Markov chain state sequence in discrete time with states in 0, ..., N
    :param order: Transition order
    """

    M = np.zeros(shape=(max(arr) + 1, max(arr) + 1))
    for (i, j) in zip(arr, arr[1:]):
        M[i, j] += 1

    T = (M.T / M.sum(axis=1)).T

    return np.linalg.matrix_power(T, order)


def transition_probability_matrix(data):
    transition = transition_matrix(arr=data, order=1)

    col_labels = ["To State {}".format(i) for i in range(len(transition))]
    row_labels = ["From State {}".format(i) for i in range(len(transition))]

    transition_with_labels = np.vstack([col_labels, transition])
    transition_with_labels = np.hstack([np.array([[""] + row_labels]).T, transition_with_labels])

    table = tabulate(transition_with_labels, headers='firstrow', tablefmt='fancy_grid')
    return table
