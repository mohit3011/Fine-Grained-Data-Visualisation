import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as anim


from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Post
from .forms import PostForm



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
		messages.success(request, "Successfully Created")
		return redirect('creation')

	context = {"form":form}

	return render(request,"web/uploadfile.html",context)

def creation(request):

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

	return render(request,"web/creation.html")



