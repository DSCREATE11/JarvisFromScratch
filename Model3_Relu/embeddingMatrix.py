import numpy as np
import wordToIndex as wti

(words, wordDict) = wti.build_vocabulary("vocabulary.txt")
"""stopWords = wti.STOP_WORD"""


DIMENSION = 8
embedding_matrix = np.random.randn(10000, DIMENSION)

def tokenize(raw_sentence):
    new_sentence = ""
    for i in raw_sentence:
        if((i.isalnum() or i.isspace()) and """i not in stopWords"""):
            new_sentence += i
    tokens = new_sentence.split()
    return tokens

def get_index(tokens):
    global wordDict
    index_list = []
    for i in tokens:
        if i in wordDict:
            index_list.append(wordDict[i])
    return index_list

def get_sub_matrix(index_list):
    global embedding_matrix,DIMENSION
    sub_matrix = np.zeros((len(index_list), DIMENSION))
    for index,row in enumerate(index_list):
        for j in range(DIMENSION):
            sub_matrix[index][j] = embedding_matrix[row][j]
    return sub_matrix

def getHMatrix(input_text):
    tokens = tokenize(input_text)
    index_list = get_index(tokens)
    sub_matrix = get_sub_matrix(index_list)

    """if len(index_list) == 0:
        return np.zeros((1, DIMENSION))"""
    
    (rows,columns) = sub_matrix.shape
    h_matrix = np.zeros((1, columns))
    for j in range(columns):
        sum = 0
        for i in range(rows):
            sum += sub_matrix[i][j]
        h_matrix[0][j] = sum/rows
    
    
    return h_matrix

def update_embedding_matrix(dh, command, learning_rate):

    global embedding_matrix

    index_list = get_index(tokenize(command))
    
    """if len(index_list) == 0:
        return"""
    
    adjustment_matrix = dh.flatten()/len(index_list)
    for i in index_list:
        embedding_matrix[i] -= learning_rate * adjustment_matrix   







