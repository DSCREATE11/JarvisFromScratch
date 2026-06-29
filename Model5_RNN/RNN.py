import numpy as np
import sigmoid as Relu
import embeddingMatrix as emb

DIMENSION = 8
NEURONS = 16

currentHiddenWeightMatrix = np.random.randn(DIMENSION, NEURONS) * np.sqrt(2/DIMENSION)
pastHiddenWeightMatrix = np.random.randn(NEURONS, NEURONS) * np.sqrt(2/NEURONS)
hiddenBiasMatrix = np.zeros((1, NEURONS))

hTimeVectors = []
zTimeVectors = []

def CreateHiddenStateVector(input_command):
    global currentHiddenWeightMatrix, pastHiddenWeightMatrix, hiddenBiasMatrix, hTimeVectors, zTimeVectors

    hTimeVectors = []
    zTimeVectors = []

    input_matrix = emb.get_sub_matrix(emb.get_index(emb.tokenize(input_command)))
    (rows, columns) = input_matrix.shape
    hiddenStateVector = np.zeros((1, NEURONS))

    for i in range(rows):
        z_t = (input_matrix[i:i+1] @ currentHiddenWeightMatrix) + ( hiddenStateVector @ pastHiddenWeightMatrix) + hiddenBiasMatrix
        zTimeVectors.append(z_t)
        hiddenStateVector = Relu.Relu_forward(z_t)
        hTimeVectors.append(hiddenStateVector)

    return hiddenStateVector

def UpdateRNNLayer(futureHiddenError, command, learningRate):
    global currentHiddenWeightMatrix, pastHiddenWeightMatrix, hiddenBiasMatrix

    index_list = emb.get_index(emb.tokenize(command))
    input_matrix = emb.get_sub_matrix(emb.get_index(emb.tokenize(command)))
    
    changeCurrentHiddenWeightMatrix = np.zeros((DIMENSION, NEURONS))
    changePastHiddenWeightMatrix = np.zeros((NEURONS, NEURONS))
    changeHiddenBiasMatrix = np.zeros((1, NEURONS))

    for i in range(len(index_list)-1, -1, -1):

        currentHiddenError = futureHiddenError * Relu.Relu_backward(zTimeVectors[i])
        futureHiddenError = np.clip(futureHiddenError, -1.0, 1.0)
        
        changeCurrentHiddenWeightMatrix += input_matrix[i:i+1].T @ currentHiddenError
        
        changePastHiddenWeightMatrix += hTimeVectors[i].T @ currentHiddenError

        changeHiddenBiasMatrix += currentHiddenError

        embedding_error = currentHiddenError @ currentHiddenWeightMatrix.T
        emb.update_index_embedding_matrix(embedding_error, index_list[i], learningRate)

        futureHiddenError = currentHiddenError @ pastHiddenWeightMatrix.T

    # --- INSIDE UpdateRNNLayer (Right before parameter updates) ---
    
    # Clip gradients to sit strictly between -1.0 and 1.0
    np.clip(changeCurrentHiddenWeightMatrix, -1.0, 1.0, out=changeCurrentHiddenWeightMatrix)
    np.clip(changePastHiddenWeightMatrix, -1.0, 1.0, out=changePastHiddenWeightMatrix)
    np.clip(changeHiddenBiasMatrix, -1.0, 1.0, out=changeHiddenBiasMatrix)


    currentHiddenWeightMatrix -= changeCurrentHiddenWeightMatrix * learningRate
    pastHiddenWeightMatrix -= changePastHiddenWeightMatrix * learningRate
    hiddenBiasMatrix -= changeHiddenBiasMatrix * learningRate

    
        
