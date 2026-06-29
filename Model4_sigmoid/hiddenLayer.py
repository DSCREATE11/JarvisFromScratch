import numpy as np
import Relu
import embeddingMatrix as emb

NEURONS = 16
DIMENSION = 8

# For Sigmoid, traditional random initialization works nicely
hidden_weight_matrix = np.random.randn(DIMENSION, NEURONS) * 0.1
hidden_bias_matrix = np.zeros((1, NEURONS))

def get_HiddenHMatrix(input_text):
    global hidden_weight_matrix, hidden_bias_matrix
    h_matrix = emb.getHMatrix(input_text)
    new_matrix = h_matrix @ hidden_weight_matrix + hidden_bias_matrix
    return new_matrix

def get_ReluHiddenMatrix(input_text):
    return Relu.Relu_forward(get_HiddenHMatrix(input_text))

def updateHiddenLayer(hidden_error_matrix, learningRate, command):
    global hidden_weight_matrix, hidden_bias_matrix

    # 1. Get the POST-activation hidden matrix (h_hidden) from the forward pass
    h_hidden = get_ReluHiddenMatrix(command)
    
    # 2. Compute the Sigmoid backward gate using h_hidden * (1 - h_hidden)
    Relu_hidden_error_matrix = hidden_error_matrix * Relu.Relu_backward(h_hidden)
    
    # 3. Calculate weight gradients
    h_avg = emb.getHMatrix(command)
    dw1 = h_avg.T @ Relu_hidden_error_matrix
    
    # 4. Update parameters
    hidden_weight_matrix -= dw1 * learningRate
    hidden_bias_matrix -= Relu_hidden_error_matrix * learningRate

    # 5. Project error back to word embeddings
    embedding_error = Relu_hidden_error_matrix @ hidden_weight_matrix.T
    emb.update_embedding_matrix(embedding_error, command, learningRate)
