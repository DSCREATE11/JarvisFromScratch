import numpy as np

def Relu_forward(z):

    z = np.clip(z, -500, 500)
    # Safe implementation that prevents exponential explosion
    return np.where(
        z >= 0,
        1.0 / (1.0 + np.exp(-z)),
        np.exp(z) / (1.0 + np.exp(z))
    )

# Change the function inside your activation file to this:
def Relu_backward(z_matrix):
    # Safe forward pass first to get the bounded state (h)
    z_matrix = np.clip(z_matrix, -500, 500)
    h = 1.0 / (1.0 + np.exp(-z_matrix))
    
    # Now this is perfectly stable!
    return h * (1.0 - h)
