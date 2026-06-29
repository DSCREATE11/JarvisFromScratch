import Matrix_multiplication as mm
import numpy as np

# 1. Load the optimized parameters from the files
try:
    mm.weight_matrix = np.load("/home/divyam/Jarvis/weight_matrix.npy")
    mm.bias_matrix = np.load("/home/divyam/Jarvis/bias_matrix.npy")
    print("Loaded optimized model parameters successfully!")
except FileNotFoundError:
    print("Error: Could not find saved weights. Run your training script first!")

# 2. Start a continuous live loop to test your assistant
while True:
    user_command = input("\nPls enter the command (or type 'exit'): ")
    if user_command.lower() == 'exit':
        break
        
    # Run the forward pass with the loaded weights
    probabilities = mm.create_zMatrix(user_command)
    
    # Get the index of the highest probability
    predicted_class_idx = np.argmax(probabilities)
    confidence = probabilities[0][predicted_class_idx]
    
    predicted_class = mm.classes[predicted_class_idx]
    
    print(f"Predicted Class: {predicted_class.upper()} ({confidence*100:.2f}% confidence)")
