listA = [1,2,3,4,5,6,7,8,9,10]
listB = [20,21,22,23,24,25,26,27,28,29,30]

def OddList(listA,listB):
    NewList = []
    for i in listA:
        if i%2 == 1:
            NewList.append(i)
    for i in listB:
        if i%2 == 1:
            NewList.append(i)
    print(NewList)

OddList(listA,listB)

#No errors