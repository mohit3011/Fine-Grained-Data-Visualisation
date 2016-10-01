from scipy.spatial import ConvexHull
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = raw_input()
filename  = str(filename)


img = cv2.imread(filename)
print img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

coord = np.where(np.all(img == (0, 0, 255), axis=-1))
points=[]
plx=[]
ply=[]
it=0
for i in xrange(0,len(coord[0]),50):
	xp=coord[0][i]
	yp=-1*coord[1][i]
	yo=[xp,yp]
	plx.append(xp)
	ply.append(yp)
	print yo
	points.append(yo)
	it=it+1
hull = ConvexHull(points)
plt.plot(plx, ply, 'o')
# plot convex hull polygon
#plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(plx[hull.vertices[0]],points[hull.vertices[1]],'r--',lw=2)
# plot convex full vertices
#plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
plt.show()
cv2.imshow('dst',img)
k = cv2.waitKey(15000)
if k==27 or k==-1:
    cv2.destroyAllWindows()
