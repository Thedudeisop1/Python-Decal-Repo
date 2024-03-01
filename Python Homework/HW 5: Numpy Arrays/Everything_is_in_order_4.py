#Given a multidimensional matrix, sort the matrix along the columns.
import numpy as np

arr = np.random.randint(1,50,(4,5))
print(arr)

def sorting(a):
    newArray = np.sort(a, axis = 0)
    print(newArray)

sorting(arr)