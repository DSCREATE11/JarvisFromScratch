import Matrix_multiplication as mm
import Vectorization as vp
import training_data
import numpy as np

# creating one-hot encoding matrix

edge_size = mm.return_classes_size()
encoding_matrix = np.zeros((edge_size,edge_size))

for i in range(edge_size):
    for j in range(edge_size):
        if(i==j):
            encoding_matrix[i][j] = 1
            break

# calculating the error gradient, adjustment and running epochs

dataset = training_data.training_data

print("Starting epoch")

for i in range(500):
    for input_sentence,target in dataset:
        error_gradient = mm.create_zMatrix(input_sentence) - np.array(encoding_matrix[target])
        input_matrix = vp.Create_vector(input_sentence, mm.bag_of_words)
        adjustment_matrix = input_matrix.T @ error_gradient
        mm.weight_matrix = mm.weight_matrix - (mm.LEARNING_RATE * adjustment_matrix)
        mm.bias_matrix = mm.bias_matrix - (mm.LEARNING_RATE * error_gradient)    

print("Model trained")
np.save("/home/divyam/Jarvis/weight_matrix.npy", mm.weight_matrix)
np.save("/home/divyam/Jarvis/bias_matrix.npy", mm.bias_matrix)

print("Saved trained weights and biases successfully!")
print()

command = input("Pls enter the command : ")

print(mm.create_zMatrix(command))
            
