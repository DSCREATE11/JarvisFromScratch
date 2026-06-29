import numpy as np

def Relu_forward( input_matrix ):

    (rows, columns) = input_matrix.shape
    new_matrix = np.zeros(input_matrix.shape)

    for i in range(rows):
        for j in range(columns):
            if(input_matrix[i][j] > 0):
                new_matrix[i][j] = input_matrix[i][j]

    return new_matrix

def Relu_backward( input_matrix ):

    (rows, columns) = input_matrix.shape
    new_matrix = np.zeros(input_matrix.shape)

    for i in range(rows):
        for j in range(columns):
            if(input_matrix[i][j] > 0):
                new_matrix[i][j] = 1

    return new_matrix
