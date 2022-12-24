import numpy as np


##################Attributes######################
""" 
a_mul = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])
"""
#print(a_mul.shape)
#print(a_mul.ndim)
#print(a_mul.size)
#print(a_mul.dtype)
#print(a_mul[0])
#print(a_mul[0,1])
#print(a_mul[0,2])
#########################DataTypes##########################

#d = {'1': 'A'}
#a = np.array([[1,2,3],
#                [4,d,6],
#                [7,'8',9]]) #Crash dtype=np.int32
#print(a.dtype)
#print(type(a[1,1]))
##########################Filling arrays#########################
#a = np.full((2,3,4), 9)
#print(a)

#a = np.zeros((3,4,8))
#print(a)

#a = np.ones((3,4,8))
#print(a)

#a = np.empty((5,5,5))
#print(a)

#x_values = np.arange(1,150,3)
#print(x_values)

#x_values = np.linspace(0,1000,200)
#print(x_values)
##########################NAN & INF#########################
#print(np.nan)
#print(np.inf)
#print(np.sqrt(-1))
#print(np.array([10])/0)
##########################MATHEMATICAL OPERATIONS#########################

#l1 = [1,2,3,4,5,6]
#l2 = [7,8,9,10,11,12]
#a1 = np.array([1,2,3])
#a2 = np.array([[1],
#              [2]])

#a = np.array([[1,2,3],
#              [4,5,6]])
#print(np.sqrt(a))
#print(np.sin(a))
#print(a1 + a2)
#############################ARRAY METHODS#############################

#a = np.array([[1,2,3],[4,5,6]])
#a = np.append(a, [7,8,9])
#a = np.insert(a,3 ,[4,5,6])
#print(a)
#print(np.delete(a, 1,0))

######################Structuring Methods########################
#a = np.array([[1,2,3,4,5],
#            [6,7,8,9,10],
#            [11,12,13,14,15],
#            [16,17,18,19,20]])
#print(a.shape)
#print(a.reshape(5,4))
#print(a.reshape(20,))
#print(a.reshape(2,10))
#print(a)
#print(a.flatten())
#print(a.ravel())
#var_1 = a.flatten()
#var_1[2] = 100
#print(var_1)
#print(a)
#var = [v for v in a.flat]
#print(var)
#print(a.transpose())
#print(a.T)
#print(a.swapaxes(0,1))
##################Concatenating,Stacking,Splitting######################

#a = np.array([[1,2,3,4,5],
#            [6,7,8,9,10],
#            [11,12,13,14,15],
#            [16,17,18,19,20]])

#a = np.concatenate((a1, a2), axis = 1)
#a = np.stack((a1,a2))
#a = np.vstack((a1,a2))
#a = np.hstack((a1,a2))

#print(np.split(a, 4, axis = 0))

#####################aggregate Functions #################

#a = np.array([[1,2,3,4,5],
#            [6,7,8,9,10],
#            [11,12,13,14,15],
#            [16,17,18,19,20]])

#print(a.min())
#print(a.max())
#print(a.sum())
#print(a.mean())
#print(a.std())
#print(np.median(a))
#################Numpy Random #################
#numbers = np.random.randint(90 ,100, size=(2,3,4))
#print(numbers)
#numbers_2 = np.random.binomial(10, p = 0.6, size=(5,10))
#print(numbers_2)
#number_3 = np.random.normal(loc = 170, scale = 15,size = (5,10))
#print(number_3)
#numbers = np.random.choice([5,1,4,8,5,623,1], size = (5,10))
#print(numbers)
###################Exporting and Importing################

#a = np.array([[1,2,3,4,5],
#            [6,7,8,9,10],
#            [11,12,13,14,15],
#            [16,17,18,19,20]])
#np.save("myarray.npy", a)
#a = np.load("myarray.npy")
#print(a)
#a = np.array([[1,2,3,4,5],
#            [6,7,8,9,10],
#            [11,12,13,14,15],
#            [16,17,18,19,20]])
#np.savetxt("myarray.csv", a, delimiter =",")
#a = np.loadtxt("myarray.csv")
#print(a)
