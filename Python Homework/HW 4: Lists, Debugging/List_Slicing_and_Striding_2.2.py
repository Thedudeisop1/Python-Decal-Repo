List = [1,2,3,4,5,6,7,8,9]

def square(List):
    for i in List:
        List.remove(i)
        i = i**2
        List.insert(0,i)
    List.sort()
    print(List)

square(List)

#Had an error where the list assignment index was out of range, I fixed it by adding in a number into my assignment