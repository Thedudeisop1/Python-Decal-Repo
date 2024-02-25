list1 = [1,1,1,1,1,1,1,1,1,2,2,2,2,3,4,5,6,6,7,7,7,8]

def removeDuplicates(a):
    for i in a:
        number = a.count(i)
        if number >= 2:
            a.remove(i)
    for i in a:
        number = a.count(i)
        if number >= 2:
            a.remove(i)
    for i in a:
        number = a.count(i)
        if number >= 2:
            a.remove(i)
    print(a)

removeDuplicates(list1)