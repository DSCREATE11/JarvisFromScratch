import numpy as np
import embeddingMatrix as emb
import hiddenLayer as hl

classes = ["Lights", "Fans", "Mail", "Calendar", "Search", "Greet"]

NEURONS = 16

weight_matrix = np.random.randn(NEURONS,len(classes)) * 0.01
bias_matrix = np.zeros((1,len(classes)))

def softmax(probability_matrix):

    (rows, columns) = probability_matrix.shape
    z_matrix = np.zeros((rows, columns))

    for i in range(rows):
        sum = 0
        row_max = np.max(probability_matrix[i])
        for j in range(columns):
            sum += np.exp(probability_matrix[i][j] - row_max)
        for j in range(columns):
            z_matrix[i][j] = np.exp(probability_matrix[i][j] - row_max)/sum
    return z_matrix

def createZMatrix( h_matrix ):
    global weight_matrix, bias_matrix
    probability_matrix = h_matrix @ weight_matrix + bias_matrix
    z_matrix = softmax(probability_matrix)
    return z_matrix

def backwardPass(error_gradient, hMatrix, command, learningRate):

    global weight_matrix, bias_matrix
    
    dw = (hMatrix.T @ error_gradient)
    weight_matrix -= dw * learningRate
    bias_matrix -= error_gradient * learningRate

    hidden_error = error_gradient @ weight_matrix.T
    hl.updateHiddenLayer( hidden_error, learningRate, command)


    

