#Hey Twin: Given an array, find the rows where all the values are equal.
import numpy as np

arr = np.array([[1,1,1],[1,2,3],[2,2,2]])

def findEqual(array):
    for i in array:
        if np.sum(i)/len(i) == i[0]:
            print(i)

findEqual(arr)