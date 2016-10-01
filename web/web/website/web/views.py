from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib import messages




def index(request):
	stri = "mohit"
	context = {"hello":stri
	   }
	return render(request, "web/index.html", context)


