import numpy as np
import os,sys
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from matplotlib import cm
from scipy.spatial import ConvexHull
import random
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as anim

import matplotlib.animation as animation
import time
import pandas as pd

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Post,Post1
from .forms import PostForm,PostForm1



def index(request):
	stri = "mohit"
	context = {"hello":stri
	   }
	return render(request, "web/index.html", context)





def uploadfile(request):

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		os.chdir("/home/mohit/Sem3/ssad_project/SSAD05/SSAD05/web/web/media_cdn/")
		os.system("mv * point.txt")
		messages.success(request, "Successfully Created")
		return redirect('creationmodel')

	context = {"form":form}

	return render(request,"web/uploadfile.html",context)


def uploadfiletwitter(request):

	form = PostForm1(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return creationtwitter(request, instance.hash1, instance.hash2,instance.hash3)

	context = {"form":form}

	return render(request,"web/uploadfiletwitter.html",context)





def creationmodel(request):

	content = 'point.txt'
	content ='/home/mohit/Sem3/ssad_project/SSAD05/SSAD05/web/web/media_cdn/' + content
	fi = open(content,'r')

	xp=[]
	yp=[]
	zp=[]
	color=['bo-','go-','ro-','co-','mo-','yo-','ko-']
	i=0
	for line in fi:
		x1 = line[1]+line[2]+line[3]
		y1 =  line[6]+line[7]+line[8]
		z1 =  line[6]+line[7]+line[8]


		x1 = int(x1)
		y1 = -1*int(y1)
		z1 = int(z1)
		xp.append(x1)
		yp.append(y1)
		zp.append(z1)

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	ax.plot_trisurf(xp, yp, zp, cmap=cm.jet, linewidth=0.2)
	plt.show()
	return redirect('index')






def creationconvex(request):

	content = 'point.txt'
	content ='/home/mohit/Sem3/ssad_project/SSAD05/SSAD05/web/web/media_cdn/' + content
	fi = open(content,'r')

	a = 20

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
	return redirect('index')







def creationtwitter(request,hash1=None,hash2=None,hash3=None):

	try:
	    import json
	except ImportError:
	    import simplejson as json

	h1 = hash1
	h2 = hash2
	h3 = hash3

	print hash1,hash2,hash3

	color = ['#2ecc71','#2980b9','#c0392b','#f1c40f','#2c3e50']

	ckey = 'fibkxu7Ki2PjXQM13EOpqNoB8'
	csecret = 'aLs6U02RHTl3Hx1XOyF20SuYAfUpAKGJvEWpca1s8JWqqEw7Wg'
	atoken = '744960984230440960-va4hCQfFm43kPT3kbb7BVwX7Xtnj7Wa'
	asecret = 'pCRHlvHBLsTgPymvtzVNiXX6sl44dBPTEmBHpfMFycd63'

	oauth = OAuth(atoken , asecret, ckey, csecret)

	twitter_stream = TwitterStream(auth=oauth)

	filterString = h1+","+h2+","+h3
	iterator = twitter_stream.statuses.filter(track=filterString)


	total_tweets = 0
	t=[]
	cnt_of_h=[0,0,0]
	width = 0.8

	fig,ax = plt.subplots()
	h = [h1,h2,h3]
	x_pos = list(range(len(h)))

	def word_in_text(word,text):
	    word = word.lower()
	    text = text.lower()
	    match = re.search(word,text)
	    if match:
	        return True
	    return False

	def add_data():
	    global total_tweets
	    cnt = 0

	    if total_tweets > 3000:
	        os.system('sleep 1m')
	        os.system('exit')

	    for tweet in iterator:
	        try:
	            x = json.dumps(tweet)
	            j = json.loads(x)
	            tweet_text = j['text']
	            if word_in_text(h1,tweet_text):
	                cnt_of_h[0] += 1
	            if word_in_text(h2,tweet_text):
	                cnt_of_h[1] += 1
	            if word_in_text(h3,tweet_text):
	                cnt_of_h[2] += 1
	        except:
	            continue
	        cnt += 1
	        if cnt == 5:
	            break;
	       
	    total_tweets += 5
	    print total_tweets

	def animate(i):
	    global width
	    add_data()
	    width = 0.5
	    ax.clear()
	    ax.set_ylabel('Number of tweets')
	    stitle = "Ranking : "+h1+" vs. " + h2 + " vs. " + h3
	    ax.set_title(stitle)
	    ax.set_xticks([p+ 0.2*width for p in x_pos])
	    ax.set_xticklabels(h)
	    plt.bar(x_pos, cnt_of_h, width, color='g')


	ani = animation.FuncAnimation(fig,animate,interval=10)

	plt.show()
	return redirect('index')
