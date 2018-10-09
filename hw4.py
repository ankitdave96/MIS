import numpy as np
from numpy.linalg import inv

data = import("iris.csv");
data_as_matrix =([0,0,0,0])).as_matrix()
data_as_matrix = np.zeros(150,4)
#diving the input into differts zones by different percentage
percentage = 50;
test = (percentage/100)*150
train = test - train;
training_matrix = np.splt(data_as_matrix,train)
testing matrix = np.split(data_as_matrix,test)
#output will be of the for [001]or [100] etc.
output_set[3][3]={[0,0,1],[0,1,0],[1,0,0]}
#set lamda value and vary it
lambda_set[3]={100,0.01,0.0001};
rang = len(training_matrix)
for i in range(rang)):
out = np.dot(np.transpose(training_matrix[i]), output_set[3][3])
out_class = np.zeors(3,150*(percentage/100))
for i in range(len(X)):
    res = np.dot(np.transpose(W), np.transpose(test[i]))
    for j in range(1, len(result)):
        if result[counter] > max:
            max_index = counter
            max = result[counter]
    out_class.append(max_index)
#put diff values of out_calss to get the confusion matrix for all 3
for i in range(len(out_class[1])):
    if y[i] != out[i]:
        miss += 1
correct = len(out_class) - miss

print(str(miss/len(out_class))+" "str(1- miss/len(out_class)))+" "str(correct/correct+miss))
