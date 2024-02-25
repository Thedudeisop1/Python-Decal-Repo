List2D = []

def Making2D(a):
    for i in range(1,25,5):
        list1 = []
        for j in range(5):
            list1.append(i + j)
        a.append(list1)
    print(a)

Making2D(List2D)

#Forgot to indent after defining a function