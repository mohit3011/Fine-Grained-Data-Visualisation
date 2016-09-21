import random
import matplotlib.pyplot as plt

for i in xrange(1,100,10):
    a=[]
    b=[]
    for j in range(1,100000):
        rand1 = random.randrange(1,100000)
        a.append(rand1)
        b.append(i)
    plt.plot(a,b,'ro')
plt.xlabel("point distribution")
plt.ylabel("different iterations")
plt.show()
