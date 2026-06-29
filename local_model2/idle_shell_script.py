Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py ===========
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 10, in <module>
    build_vocabulary("vocabulary.txt")
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 5, in build_vocabulary
    if fp.split():
       ^^^^^^^^
AttributeError: '_io.TextIOWrapper' object has no attribute 'split'

= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 10, in <module>
    build_vocabulary("vocabulary.txt")
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 6, in build_vocabulary
    words.append(fp.split().lower())
                 ^^^^^^^^
AttributeError: '_io.TextIOWrapper' object has no attribute 'split'
>>> 
= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 10, in <module>
    build_vocabulary("vocabulary.txt")
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 6, in build_vocabulary
    words.append(fp.split().lower())
                 ^^^^^^^^
AttributeError: '_io.TextIOWrapper' object has no attribute 'split'
>>> 
= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 10, in <module>
    build_vocabulary("vocabulary.txt")
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 6, in build_vocabulary
    words.append(line.split().lower())
                 ^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'lower'
>>> 
= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
[['the'], ['of'], ['and'], ['to'], ['a'], ['in'], ['for'], ['is'], ['on'], ['that'], ['by'], ['this'], ['with'], ['i'], ['you'], ['it'], ['not'], ['or'], ['be'], ['are'], ['from'], ['at'], ['as'], ['your'], ['all'], ['have'], ['new'], ['more'], ['an'], ['was'], ['we'], ['will'], ['home'], ['can'], ['us'], ['about'], ['if'], ['page'], ['my'], ['has'], ['search'], ['free'], ['but'], ['our'], ['one'], ['other'], ['do'], ['no'], ['information'], ['time']]
>>> 
= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
['the\n', 'of\n', 'and\n', 'to\n', 'a\n', 'in\n', 'for\n', 'is\n', 'on\n', 'that\n', 'by\n', 'this\n', 'with\n', 'i\n', 'you\n', 'it\n', 'not\n', 'or\n', 'be\n', 'are\n', 'from\n', 'at\n', 'as\n', 'your\n', 'all\n', 'have\n', 'new\n', 'more\n', 'an\n', 'was\n', 'we\n', 'will\n', 'home\n', 'can\n', 'us\n', 'about\n', 'if\n', 'page\n', 'my\n', 'has\n', 'search\n', 'free\n', 'but\n', 'our\n', 'one\n', 'other\n', 'do\n', 'no\n', 'information\n', 'time\n']
>>> 
= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 11, in <module>
    build_vocabulary("vocabulary.txt")
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 7, in build_vocabulary
    words.append(token[0].lower())
                 ^^^^^
NameError: name 'token' is not defined. Did you mean: 'tokens'? Or did you forget to import 'token'?

= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 11, in <module>
    build_vocabulary("vocabulary.txt")
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 4, in build_vocabulary
    for line in fp:
ValueError: I/O operation on closed file.

= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py
['the', 'of', 'and', 'to', 'a', 'in', 'for', 'is', 'on', 'that', 'by', 'this', 'with', 'i', 'you', 'it', 'not', 'or', 'be', 'are', 'from', 'at', 'as', 'your', 'all', 'have', 'new', 'more', 'an', 'was', 'we', 'will', 'home', 'can', 'us', 'about', 'if', 'page', 'my', 'has', 'search', 'free', 'but', 'our', 'one', 'other', 'do', 'no', 'information', 'time']

========= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py =========
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 2, in <module>
    import embeddingMatrix as emb
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 2, in <module>
    import wordToIndex as wti
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 11
    for index, word in enumerate(words):
IndentationError: unexpected indent

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 2, in <module>
    import embeddingMatrix as emb
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 4, in <module>
    (words, wordDict) = wti.build_vocabulary("vocabulary.txt")
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 13, in build_vocabulary
    return (words, words_to_index)
                   ^^^^^^^^^^^^^^
NameError: name 'words_to_index' is not defined. Did you mean: 'word_to_index'?

= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 2, in <module>
    import embeddingMatrix as emb
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 4, in <module>
    (words, wordDict) = wti.build_vocabulary("vocabulary.txt")
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/wordToIndex.py", line 12, in build_vocabulary
    words_to_index[word] = index
    ^^^^^^^^^^^^^^
NameError: name 'words_to_index' is not defined. Did you mean: 'word_to_index'?

= RESTART: /home/divyam/Jarvis/local_model2/wordToIndex.py

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 2, in <module>
    import embeddingMatrix as emb
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 7, in <module>
    embedding_matrix = np.random.randn((10000, DIMENSION))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "numpy/random/mtrand.pyx", line 1287, in numpy.random.mtrand.RandomState.randn
  File "numpy/random/mtrand.pyx", line 1448, in numpy.random.mtrand.RandomState.standard_normal
  File "_common.pyx", line 636, in numpy.random._common.cont
TypeError: 'tuple' object cannot be interpreted as an integer

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 29, in <module>
    print(createZMatrix(emb.getHMatrix()))
                        ^^^^^^^^^^^^^^^^
TypeError: getHMatrix() missing 1 required positional argument: 'input_text'

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 29, in <module>
    print(createZMatrix(emb.getHMatrix(dummy_command)))
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 34, in getHMatrix
    tokens = tokenize(raw_sentence)
                      ^^^^^^^^^^^^
NameError: name 'raw_sentence' is not defined

= RESTART: /home/divyam/Jarvis/local_model2/embeddingMatrix.py

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/weightsAndBias.py", line 29, in <module>
    print(createZMatrix(emb.getHMatrix(dummy_command)))
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 44, in getHMatrix
    h_matrix[1][j] = sum/rows
    ~~~~~~~~^^^
IndexError: index 1 is out of bounds for axis 0 with size 1

= RESTART: /home/divyam/Jarvis/local_model2/weightsAndBias.py
[[0.25324524 0.252432   0.24546337 0.24885939]]

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24864479 0.25236486 0.24643089 0.25255946]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 15, in <module>
    for (command, target) in training_data:
                             ^^^^^^^^^^^^^
NameError: name 'training_data' is not defined. Did you mean: 'trainingData'?

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24928507 0.2492628  0.25050607 0.25094607]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 23, in <module>
    emb.update_embedding_matrix(dW, command, learning_rate)
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 70, in update_embedding_matrix
    embedding_matrix[i] -= learning_rate * adjustment_matrix   
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: operands could not be broadcast together with shapes (8,) (8,4) (8,) 

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.25061455 0.2520854  0.25055751 0.24674254]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 23, in <module>
    emb.update_embedding_matrix(dW, command, learning_rate)
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 70, in update_embedding_matrix
    embedding_matrix[i] -= learning_rate * adjustment_matrix   
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: operands could not be broadcast together with shapes (8,) (8,4) (8,) 

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24904469 0.24912583 0.25610851 0.24572097]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 24, in <module>
    emb.update_embedding_matrix(dh, command, learning_rate)
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 54, in update_embedding_matrix
    adjustment_matrix = dh.flatten/len(index_list)
                        ^^
NameError: name 'dh' is not defined

========= RESTART: /home/divyam/Jarvis/local_model2/embeddingMatrix.py ========

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.25482823 0.24935865 0.24725199 0.24856114]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 24, in <module>
    emb.update_embedding_matrix(dh, command, learning_rate)
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 54, in update_embedding_matrix
    adjustment_matrix = dh.flatten/len(index_list)
                        ~~~~~~~~~~^~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'

========= RESTART: /home/divyam/Jarvis/local_model2/embeddingMatrix.py ========

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24855004 0.2516579  0.24943383 0.25035823]]
Starting Training
Model trained !

 Please enter a command : TURN on the fan
[[9.99999996e-01 2.22128072e-12 4.21183143e-09 4.45318171e-11]]

 Please enter a command : it is so hot
[[9.89300505e-01 2.35080833e-05 1.13422516e-03 9.54176207e-03]]

 Please enter a command : say cheese
[[3.34205086e-05 1.87564016e-07 7.21326982e-09 9.99966385e-01]]

 Please enter a command : how is the weather
[[2.27411049e-03 1.86380734e-05 4.03876090e-03 9.93668491e-01]]

 Please enter a command : google the president of india
[[1.46847217e-09 4.19836467e-16 4.39353423e-10 9.99999998e-01]]

 Please enter a command : click my photo
[[6.43293947e-07 9.80261370e-01 2.04242977e-06 1.97359442e-02]]

 Please enter a command : click a picture
[[0.00758289 0.87373739 0.06757299 0.05110673]]

 Please enter a command : picture
[[9.85420472e-06 4.08073809e-03 9.95909141e-01 2.66246576e-07]]

 Please enter a command : take my picture
[[7.74776930e-06 9.99877034e-01 2.65337204e-05 8.86847811e-05]]

 Please enter a command : use camera
[[6.71405379e-14 4.37947127e-16 1.00000000e+00 8.14248728e-11]]

 Please enter a command : record this
[[0.08506942 0.56482153 0.04067231 0.30943675]]

 Please enter a command : take a photograph
[[5.41995601e-01 3.17816498e-01 2.15705822e-06 1.40185744e-01]]

 Please enter a command : lights on
[[2.09284301e-06 7.62210669e-08 7.11841569e-01 2.88156262e-01]]

 Please enter a command : 
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 36, in <module>
    print(wab.createZMatrix(emb.getHMatrix(test_command)))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 44, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24874832 0.24600318 0.25219434 0.25305416]]
Starting Training
Model trained !

 Please enter a command : hh

[[7.41684435e-01 4.41473771e-05 1.27714086e-01 1.30557332e-01]]

 Please enter a command : Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 36, in <module>
    print(wab.createZMatrix(emb.getHMatrix(test_command)))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 44, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.25205015 0.25049674 0.25090818 0.24654493]]
Starting Training
Model trained !

 Please enter a command : turn on the fan
[[9.99999823e-01 2.33698541e-09 1.74852283e-07 2.89639644e-11]]

 Please enter a command : lamp
[[1.19247945e-47 1.00000000e+00 2.04142826e-43 1.28210703e-42]]

 Please enter a command : camera
[[5.60401392e-34 2.77613889e-33 1.00000000e+00 1.19672354e-31]]

 Please enter a command : google
[[4.92888801e-40 4.23457857e-36 2.04764548e-40 1.00000000e+00]]

 Please enter a command : fan
[[1.00000000e+00 5.51260004e-34 9.34043448e-38 3.26219009e-38]]

 Please enter a command : it is hot in here
[[9.96506195e-01 7.86513478e-06 4.27550195e-04 3.05838987e-03]]

 Please enter a command : take me photograph
[[3.47673174e-03 1.95290620e-04 9.70910271e-01 2.54177070e-02]]

 Please enter a command : click a picture
[[5.42257968e-01 1.33800440e-04 2.41295874e-10 4.57608232e-01]]

 Please enter a command : take a picture
[[9.29482420e-01 7.03485890e-04 2.58416203e-05 6.97882528e-02]]

 Please enter a command : capture it
[[9.91833715e-01 2.56105095e-08 8.16625574e-03 3.80794135e-09]]

 Please enter a command : it is dark in here
[[9.66628189e-01 2.79207181e-02 6.25762335e-04 4.82533037e-03]]

 Please enter a command : turn on the lights
[[6.69139591e-04 3.59142467e-03 9.95720674e-01 1.87616353e-05]]

 Please enter a command : 
= RESTART: /home/divyam/Jarvis/local_model2/training.py
[[0.25023044 0.25448553 0.24934193 0.2459421 ]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 16, in <module>
    h_matrix = emb.getHMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 46, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24965255 0.25157216 0.24920187 0.24957342]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 16, in <module>
    h_matrix = emb.getHMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 46, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24632526 0.25232522 0.25232795 0.24902157]]
Starting Training
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/local_model2/training.py", line 18, in <module>
    h_matrix = emb.getHMatrix(command)
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 46, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.25895579 0.24860712 0.24367225 0.24876484]]
Starting Training

Warning (from warnings module):
  File "/home/divyam/Jarvis/local_model2/embeddingMatrix.py", line 59
    adjustment_matrix = dh.flatten()/len(index_list)
RuntimeWarning: divide by zero encountered in divide
Model trained !

 Please enter a command : 
========= RESTART: /home/divyam/Jarvis/local_model2/embeddingMatrix.py ========

============ RESTART: /home/divyam/Jarvis/local_model2/training.py ============
[[0.24961744 0.2490932  0.2526701  0.24861926]]
Starting Training
Model trained !

 Please enter a command : it is dark in here
[[4.51169306e-01 4.16366410e-01 1.32464037e-01 2.46735772e-07]]

 Please enter a command : click a photo
[[5.12923685e-04 9.24016398e-01 2.24478731e-03 7.32258907e-02]]

 Please enter a command : camera
[[9.12687500e-02 1.93860000e-01 7.14674431e-01 1.96819314e-04]]

 Please enter a command : camera
[[9.12687500e-02 1.93860000e-01 7.14674431e-01 1.96819314e-04]]

 Please enter a command : fan
[[9.12687500e-02 1.93860000e-01 7.14674431e-01 1.96819314e-04]]

 Please enter a command : lamp
[[9.12687500e-02 1.93860000e-01 7.14674431e-01 1.96819314e-04]]

 Please enter a command : google
[[1.73369904e-51 1.08673484e-54 2.93830912e-50 1.00000000e+00]]

 Please enter a command : who is the president of India?
[[1.29608584e-05 3.76751444e-05 3.81372055e-04 9.99567992e-01]]

 Please enter a command : write a gmail
[[9.12687500e-02 1.93860000e-01 7.14674431e-01 1.96819314e-04]]

 Please enter a command : send a mail
[[3.46543908e-07 1.06801168e-09 4.93445919e-08 9.99999603e-01]]

 Please enter a command : 
[[9.12687500e-02 1.93860000e-01 7.14674431e-01 1.96819314e-04]]

