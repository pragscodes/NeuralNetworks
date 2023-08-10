import sys
import numpy as np
import matplotlib

inputs =[1.2,5.1,2.1,2.5]
# Unique weights for each neuron so three weights are added
weights1 =[3.1,2.1,8.7,2]
weights2=[2,3,4,1.9]
weights3=[5,2,1,4]

#Similarly the same applies for number of bias 
bias1 = 2
bias2 = 1
bias3=3
#Sum of the neural layer would be input*weight+bias for every neuron here no of neurons are three
output = [inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+bias1,
          inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3]+bias2,
          inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3]+bias3]
          
          
print(output)
