import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


from django.shortcuts import render, get_object_or_404
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

	context = {"form":form}

	return render(request,"web/uploadfile.html",context)


