import numpy as np
import Relu
import embeddingMatrix as emb

NEURONS = 16
DIMENSION = 8

hidden_weight_matrix = np.random.randn(DIMENSION, NEURONS) * np.sqrt(2.0 / DIMENSION)
hidden_bias_matrix = np.zeros((1, NEURONS)) 

def get_HiddenHMatrix( input_text ):
    global hidden_weight_matrix, hidden_bias_matrix
    
    h_matrix = emb.getHMatrix(input_text)
    new_matrix = h_matrix @ hidden_weight_matrix + hidden_bias_matrix
    return new_matrix

def get_ReluHiddenMatrix( input_text ):

    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
    return new_matrix

def updateHiddenLayer( hidden_error_matrix, learningRate, command):

    global hidden_weight_matrix, hidden_bias_matrix

    Relu_hidden_error_matrix = hidden_error_matrix * Relu.Relu_backward(get_HiddenHMatrix(command))
    dw1 = emb.getHMatrix(command).T @ Relu_hidden_error_matrix
    
    hidden_weight_matrix -= hidden_error_matrix * learningRate
    hidden_bias_matrix -= Relu_hidden_error_matrix * learningRate

    embedding_error = Relu_hidden_error_matrix @ hidden_weight_matrix.T
    emb.update_embedding_matrix(embedding_error, command, learningRate)
    
    
    

    
