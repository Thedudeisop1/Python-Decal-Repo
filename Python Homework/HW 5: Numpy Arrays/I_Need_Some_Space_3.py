#Given an array of strings, return an array where each letter in each string is separated by a space.
import numpy as np

myArray = np.array(["Python","is","cool!"])

def spaceBetween(array):
    newArray = np.array([])
    for i in array:
        new = ""
        for k in range(len(i)):
            new = new + " " + i[k]
        new1 = np.append(newArray,new)
        newArray = new1
    print(new1)
    
spaceBetween(myArray)