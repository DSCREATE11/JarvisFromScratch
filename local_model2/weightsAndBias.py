import numpy as np
import embeddingMatrix as emb

classes = ["Fan", "Lamp", "Camera", "Google"]

weight_matrix = np.random.randn(8,len(classes)) * 0.01
bias_matrix = np.zeros((1,len(classes)))

def softmax(probability_matrix):

    (rows, columns) = probability_matrix.shape
    z_matrix = np.zeros((rows, columns))

    for i in range(rows):
        sum = 0
        for j in range(columns):
            sum += np.exp(probability_matrix[i][j])
        for j in range(columns):
            z_matrix[i][j] = np.exp(probability_matrix[i][j])/sum
    return z_matrix

def createZMatrix( h_matrix ):
    global weight_matrix, bias_matrix
    probability_matrix = h_matrix @ weight_matrix + bias_matrix
    z_matrix = softmax(probability_matrix)
    return z_matrix

dummy_command = "Turn on the lights, it is dark"
print(createZMatrix(emb.getHMatrix(dummy_command)))
