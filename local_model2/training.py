import numpy as np
import embeddingMatrix as emb
import weightsAndBias as wab
import trainingData as trD

EPOCHS = 1000
trainingData = trD.training_data
learning_rate = 0.01

hot_element_matrix = np.eye(4);

print("Starting Training")

for i in range(EPOCHS):
    for (command, target) in trainingData:
        if (emb.tokenize(command) == []):
            break
        h_matrix = emb.getHMatrix(command)
        z_matrix = wab.createZMatrix(h_matrix)
        target_matrix = hot_element_matrix[target]

        error_gradient = z_matrix - target_matrix
        dW = h_matrix.T @ error_gradient
        dh = error_gradient @ wab.weight_matrix.T

        emb.update_embedding_matrix(dh, command, learning_rate)
        wab.weight_matrix -= learning_rate * dW
        wab.bias_matrix -= learning_rate * error_gradient

print("Model trained !")

print()

test_command = "hello"

while(test_command):
    test_command = input(" Please enter a command : ")
    print(wab.createZMatrix(emb.getHMatrix(test_command)))
    print()

    
    
