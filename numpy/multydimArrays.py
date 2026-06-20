import numpy as np

#WE NEED A CONSISTENT NUMBER OF ELEMENTS CAN USE A PLACEHOLDER LIKE " "
#this is a 3 dim array
array =np.array([[["A","B","C"],[1,2,3],[True,False,False]],
                 [["E","F","G"],[1,2,3],[True,False,False]],
                 [["K","I","J"],[1,2,3],[True,False,False]]])
print(array.ndim)


#(layers,rows,columns)
print(array.shape)

#chain indexing
print(array[0][0][0])

#numpy multy dim indexing
print(array[1,0,1])

word =array[0,0,0]+array[1,0,0]+array[2,0,1]
print(word)

