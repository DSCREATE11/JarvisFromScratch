Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: /home/divyam/Jarvis/Model4_sigmoid/training.py ===========
Starting Training
Model trained !

 Please enter a command : fan
[[9.99997431e-01 2.50984503e-06 4.27149413e-08 1.61861983e-08]]

 Please enter a command : lamp
[[7.17702342e-07 9.99998568e-01 9.55348352e-10 7.13586656e-07]]

 Please enter a command : camera
[[5.14532184e-08 1.14816784e-08 9.99999920e-01 1.69669535e-08]]

 Please enter a command : google
[[2.99609332e-10 5.50111148e-07 4.88163814e-09 9.99999445e-01]]

 Please enter a command : I want to read
[[6.33445016e-04 1.32475640e-07 8.34510461e-01 1.64855962e-01]]

 Please enter a command : Snap the camera
[[9.61546289e-08 2.47806113e-08 9.99999861e-01 1.80561983e-08]]

 Please enter a command : It is so hot, turn on the fan
[[9.99221511e-01 3.81209912e-06 7.72014632e-04 2.66207338e-06]]

 Please enter a command : 
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/divyam/Jarvis/Model4_sigmoid/training.py", line 36, in <module>
    print(wab.createZMatrix(hl.get_ReluHiddenMatrix(test_command)))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model4_sigmoid/hiddenLayer.py", line 19, in get_ReluHiddenMatrix
    return Relu.Relu_forward(get_HiddenHMatrix(input_text))
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model4_sigmoid/hiddenLayer.py", line 14, in get_HiddenHMatrix
    h_matrix = emb.getHMatrix(input_text)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/divyam/Jarvis/Model4_sigmoid/embeddingMatrix.py", line 49, in getHMatrix
    h_matrix[0][j] = sum/rows
                     ~~~^~~~~
ZeroDivisionError: division by zero
