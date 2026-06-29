
### Pre-processing the data

Before we can feed the commands into the model we need to process the data into a standard format. We perform mainly two functions to create the processed bits or *tokens*

-  First, we split the command into a list. It should be noted that actual models may split the command at random points (creating chunks with parts of words) but here, for simplicity, we would be splitting the command into its component words

- We remove spaces and special characters from the list and turn everything to lowercase. The reason why we turn everything lowercase is so that the word Help and help are not seen as different but the same word

After performing these two functions, we can get a list of *normalized text* or *tokens* from a given command which can be fed into the network

### Bag of Words and Vectors

A bag of Words refers to a list of common words that prove to be meaningful in determining the intent of a given command (check Matrix_multiplication.py to see the bag of words used).
Now we use this bag of words and our list of tokens to create another numerical list called a vector. One can imagine a vector to be an array of switches, if the given token has a word present in our bag of words it is turned on (given a value one) otherwise it is kept at 0. 

[[One must keep in mind the length of this vector is equal to the length of words in the bag of words

### Weights and Bias Matrices

[[Before we move onto this part it is highly recommended to brush up on the concepts of linear regression

Now, in order to predict which command which belongs to which class, we want to somehow convert our vectors into matrix having probability of each respective class (in this case 4). To do this we introduce two new matrices the weights and the bias.
The dimension of the weight matrix is (no of tokens in bag of words, no of classes) and the bias matrix has the dimensions (1, number of classes). Now we create the probability matrix (Z) as:
 $$Z = H \cdot W + b$$

where H represents the vector. But doing this alone does not guarantee that the output matrix (z) would come out as a probability of each class with a total sum of one i.e. we may get a z matrix of sort [12,1,-45,300] which is not favorable. Thus we use the *softmax function*.
The softmax function is a mathematical function which allows us to convert the values in a matrix to probabilities in which the total sum of values in each row turns out  to be one. It is mathematically defined as:

$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{C} e^{z_j}}$$
 
 where i represents the ith row and j represents the jth column and c represents the number of columns/number of classes. You can see the softmax function used in matrix_multiplication.py

### Feed-forward pass

 So, in order to get a prediction, we pass a command through normalization first which returns a list of words. Then, this list of words is passed on to create a vector based on the given bag of words. This vector also known as *h vector* is multiplied (dot product) with the weight matrix and added to the bias matrix to give the output matrix. Now in order to get the probability we use the softmax function creating the final or z_matrix.
 
Then we select the class with the highest probability using the *argmax* function.

### Calculating the error and Training

The result of the feed-forward pass is a matrix with number of columns equal to the number of classes along with the probability of each class.

Before we move forward, we must understand what training data is and it's format. Training data refers to a set of pre-defined commands and their ideal predictions. In our case the training data may be a tuple containing a string "Turn on the fan" and a z matrix [1,0,0,0] where the first class represents fan, while the other 3 refer to some other object.

When we pass the same command through our model, it may produce a matrix like [0.85, 0.05,0.1,0] or something completely off like [0.25,0.5,0.12,0.13] now, in order to correct our weights and bias we would like to calculate the error in prediction, which we do by subtracting the predicted value from the ideal case([1,0,0,0]) i.e.:

$$\mathbf{E} = \hat{\mathbf{y}} - \mathbf{y}$$

here E is called the *error gradient*. Now in order to calculate the actual error in the bias and weight respectively, we need to take the partial derivative of the z_matrix formula. 
[[Recall that in linear regression we used the same method to calculate the error in slope and constant. Here, the slope is the same as the weight matrix and the constant is same as the bias matrix. 
On performing the calculations we get the error in the weights and bias as:

$$\mathbf{dW} = \mathbf{x}^T \cdot \mathbf{E}$$
$$\mathbf{db} = \mathbf{E}$$

Now, we use this error to update the weight and bias matrix as follows. This is known as back-propagation 

$$\mathbf{W}_{\text{new}} = \mathbf{W}_{\text{old}} - (\alpha \cdot \mathbf{dW})$$
$$\mathbf{b}_{\text{new}} = \mathbf{b}_{\text{old}} - (\alpha \cdot \mathbf{E})$$

here alpha $(\alpha)$ refers to the *learning rate*. One can imagine the training process as taking small steps in the form of changes in the weight and bias matrix in order to achieve a minima of error in the prediction. If the steps are too big, we would fail to get fine tuned models whereas if the step is too large, we would basically remain at the same place even after a lot of training. By multiplying the error with the learning rate we make sure we do not make any drastic/insignificant change to the matrices.
[[It may be noted that we have used a learning rate of 0.01 in our small model, though, in llms learning rate of e-4 are common.

### One Hot Encoding Matrix

One hot encoding matrix is a better way to prepare the training dataset. Imagine an identity matrix of n dimensions where n refers to the number of classes, now for any given ith class, the ideal z_vector is just ith row of this identity matrix which is known as one hot encoding matrix.
Now if the 2nd class in my four classes is lamp, instead of having the vector [0,1,0,0] associated with the command, I can just associate the integer 1 and look into the matrix at the row with index 1 (i.e. the second row from top)

### Repeating the Training (Epochs)

The process mentioned above follows through the life of a single command in feed-forward and back propagation. During training we use sets of data containing thousands to lakhs of such examples depending about the vocabulary size and number of classes. 
[[In this case our trainingData.py consists of a 1000 tuples with training examples

Now, the number of times we move through this entire dataset is called an *epoch*. One must be careful while setting up the number of epochs while training. if the number is too less the model would be poorly trained but if the number is kept to high (like 500 for our case), the model *overfits* i.e. it simply memorizes the commands exactly as they are.

### Implementing the Code

Let us individually go through what each program file in the folder does:

- Input_Text_Processor.py
	This program file takes in raw command and returns a list of normalized words (tokens) through the  `process_string(raw_string)` function
	
-  Vectorization.py
	This program takes in the bag of words and the list of tokens and returns the h vector through the ``Create_vector(input_list, bag_of_words)`` function.
	
- Matrix_multiplication.py
	This is the main site of action of this model. It contains the weight matrix, bias matrix, bag_of_words, learning rate and the softmax function
	It also houses the ``create_zmatrix(raw_string)`` function which takes in the raw string, employs the above mentioned functions and returns the final z matrix
	
- training.py
	This file is responsible for pulling the z matrices, calculating the error and feeding it back to the netword during training
	
- training_data.py
	Contains the set of commands with their correct class as tuples to be used during training