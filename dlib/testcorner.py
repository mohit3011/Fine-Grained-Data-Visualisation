from scipy.spatial import ConvexHull
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = raw_input()
filename  = str(filename)


img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

coord = np.where(np.all(img == (0, 0, 255), axis=-1))
plx=[]
ply=[]
point=[]
it=0
for i in xrange(0,len(coord[0]),100):
	xp=coord[0][i]
	yp=-1*coord[1][i]
	plx.append(float(xp))
	ply.append(float(yp))
	point.append([xp,yp])
	it=it+1
points=np.array(point)
flag=[0 for i in xrange(len(points))]
print flag
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
"""
plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r-', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
"""
for simplex in hull.simplices:
	plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
hull_indices = hull.vertices
for i in hull_indices:
	flag[i]=1
cpy=[]
for i in xrange(len(points)):
	if flag[i]!=1:
		cpy.append(points[i])
cpy=np.array(cpy)
hull = ConvexHull(cpy)
for simplex in hull.simplices:
	plt.plot(cpy[simplex, 0], cpy[simplex, 1], 'r-')

plt.show()
cv2.imshow('dst',img)
k = cv2.waitKey(15000)
if k==27 or k==-1:
    cv2.destroyAllWindows()
