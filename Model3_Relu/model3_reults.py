Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 3, in <module>
    import hiddenLayer.py as hl
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 8, in <module>
    hidden_weight_matrix = np.zeroes((DIMENSION, NEURONS))
                           ^^^^^^^^^
  File "/usr/lib/python3/dist-packages/numpy/__init__.py", line 333, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'zeroes'. Did you mean: 'zeros'?

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 3, in <module>
    import hiddenLayer.py as hl
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 8, in <module>
    hidden_weight_matrix = np.zeros((DIMENSION, NEURONS))
                                     ^^^^^^^^^
NameError: name 'DIMENSION' is not defined. Did you mean: 'DIMESNION'?

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 3, in <module>
    import hiddenLayer.py as hl
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 8, in <module>
    hidden_weight_matrix = np.zeros((DIMENSION, NEURONS))
                                     ^^^^^^^^^
NameError: name 'DIMENSION' is not defined. Did you mean: 'DIMENSNION'?

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 3, in <module>
    import hiddenLayer.py as hl
ModuleNotFoundError: No module named 'hiddenLayer.py'; 'hiddenLayer' is not a package

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 3, in <module>
    import hiddenLayer.py as hl
ModuleNotFoundError: No module named 'hiddenLayer.py'; 'hiddenLayer' is not a package

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 21, in <module>
    h_matrix = hl.get_ReluHiddenMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 20, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 14, in get_HiddenHMatrix
    h_matrix = emb.getHMatrix()
               ^^^^^^^^^^^^^^^^
TypeError: getHMatrix() missing 1 required positional argument: 'input_text'

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 26, in <module>
    BackwardPass(error_gradient, h_matrix, command, learningRate)
    ^^^^^^^^^^^^
NameError: name 'BackwardPass' is not defined

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 26, in <module>
    backwardPass(error_gradient, h_matrix, command, learningRate)
    ^^^^^^^^^^^^
NameError: name 'backwardPass' is not defined

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learningRate)
                                                        ^^^^^^^^^^^^
NameError: name 'learningRate' is not defined. Did you mean: 'learning_rate'?

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 40, in backwardPass
    hl.updateHiddenLayer( hidden_error, learningRate, command)
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 28, in updateHiddenLayer
    dw1 = emb.getHmatrix(command).T @ Relu_hidden_error_matrix
          ^^^^^^^^^^^^^^
AttributeError: module 'embeddingMatrix' has no attribute 'getHmatrix'. Did you mean: 'getHMatrix'?

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 40, in backwardPass
    hl.updateHiddenLayer( hidden_error, learningRate, command)
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 34, in updateHiddenLayer
    emb.update_embedding_matrix(dh, command, learning_rate)
                                ^^
NameError: name 'dh' is not defined

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 26, in <module>
    wab.backwardPass(error_gradient, h_matrix, command, learning_rate)
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 40, in backwardPass
    hl.updateHiddenLayer( hidden_error, learningRate, command)
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 34, in updateHiddenLayer
    emb.update_embedding_matrix(embedding_error, command, learning_rate)
                                                          ^^^^^^^^^^^^^
NameError: name 'learning_rate' is not defined. Did you mean: 'learningRate'?

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Model trained !

 Please enter a command : it is so dark
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : lamp
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : fan
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : 
[[0.11006262 0.15861064 0.22290908 0.50841766]]


= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Model trained !

 Please enter a command : turn on the fan
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : google
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : fan
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : 
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 36, in <module>
    print(wab.createZMatrix(hl.get_ReluHiddenMatrix(test_command)))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 20, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 14, in get_HiddenHMatrix
    h_matrix = emb.getHMatrix(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/embeddingMatrix.py", line 49, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training
Model trained !

 Please enter a command : turn on the fan
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : hello
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : 
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 36, in <module>
    print(wab.createZMatrix(hl.get_ReluHiddenMatrix(test_command)))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 20, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 14, in get_HiddenHMatrix
    h_matrix = emb.getHMatrix(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/embeddingMatrix.py", line 49, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

============= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py ============
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 3, in <module>
    import weightsAndBias as wab
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 3, in <module>
    import hiddenLayer as hl
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 8, in <module>
    hidden_weight_matrix = np.random.randn((DIMENSION, NEURONS)) * 0.01
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "numpy/random/mtrand.pyx", line 1287, in numpy.random.mtrand.RandomState.randn
  File "numpy/random/mtrand.pyx", line 1448, in numpy.random.mtrand.RandomState.standard_normal
  File "_common.pyx", line 636, in numpy.random._common.cont
TypeError: 'tuple' object cannot be interpreted as an integer

============= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py ============
Starting Training
Model trained !

 Please enter a command : fan
[[0.11006262 0.15861064 0.22290908 0.50841766]]

 Please enter a command : 
= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 20
    sum += np.exp(probability_matrix[i][j])
RuntimeWarning: overflow encountered in exp

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 22
    z_matrix[i][j] = np.exp(probability_matrix[i][j])/sum
RuntimeWarning: overflow encountered in exp

Warning (from warnings module):
  File "/home/divyam/Jarvis/Model3_Relu/weightsAndBias.py", line 22
    z_matrix[i][j] = np.exp(probability_matrix[i][j])/sum
RuntimeWarning: invalid value encountered in scalar divide
Model trained !

 Please enter a command : fan
[[nan nan nan nan]]

 Please enter a command : 
============= RESTART: /home/divyam/Jarvis/Model3_Relu/training.py ============
Starting Training
Model trained !

 Please enter a command : fan
[[1.00000000e+00 3.13321353e-67 3.47297765e-30 6.54861563e-41]]

 Please enter a command : lamp
[[1.37899874e-17 9.99998978e-01 8.85983486e-25 1.02161690e-06]]

 Please enter a command : camera
[[1.21554672e-037 6.89773308e-105 1.00000000e+000 1.03143472e-037]]

 Please enter a command : google
[[1.20011795e-177 4.98263052e-142 1.14115665e-141 1.00000000e+000]]

 Please enter a command : It is hot in here
[[3.99735717e-01 6.00258729e-01 1.00570559e-10 5.55484898e-06]]

 Please enter a command : it is hot
[[7.41876076e-02 9.25806679e-01 2.18081838e-12 5.71311502e-06]]

 Please enter a command : It is dark
[[1.67693251e-10 9.91798798e-01 1.05078140e-07 8.20109678e-03]]

 Please enter a command : My room is dark
[[2.92739546e-04 9.91998884e-01 5.75813026e-06 7.70261845e-03]]

 Please enter a command : turn on the wind
[[5.42305105e-02 1.34515375e-07 9.45599078e-01 1.70276800e-04]]

 Please enter a command : I need some wind
[[9.99850283e-01 1.22737498e-10 1.48133533e-04 1.58345384e-06]]

 Please enter a command : let some airflow
[[3.67996713e-03 9.96311589e-01 5.92685262e-13 8.44374242e-06]]

 Please enter a command : let some air flow
[[9.99999994e-01 6.26770845e-11 7.28784644e-10 5.24552750e-09]]

 Please enter a command : click a picture
[[4.32636618e-10 1.00000000e+00 7.29299071e-18 2.39418458e-11]]

 Please enter a command : turn on the lamp
[[1.36224857e-06 9.99998417e-01 9.01136098e-11 2.20606717e-07]]

 Please enter a command : turn on the fan
[[9.99999994e-01 1.61675396e-21 5.97184806e-09 9.65848703e-13]]

 Please enter a command : turn on the lamp
[[1.36224857e-06 9.99998417e-01 9.01136098e-11 2.20606717e-07]]

 Please enter a command : use the camera
[[2.89742855e-21 2.07070520e-57 1.00000000e+00 5.86148544e-21]]

 Please enter a command : open the camera
[[1.78482501e-14 4.21010471e-39 1.00000000e+00 4.16873430e-14]]

 Please enter a command : click my photo using a camera
[[1.96310077e-07 1.49167700e-22 9.99999778e-01 2.54207137e-08]]

 Please enter a command : google the president of india
[[2.31491287e-45 2.95559836e-31 8.44587748e-38 1.00000000e+00]]

 Please enter a command : google the weather in rohini, Delhi
[[7.95591637e-60 3.14628135e-44 1.00128997e-49 1.00000000e+00]]

 Please enter a command : use the camera
[[2.89742855e-21 2.07070520e-57 1.00000000e+00 5.86148544e-21]]

 Please enter a command : i am sweating
[[9.99675569e-01 1.58589607e-06 2.98147981e-04 2.46967220e-05]]

 Please enter a command : it want to read a book
[[1.14651732e-02 9.14376433e-01 2.37392750e-05 7.41346548e-02]]

 Please enter a command : book
[[9.71146676e-01 2.71071686e-03 5.02115858e-05 2.60923955e-02]]

 Please enter a command : fan
[[1.00000000e+00 3.13321353e-67 3.47297765e-30 6.54861563e-41]]

 Please enter a command : 
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model3_Relu/training.py", line 36, in <module>
    print(wab.createZMatrix(hl.get_ReluHiddenMatrix(test_command)))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 20, in get_ReluHiddenMatrix
    new_matrix = Relu.Relu_forward(get_HiddenHMatrix(input_text))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/hiddenLayer.py", line 14, in get_HiddenHMatrix
    h_matrix = emb.getHMatrix(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model3_Relu/embeddingMatrix.py", line 49, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero
