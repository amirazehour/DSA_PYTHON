"""
NUMPY --> NUMERICAL PYTHON

PYTHON is really slow that's why we use numpy

"""

import numpy as np

array = np.array([1,2,3,4,5,6]) # faster than py lists
print(np.__version__)

mylist = [1,2,3,4,5,6]

array = array*2
mylist = mylist*2
print(array)
print(mylist)