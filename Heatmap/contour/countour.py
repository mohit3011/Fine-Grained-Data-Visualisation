from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import randomData
import sys


radius = raw_input("Enter radius > ")
radius = int(radius)
xd=[]
yd=[]

xpos=[]
ypos=[]
zpos=[]

dx=[]
dy=[]
dz=[]

if len(sys.argv) == 1:
    xd,yd=randomData.createRandomData(10000,10000,10000)
else:
    fileData = open(sys.argv[1],"r")
    for line in fileData:
        pair = line.split(',')
        xd.append(pair[0])
        yd.append(pair[1].split('\n')[0])

maxx = 0
maxy = 0

i=0
while i <  len(xd):
    if maxx < xd[i]:
        maxx = xd[i]
    i += 1

i = 0
while i <  len(yd):
    if maxy < yd[i]:
        maxy = yd[i]
    i += 1

maxx = int(maxx)
maxy = int(maxy)


divx = maxx/radius
divy = maxy/radius


i=0
while i <= divy:
    j=0
    while j <= divx:
        xpos.append(j)
        ypos.append(i)
        zpos.append(0)
        dx.append(1)
        dy.append(1)
        dz.append(0)
        j = j + 1
    i = i + 1

i = 0
while i < len(xd):
    px = int(xd[i])/radius
    py = int(yd[i])/radius
    if px + py*divx < len(dz):
        dz[px + py*divx] += 1
    i = i + 1

i = 0
wirex=[]
wirey=[]
wirez=[]


maxz = 0
while i < len(dz):
    if maxz < dz[i]:
        maxz = dz[i]
    i += 1

i = 0
while i < len(xpos):
    if int(dz[i]) >= int(maxz)/2:
        wirex.append(xpos[i])
        wirey.append(ypos[i])
        wirez.append(dz[i])
    i += 1

fig = plt.figure()
fig2 = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color = '#00ceaa')

ax2 = fig2.add_subplot(111,projection='3d')
ax2.plot_wireframe(wirex,wirey,wirez,rstride=radius,cstride=radius)

plt.show()
