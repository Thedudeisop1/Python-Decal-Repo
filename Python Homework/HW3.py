#HW3 contents

#1. Power of a Number
def powerfunction():
    x = int(input("Enter number for x: "))
    y = int(input("Enter number for y: "))
    if y == 0:
        print("1")
    elif y <= 0:
        print("I don't do negative numbers bruh")
    elif y == 1:
        print(x)
    else:
        z = x
        while y > 1:
            z = x*z
            y -= 1
        print(z)

#2. Minimum and Maximum
def minmax():
    import random
    list = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    max = 0
    for i in list:
        if max >= i:
            max = max
        elif max <= i:
            max = i

    min = 1000
    for i in list:
        if min <= i:
            min = min
        elif min >= i:
            min = i

    tuple = (min,max)
    print(list)
    print(tuple)

#3. Leap Year
def leapyear():
    import random
    year = random.randint(0,10000)
    print(year)
    if year%400 == 0:
        print("True")
    elif year%100 == 0:
        print("False")
    elif year%4 == 0:
        print("True")
    else:
        print("False")

#4. Calculate BMI
def bmi():
    weight = int(input("Enter your weight in pounds (I'll convert it to kg): "))/2.205
    height = float(input("Enter your height in feet (I'll convert it to meters): "))/3.281
    BMI = weight/height**2
    print(BMI)

#5. Rotating Digits
def rotate_digits():
    digits = int(input("Enter a number: "))
    numberofdigits = int(input("How many digits in your number, bro: "))-1
    a = digits%10
    b = digits//10
    c = 10**numberofdigits
    d = a*c
    result = b + d
    print(result)

#6. Min and Max with loops
def minforloop():
    import random
    list = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    min = list[0]
    for i in list:
        if min <= i:
            min = min
        else:
            min = i
    print(list)
    print(min)
def minwhileloop():
    import random
    list = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    howmany = len(list) - 1
    min = list[howmany]
    while howmany >= 0:
        if min >= list[howmany]:
            min = list[howmany]
        howmany = howmany - 1
    print(list)
    print(min)
def maxforloop():
    import random
    list = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    max = list[0]
    for i in list:
        if max >= i:
            max = max
        else:
            max = i
    print(list)
    print(max)
def maxwhileloop():
    import random
    list = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    howmany = len(list) - 1
    max = list[howmany]
    while howmany >= 0:
        if max <= list[howmany]:
            max = list[howmany]
        howmany = howmany - 1
    print(list)
    print(max)

#7. Vowels
def vowels():
    string = input("Enter word(s): ")
    count = 0
    for x in string:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
            count += 1
    print(count, "vowels")

#8. Digital Root
def root():
    integers = input("Enter a number: ")
    count = 0
    for i in integers:
        if i == "1":
            count += 1
        elif i == "2":
            count += 2
        elif i == "3":
            count += 3
        elif i == "4":
            count += 4
        elif i == "5":
            count += 5
        elif i == "6":
            count += 6
        elif i == "7":
            count += 7
        elif i == "8":
            count += 8
        elif i == "9":
            count += 9
    print("Digital root =", count)

#1. Power of a Number
powerfunction()
print("")

#2. Minimum and Maximum
minmax()
print("")

#3. Leap Year
leapyear()
print("")

#4. Calculate BMI
bmi()
print("")

#5. Rotating Digits
rotate_digits()
print("")

#6. Min and Max but with loops
minforloop()
minwhileloop()
maxforloop()
maxwhileloop()
print("")

#7. Vowels
vowels()
print("")

#8. Digital Root
root()
print("")