import random
import sys

def createRandomData(*args):
    """
        Takes arguments as createRandomData(number of points, upper limit of x,upper limit of y, upper limit of z (optional))

        returns 2/3 lists based on input arguments
    """
    length = len(args)
    num = args[0]
    maxX = args[1]
    maxY = args[2]
    if length == 4:
        maxZ = args[3]
    x=[]
    y=[]
    z=[]
    for i in range(1,int(num)):
        randx = str(random.randint(1,int(maxX)))
        randy = str(random.randint(1,int(maxY)))
        if length == 4:
            randz = str(random.randint(1,int(maxZ)))
        x.append(randx)
        y.append(randy)
        if length == 4:
            z.append(randz)
    list_of_lists = []
    list_of_lists.append(x)
    list_of_lists.append(y)
    if length == 4:
        list_of_lists.append(z)
    return list_of_lists
