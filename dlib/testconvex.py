from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
import random
filename = raw_input()
filename  = str(filename)
a=1
points=[[] for i in xrange(a)]
for i in xrange(a):
	color=['b-','g-','r-','c-','m-','y-','k-']
	fo=open(filename,'r')
	for line in fo:
		te=line.split(' ')
		points[i].append([te[0],te[1]])
	points[i]=np.array(points[i])
#plt.plot(points[i][:,0], points[i][:,1], 'o')
	plt.show(block=False)
	hull=ConvexHull(points[i])
	for simplex in hull.simplices:
	 	plt.plot(points[i][simplex, 0], points[i][simplex, 1], color[i%7])
		plt.draw()
		plt.pause(0.1)
plt.show(block=False)
plt.figure()
for i in xrange(a):
	plt.plot(points[i][:,0], points[i][:,1], 'o')
plt.show()
#if k==27 or k==-1:
#  cv2.destroyAllWindows()
