import numpy as np
import embeddingMatrix as emb
import weightsAndBias as wab
import training_data as trD
import hiddenLayer as hl

EPOCHS = 60
trainingData = trD.data
learning_rate = 0.005

hot_element_matrix = np.eye(6);

print("Starting Training")

for i in range(EPOCHS):
    for (command, target) in trainingData:
        
        """if (emb.tokenize(command) == []):
            break"""
        
        h_matrix = hl.get_ReluHiddenMatrix(command)
        z_matrix = wab.createZMatrix(h_matrix)
        target_matrix = hot_element_matrix[target]

        error_gradient = z_matrix - target_matrix
        wab.backwardPass(error_gradient, h_matrix, command, learning_rate)

print("Model trained !")

print()

test_command = "hello"

while(test_command):
    test_command = input(" Please enter a command : ")
    print(wab.createZMatrix(hl.get_ReluHiddenMatrix(test_command)))
    print()

    
    
