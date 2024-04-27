from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
     return HttpResponse("Welcome")


def index(request):
    return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')
     
@login_required
def secret(request):
    if request.user.groups.filter(name='MUser').exists():
        return render(request,"secret.html")
    else:
        return render(request,"ua.html")