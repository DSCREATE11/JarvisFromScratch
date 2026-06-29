Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: /home/divyam/Jarvis/Model5_RNN/getVocab.py

= RESTART: /home/divyam/Jarvis/Model5_RNN/getVocab.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/getVocab.py", line 25, in <module>
    extract_vocab_from_corpus(BNCCorpus.txt)
                              ^^^^^^^^^
NameError: name 'BNCCorpus' is not defined

= RESTART: /home/divyam/Jarvis/Model5_RNN/getVocab.py
Extracted 132288 unique tokens from corpus.
132288
['00010Just', '099', '1', '10', '135', '1970s', '1975', '1980', '1984', '1okay', '2', '25th', '2part', '3', '36', '5', '50', '6', '6th', '6thyear', '7tel', '8', '84she', '85', '8th', 'A', 'A1', 'AAFrederick', 'AAer', 'AAnnie', 'AAvila', 'AB', 'ABBA', 'ABC', 'ABCD', 'ABDEand', 'ABasketball', 'AC', 'ACyou', 'AD', 'ADave', 'ADiana', 'AF', 'AGM', 'AI', 'AIDS', 'AIDSis', 'AJoan', 'AJohn']

= RESTART: /home/divyam/Jarvis/Model5_RNN/data_maker.py
File 'training_data.py' generated successfully with 4685 samples!

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 21, in <module>
    h_matrix = hl.get_ReluHiddenMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 21, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 15, in get_HiddenHMatrix
    h_matrix = RNN.CreateHiddenStateMatrix(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'RNN' has no attribute 'CreateHiddenStateMatrix'. Did you mean: 'CreateHiddenStateVector'?

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 21, in <module>
    h_matrix = hl.get_ReluHiddenMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 21, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 15, in get_HiddenHMatrix
    h_matrix = RNN.CreateHiddenStateVector(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 29, in CreateHiddenStateVector
    hTimeVectors.append(hiddenStateVectors)
                        ^^^^^^^^^^^^^^^^^^
NameError: name 'hiddenStateVectors' is not defined. Did you mean: 'hiddenStateVector'?

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 25, in <module>
    error_gradient = z_matrix - target_matrix
                     ~~~~~~~~~^~~~~~~~~~~~~~~
ValueError: operands could not be broadcast together with shapes (1,6) (4,) 

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateHiddenLayer( hidden_error, learningRate, command)
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 31, in updateHiddenLayer
    hidden_weight_matrix -= dw1 * learningRate # come back in case of error
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: operands could not be broadcast together with shapes (16,16) (8,16) (16,16) 

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateRNNLayer( hidden_error, command, learningRate)
    ^^^^^^^^^^^^^^^^^
AttributeError: module 'hiddenLayer' has no attribute 'updateRNNLayer'. Did you mean: 'updateHiddenLayer'?

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateRNNLayer( hidden_error, command, learningRate)
    ^^^^^^^^^^^^^^^^^
AttributeError: module 'hiddenLayer' has no attribute 'updateRNNLayer'. Did you mean: 'updateHiddenLayer'?

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateHiddenLayer( hidden_error, command, learningRate)
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 28, in updateHiddenLayer
    Relu_hidden_error_matrix = hidden_error_matrix * Relu.Relu_backward(get_HiddenHMatrix(command))
                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 15, in get_HiddenHMatrix
    h_matrix = RNN.CreateHiddenStateVector(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 21, in CreateHiddenStateVector
    input_matrix = emb.get_sub_matrix(emb.get_index(emb.tokenize(input_command)))
                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/embeddingMatrix.py", line 13, in tokenize
    for i in raw_sentence:
TypeError: 'float' object is not iterable

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 31, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateHiddenLayer( hidden_error, command, learningRate)
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 28, in updateHiddenLayer
    Relu_hidden_error_matrix = hidden_error_matrix * Relu.Relu_backward(get_HiddenHMatrix(command))
                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 15, in get_HiddenHMatrix
    h_matrix = RNN.CreateHiddenStateVector(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 21, in CreateHiddenStateVector
    input_matrix = emb.get_sub_matrix(emb.get_index(emb.tokenize(input_command)))
                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/embeddingMatrix.py", line 13, in tokenize
    for i in raw_sentence:
TypeError: 'float' object is not iterable

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateHiddenLayer( hidden_error, learningRate, command)
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 35, in updateHiddenLayer
    RNN.UpdateRNNLayer(RNNFinalError, command, learningRate)
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 60, in UpdateRNNLayer
    hiddenBiasMatrix -= changeHiddenBiasMatrix * learningRate
    ^^^^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'hiddenBiasMatrix' where it is not associated with a value

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 26
    z_t = (input_matrix[i:i+1] @ currentHiddenWeightMatrix) + ( hiddenStateVector @ pastHiddenWeightMatrix) + hiddenBiasMatrix
RuntimeWarning: overflow encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 26
    z_t = (input_matrix[i:i+1] @ currentHiddenWeightMatrix) + ( hiddenStateVector @ pastHiddenWeightMatrix) + hiddenBiasMatrix
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 16
    new_matrix = h_matrix @ hidden_weight_matrix + hidden_bias_matrix
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 28
    probability_matrix = h_matrix @ weight_matrix + bias_matrix
RuntimeWarning: invalid value encountered in matmul

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 34
    RNNFinalError = Relu_hidden_error_matrix @ hidden_weight_matrix.T
RuntimeWarning: overflow encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 49
    changePastHiddenWeightMatrix += hTimeVectors[i].T @ currentHiddenError
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 53
    embedding_error = currentHiddenError @ currentHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 56
    futureHiddenError = currentHiddenError @ pastHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 47
    changeCurrentHiddenWeightMatrix += input_matrix[i:i+1].T @ currentHiddenError
RuntimeWarning: invalid value encountered in add

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 45
    currentHiddenError = futureHiddenError * Relu.Relu_backward(zTimeVectors[i])
RuntimeWarning: invalid value encountered in multiply

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 3, in <module>
    import hiddenLayer as hl
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 4, in <module>
    import RNN
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 2
    import Relu(Copy 1) as Relu
               ^
SyntaxError: invalid syntax

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 3, in <module>
    import hiddenLayer as hl
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 4, in <module>
    import RNN
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 2
    import 'Relu(Copy 1)' as Relu
           ^^^^^^^^^^^^^^
SyntaxError: invalid syntax

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 47
    changeCurrentHiddenWeightMatrix += input_matrix[i:i+1].T @ currentHiddenError
RuntimeWarning: overflow encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 45
    currentHiddenError = futureHiddenError * Relu.Relu_backward(zTimeVectors[i])
RuntimeWarning: overflow encountered in multiply

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 47
    changeCurrentHiddenWeightMatrix += input_matrix[i:i+1].T @ currentHiddenError
RuntimeWarning: invalid value encountered in add

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 53
    embedding_error = currentHiddenError @ currentHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 56
    futureHiddenError = currentHiddenError @ pastHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

============= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py =============
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/sigmoid.py", line 12
    return forward_matrix * (1.0 - forward_matrix)
RuntimeWarning: overflow encountered in multiply

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 54
    embedding_error = currentHiddenError @ currentHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 57
    futureHiddenError = currentHiddenError @ pastHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 21, in <module>
    h_matrix = hl.get_ReluHiddenMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 21, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 15, in get_HiddenHMatrix
    h_matrix = RNN.CreateHiddenStateVector(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 28, in CreateHiddenStateVector
    hiddenStateVector = Relu.Relu_forward(z_t)
                        ^^^^^^^^^^^^^^^^^
AttributeError: module 'sigmoid' has no attribute 'Relu_forward'. Did you mean: 'Relu_backward'?

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/sigmoid.py", line 7
    1.0 / (1.0 + np.exp(-z)),
RuntimeWarning: overflow encountered in exp

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/sigmoid.py", line 8
    np.exp(z) / (1.0 + np.exp(z))
RuntimeWarning: overflow encountered in exp

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/sigmoid.py", line 8
    np.exp(z) / (1.0 + np.exp(z))
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 45
    currentHiddenError = futureHiddenError * Relu.Relu_backward(zTimeVectors[i])
RuntimeWarning: overflow encountered in multiply

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 50
    changePastHiddenWeightMatrix += hTimeVectors[i].T @ currentHiddenError
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 54
    embedding_error = currentHiddenError @ currentHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 57
    futureHiddenError = currentHiddenError @ pastHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 45
    currentHiddenError = futureHiddenError * Relu.Relu_backward(zTimeVectors[i])
RuntimeWarning: overflow encountered in multiply

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 54
    embedding_error = currentHiddenError @ currentHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 57
    futureHiddenError = currentHiddenError @ pastHiddenWeightMatrix.T
RuntimeWarning: invalid value encountered in matmul

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model5_RNN/sigmoid.py", line 16
    return forward_matrix * (1.0 - forward_matrix)
RuntimeWarning: overflow encountered in multiply

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model5_RNN/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model5_RNN/weightsAndBias.py", line 41, in backwardPass
    hl.updateHiddenLayer( hidden_error, learningRate, command)
  File "/home/divyam/Jarvis/Model5_RNN/hiddenLayer.py", line 35, in updateHiddenLayer
    RNN.UpdateRNNLayer(RNNFinalError, command, learningRate)
  File "/home/divyam/Jarvis/Model5_RNN/RNN.py", line 40, in UpdateRNNLayer
    changePastHiddenWeightMatrix = np.zeros((NEURONS, NEURONS))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training
Model trained !

 Please enter a command : Hello Jarvis
[[0.03269224 0.02188984 0.22584794 0.07821242 0.19585583 0.44550173]]

 Please enter a command : hey
[[1.73736480e-01 3.47569091e-03 4.45742363e-05 6.38517074e-09
  6.91096441e-04 8.22052152e-01]]

 Please enter a command : google the president of india
[[5.72459046e-01 6.18594810e-13 4.73605181e-04 9.14358742e-03
  7.20484775e-02 3.45875283e-01]]

 Please enter a command : turn on the fan
[[1.44684327e-03 9.98337127e-01 9.08337432e-12 2.39983022e-16
  2.57294458e-06 2.13457111e-04]]

 Please enter a command : 
= RESTART: /home/divyam/Jarvis/Model5_RNN/training.py
Starting Training
Model trained !

 Please enter a command : fan
[[1.11385612e-09 9.95448898e-01 4.78937364e-05 1.25158015e-07
  4.28163222e-03 2.21449448e-04]]

 Please enter a command : It is so hot in this room
[[9.77197938e-01 2.27741586e-02 1.63634826e-05 6.27502516e-12
  1.11138365e-05 4.26274477e-07]]

 Please enter a command : Turn on the lights
[[2.36957880e-05 4.56056391e-01 1.97981263e-06 1.86428008e-05
  5.39722684e-01 4.17660606e-03]]

 Please enter a command : Turn on the fan
[[2.81584024e-07 9.99992009e-01 4.21805838e-08 2.70103696e-11
  7.52191580e-06 1.45520853e-07]]

 Please enter a command : turn on the lamp
[[9.99981350e-01 1.41948619e-05 1.10995440e-11 2.73071008e-12
  4.45419446e-06 1.32237417e-09]]

 Please enter a command : I want to read a book
[[3.51597280e-07 9.98867960e-01 2.09057205e-07 4.15744468e-07
  1.11342471e-03 1.76389550e-05]]

 Please enter a command : Write an application
[[4.48788459e-01 6.42666298e-02 1.51280397e-06 1.06853570e-02
  3.95591617e-01 8.06664244e-02]]

 Please enter a command : hello
[[2.82730224e-10 5.54190522e-07 2.43589779e-03 3.95370924e-03
  2.32157045e-02 9.70394134e-01]]

 Please enter a command : hey Jarvis!
[[2.27535423e-04 1.58472589e-03 1.33647580e-05 2.89926383e-08
  7.42581174e-02 9.23916228e-01]]

 Please enter a command : how are you doing ?
[[3.11485820e-13 7.88556101e-09 4.24200346e-06 1.77694717e-03
  1.55061699e-02 9.82712633e-01]]

 Please enter a command : Who was the president of india ?
[[8.59075181e-06 1.61182141e-03 2.33334319e-06 1.76441155e-04
  5.76110748e-01 4.22090065e-01]]

 Please enter a command : where is america
[[1.38851276e-04 4.78862392e-03 9.93917858e-01 8.29932349e-14
  7.17638885e-06 1.14749023e-03]]

 Please enter a command : what time is it in india
[[1.28305680e-02 8.86434855e-01 2.83346058e-06 2.92207521e-06
  7.76173597e-03 9.29670859e-02]]

 Please enter a command : write a mail to mom
[[9.63963446e-01 2.51229102e-02 1.10416577e-09 1.58960742e-05
  1.06252222e-02 2.72524034e-04]]

 Please enter a command : mail
[[2.10709631e-11 1.44728750e-04 9.97138389e-01 4.24846482e-09
  6.41039893e-05 2.65277378e-03]]

 Please enter a command : write an email
[[1.46990290e-10 1.78900434e-07 7.93392263e-01 5.85360744e-02
  9.21513981e-05 1.47979332e-01]]

 Please enter a command : set up my meeting
[[6.21598941e-07 2.98821056e-02 1.43050524e-08 4.87798480e-01
  4.73434349e-01 8.88442959e-03]]

 Please enter a command : set reminder to my meeting on 24 january
[[2.27912361e-05 9.89293554e-01 2.03013531e-07 9.80429889e-06
  1.04274675e-02 2.46179779e-04]]

 Please enter a command : a very very very very  long sentece
[[3.68373542e-18 5.85616751e-14 9.99999601e-01 6.98149079e-19
  4.87820297e-09 3.94081062e-07]]

 Please enter a command : is there any new mail?
[[1.37760922e-05 6.69048570e-02 8.98314716e-01 1.88183999e-05
  5.54885708e-03 2.91989752e-02]]

 Please enter a command : 
[[0.00637392 0.04522202 0.263592   0.02273435 0.30780179 0.35427592]]

