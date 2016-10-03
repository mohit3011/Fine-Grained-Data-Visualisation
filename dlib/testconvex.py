from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
import random
#filename = raw_input()
#filename  = str(filename)

a=raw_input()
a=int(a)
points=[[] for i in xrange(a)]
for i in xrange(a):
	color=['b-','g-','r-','c-','m-','y-','k-']
	for j in xrange(1,10):
		points[i].append([random.uniform(1,10000),random.uniform(1,10000)])
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
