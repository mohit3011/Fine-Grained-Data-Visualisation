from django.shortcuts import render

#from django.allauth.account.forms import LoginForm, SignupForm

def home(request):
    context = {
        'log': "hello",
    }
    return render(request, 'web/home.html', context)

# Create your views here.
