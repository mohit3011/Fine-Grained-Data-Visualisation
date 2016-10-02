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
    xd,yd=randomData.createRandomData(10000,100,100)
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
        xpos.append(j*radius)
        ypos.append(i*radius)
        zpos.append(0)
        dx.append(radius)
        dy.append(radius)
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

maxz = 0

while i < len(dz):
    if maxz < dz[i]:
        maxz = dz[i]
    i += 1

print maxz

i = 0

shades = ['#9400D3','#4B0082','#0000FF','#00FF00','#FFFF00','#FF0000']

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

divz = float(maxz)/float(6)

i = 0
while i < len(xpos):
    indx = dz[i]/divz
    xposs = []
    xposs.append(xpos[i])
    yposs = []
    yposs.append(ypos[i])
    zposs = []
    zposs.append(zpos[i])
    dxs = []
    dxs.append(dx[i])
    dys = []
    dys.append(dy[i])
    dzs = []
    dzs.append(dz[i])
    ax1.bar3d(xposs, yposs, zposs, dxs, dys, dzs, color = shades[int(indx)-1])
    i += 1

#ax2 = fig2.add_subplot(111,projection='3d')
#ax2.plot_wireframe(wirex,wirey,wirez,rstride=radius,cstride=radius)


plt.show()
