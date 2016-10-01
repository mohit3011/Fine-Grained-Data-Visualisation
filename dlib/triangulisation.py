#!/usr/bin/python
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
#   This example program shows how to find frontal human faces in an image and
#   estimate their pose.  The pose takes the form of 68 landmarks.  These are
#   points on the face such as the corners of the mouth, along the eyebrows, on
#   the eyes, and so forth.
#
#   This face detector is made using the classic Histogram of Oriented
#   Gradients (HOG) feature combined with a linear classifier, an image pyramid,
#   and sliding window detection scheme.  The pose estimator was created by
#   using dlib's implementation of the paper:
#      One Millisecond Face Alignment with an Ensemble of Regression Trees by
#      Vahid Kazemi and Josephine Sullivan, CVPR 2014
#   and was trained on the iBUG 300-W face landmark dataset.
#
#   Also, note that you can train your own models using dlib's machine learning
#   tools. See train_shape_predictor.py to see an example.
#
#   You can get the shape_predictor_68_face_landmarks.dat file from:
#   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
#
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#   or
#       python setup.py install --yes USE_AVX_INSTRUCTIONS
#   if you have a CPU that supports AVX instructions, since this makes some
#   things run faster.  
#
#   Compiling dlib should work on any operating system so long as you have
#   CMake and boost-python installed.  On Ubuntu, this can be done easily by
#   running the command:
#       sudo apt-get install libboost-python-dev cmake
#
#   Also note that this example requires scikit-image which can be installed
#   via the command:
#       pip install scikit-image
#   Or downloaded from http://scikit-image.org/download.html. 

import random
import sys
import os
import dlib
import glob
from skimage import io
import PIL
from PIL import Image
from resizeimage import resizeimage
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.animation as anim
from time import *

if len(sys.argv) != 3:
    print(
        "Give the path to the trained shape predictor model as the first "
        "argument and then the directory containing the facial images.\n"
        "For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./face_landmark_detection.py shape_predictor_68_face_landmarks.dat ../examples/faces\n"
        "You can download a trained facial shape predictor from:\n"
        "    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
    exit()





basewidth = 700
if sys.argv[2].lower().endswith(('.png', '.jpg', '.jpeg')):
	predictor_path = sys.argv[1]
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(predictor_path)
	win = dlib.image_window()

	orig_stdout = sys.stdout
	fi = open('point.txt','w')
	sys.stdout = fi
	with open(sys.argv[2],'r+b') as f:
		with Image.open(f) as image:
			 cover = resizeimage.resize_cover(image, [700, 700])
	       		 cover.save(sys.argv[2], image.format)


	img = io.imread(sys.argv[2])



	win.clear_overlay()
	win.set_image(img)

	    # Ask the detector to find the bounding boxes of each face. The 1 in the
	    # second argument indicates that we should upsample the image 1 time. This
	    # will make everything bigger and allow us to detect more faces.
	dets = detector(img, 1)
	for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
		#print shape.part(1),shape.part(2)
		shape = predictor(img, d)
		for i in xrange(68):
			print shape.part(i)

		sys.stdout = orig_stdout
		fi.close()

		fi = open('point.txt', 'r')
		plt.title('triplot of user-specified triangulation')
		plt.xlabel('Longitude (degrees)')
		plt.ylabel('Latitude (degrees)')
		plt.show(block=False)
		xp=[]
		yp=[]
		color=['bo-','go-','ro-','co-','mo-','yo-','ko-']
		for line in fi:
			x1 = line[1]+line[2]+ line[3]
			y1 = line[5] + line[6] + line[7]
			x1 = int(x1)
			y1 = -1*int(y1)
			xp.append(x1);
			yp.append(y1);
			print x1,y1
			"""
			if len(xp)>=3:
				plt.triplot(xp,yp,color[len(xp)%7])
				plt.draw()
				plt.pause(0.001)
				plt.clf()
			"""
		plt.triplot(xp,yp)
		plt.draw()
		plt.show()
	#plt.plot(x1,y1,"bo")
	#	plt.figure()
	#plt.gca().set_aspect('equal')
		# Draw the face landmarks on the screen.
		win.add_overlay(shape)

	win.add_overlay(dets)
	dlib.hit_enter_to_continue()

else:
	print "hello\n"
	fi = open(sys.argv[2],'r')
	plt.title('triplot of user-specified triangulation')
	plt.xlabel('Longitude (degrees)')
	plt.ylabel('Latitude (degrees)')
	plt.show(block=False)
	xp=[]
	yp=[]
	color=['bo-','go-','ro-','co-','mo-','yo-','ko-']
	i=0
	for line in fi:
		x1 = line[1]+line[2]+line[3]
		y1 =  line[6]+line[7]+line[8]
		x1 = int(x1)
		y1 = -1*int(y1)
		xp.append(x1);
		yp.append(y1);
		#print x1,y1
		if len(xp)>=3:
			plt.triplot(xp,yp,color[len(xp)%7])
			plt.draw()
			plt.pause(0.001)
			plt.clf()
#plt.plot(x1,y1,"bo")
#	plt.figure()
#plt.gca().set_aspect('equal')
	# Draw the face landmarks on the screen.
