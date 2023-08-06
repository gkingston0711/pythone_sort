import random


def createArray(myLen):
    myArray =[]

    for i in range(myLen):
        myArray.append(random.randint(1, 100))
    return myArray