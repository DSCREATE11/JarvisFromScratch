import Input_Text_Processor
import Vectorization
import numpy as np

bag_of_words = [
    "turn", "on", "off", "start", "stop",     # Actions
    "light", "lamp", "fan", "camera",          # Hardware Targets
    "stuffy", "hot", "dark", "night",         # Contextual States / Triggers
    "log", "save", "record", "capture",     # Logging / Physics Project Tasks
    "what", "why", "how", "explain", "weather","cloud"# Out-of-Domain / Cloud Triggers
]

classes = ["fan","lamp","light","camera"]

LEARNING_RATE = 0.05

weight_matrix = np.random.randn(len(bag_of_words), len(classes))*0.01
bias_matrix = np.zeros((1,4))

def return_vocab_size():
    return len(bag_of_words)

def return_classes_size():
    return len(classes)

def softmax(input_matrix):

    (rows,columns) = input_matrix.shape
    probability_matrix = np.zeros((rows,columns))
    
    sum_list = []
    
    for i in range(rows):
        sum = 0
        for j in range(columns):
            sum += np.exp(input_matrix[i][j])
        sum_list.append(sum)

    for i in range(rows):
        for j in range(columns):
            probability_matrix[i][j] = np.exp(input_matrix[i][j])/sum_list[i]

    return probability_matrix
            

def create_zMatrix(raw_string):

    global weight_matrix, bias_matrix
     
    normalized_text = Input_Text_Processor.process_string(raw_string)
    input_matrix = Vectorization.Create_vector(normalized_text, bag_of_words)
    zMatrix = input_matrix@weight_matrix + bias_matrix
    probability_matrix = softmax(zMatrix)

    return probability_matrix

    
    
    


