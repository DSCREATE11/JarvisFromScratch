""" It takes in a normalized list and bag of words and returns the vector """

import numpy as np

def Create_vector(input_list,bag_of_words):
    outputVector = np.zeros((1,len(bag_of_words)))
    c=0
    for i in bag_of_words:
        if(i in input_list):
            outputVector[0][c] = 1
        c+=1
    return outputVector



