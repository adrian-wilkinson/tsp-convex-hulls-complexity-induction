# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

filename = 'multiple.csv'
#load csv data
puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:,1:]
Y = puredata[:,0]

def normalization(x):
    mean_x = [];
    std_x = [];
    X_normalized = x;
    temp = x.shape[1]
    for i in range(temp):
        m = np.mean(x[:, i])
        s = np.std(x[:, i])
        mean_x.append(m)
        std_x.append(s)
        X_normalized[:, i] = (X_normalized[:, i] - m) / s
    return X_normalized, mean_x, std_x

def cost(x,y,theta):
    m = y.size #number of training examples
    predicted = np.dot(x,theta)
    sqErr = (predicted - y)
    J = (1.0) / (2 * m) * np.dot(sqErr.T, sqErr)
    return J
def gradient_descent(x, y, theta, alpha, iterations):
#gradient descent algorithm to find optimal theta values
    m = y.size
#theta size
    theta_n = theta.size  
#cost history  
    J_theta_log = np.zeros(shape=(iterations+1, 1))
#store initial values in to log    
    J_theta_log[0, 0] = cost(x, y, theta)
 
    for i in range(iterations):
        
#split equation in to several parts
        predicted = x.dot(theta)

        for thetas in range(theta_n):
            tmp = x[:,thetas]
            tmp.shape = (m,1)
            err = (predicted - y) * tmp
            theta[thetas][0] = theta[thetas][0] - alpha * (1.0 / m) * err.sum()
        J_theta_log[i+1, 0] = cost(x, y, theta)

    return theta, J_theta_log

#size of training set
m,n = np.shape(X)
#shaping Y to [m,1] matrix
Y.shape = (m, 1)
#Scale features
x_scale, mean_r, std_r = normalization(X)

#Add a column of ones to X as x0=1 
XX = np.ones(shape=(m,1))
XX = np.append(XX,x_scale,1)

#set up initial thetas to 0
theta = np.zeros(shape=(n+1, 1))
#define number of iterations and alpha
iterations = 4000
alpha = 0.001
#calculate theta using gradient descent
theta, J_theta_log = gradient_descent(XX, Y, theta, alpha, iterations)
print(theta)
print(Y[1,:])
#print(J_log)
fig = plt.figure('Cost function convergence')
plt.plot(J_theta_log)
plt.grid(True)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost function convergence')
plt.show()

#test hyphothesis with some values
death_rate=np.array([1.0,
                     (78.0 - mean_r[0])/std_r[0],
                     (284.0 - mean_r[1])/std_r[1],
                     (9.1 - mean_r[2])/std_r[2],
                     (109.0 - mean_r[3])/std_r[3]
                     ]).dot(theta)
print ('Predicted death rate for values (1, 78,   284, 9.1, 109): %f' % (death_rate))

