List2D = []

def Making2D(a):
    for i in range(1,25,5):
        list1 = []
        for j in range(5):
            list1.append(i + j)
        for k in list1:
            if k%3 == 0:
                list1.insert(list1.index(k),"?")
                list1.remove(k)
        a.append(list1)
    print(a)

Making2D(List2D)

#Says list indices must be integers or slices, not tuple. Fixed it by not including it
#Says x is not in list. Fixed it by looking up how to access a 2D list