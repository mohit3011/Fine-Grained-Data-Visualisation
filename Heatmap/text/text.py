import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import numpy as np
import math
import random

fig = plt.figure()
ax1 = fig.add_subplot(111)

count = []

filename = ""

i = 1

radius = raw_input('Enter radius of circle  >  ')
radius = float(radius)

if len(sys.argv) == 2:
    filename = filename + (sys.argv[1])
else:
    print "! Filename not entered !"

points = []

theta = 360 / float(26)

xd = []
yd = []
color = ['b','g','r','c','m','y','k']
fp = 0

for i in xrange(0,26):
    pair = []
    angle_in_rad = math.radians(float(i)*theta)
    x = radius * (math.cos(angle_in_rad))
    y = radius * (math.sin(angle_in_rad))
    pair.append(x)
    pair.append(y)
    points.append(pair)
    i = i + 1


fileData = open(filename,"r").read()

def add_data():
    global fp
    next_char = fileData[fp]
    print next_char
    if fp > len(fileData):
        pass
    else:
        fp = fp + 1
        ascii_ch = ord(next_char) - ord('a')
        if ascii_ch >= 0 and ascii_ch <= 25:
            xd.append(points[ascii_ch][0])
            yd.append(points[ascii_ch][1])
            print points[ascii_ch][0],points[ascii_ch][1]

def animate(i):
    add_data()
    ax1.clear()
    ax1.plot(xd,yd)

ani = animation.FuncAnimation(fig,animate,interval=10)
for i in range(0,26):
    ax1.text(points[i][0], points[i][1], chr(i + ord('a')), fontsize=5)
plt.show()
