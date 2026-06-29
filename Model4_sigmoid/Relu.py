import numpy as np

def Relu_forward(input_matrix):
    # Standard Sigmoid forward pass: 1 / (1 + e^-x)
    # Clipping input_matrix between -50 and 50 prevents exponentials from blowing up
    clipped_input = np.clip(input_matrix, -50, 50)
    return 1.0 / (1.0 + np.exp(-clipped_input))

def Relu_backward(forward_matrix):
    # CRITICAL: Sigmoid derivative uses the POST-activation matrix (h_hidden)
    # Formula: h * (1 - h)
    return forward_matrix * (1.0 - forward_matrix)
