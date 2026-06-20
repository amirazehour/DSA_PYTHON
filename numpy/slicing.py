import numpy as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])


#array[slice expression]
#array[start:end:step]
#we have to add the : it's exlusive since without it will select just the column
# print(array[0:3])
# print(array[1:])#:--> till the end
# print(array[0::2])

#row selection
print(array[:,0])#select all colums with index 0
print(array[:,1::2])#select multipl columns

print(array[0:2,0])#ro 0 an 1 colunm 0