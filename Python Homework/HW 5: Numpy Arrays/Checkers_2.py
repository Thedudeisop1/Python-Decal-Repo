#Checkers: Create an 8x8 array with a checkerboard pattern of zeros and ones using a slicing + striding approach.
import numpy as np

def checkerboard():
    arrays = np.array([1,0,1,0,1,0,1,0,1])
    a = arrays[0:8]
    b = arrays[1:9]
    finalArray = np.array([a,b,a,b,a,b,a,b])
    print(finalArray)

checkerboard()