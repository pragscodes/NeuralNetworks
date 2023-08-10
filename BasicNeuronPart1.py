import sys
import numpy as np
import pandas as pd

# This is a Basic  single neuron with inputs,weights and bias code using python 
#Assume it is a fully connected neural network 
inputs =[1.5,3.1,2.1] 
#every input is associated with unique weight
weights=[3.1,2.8,8.7]

#bias in neural network is a constant used models to shift the activation function
bias = 3
output = inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bias

print(output)


