import randomData

x,y = randomData.createRandomData(100000,100,100)

f = open("data.csv","w")

i = 0
while i < len(x):
    s = x[i] + ',' + y[i] + "\n"
    f.write(s)
    i = i + 1
f.close()
