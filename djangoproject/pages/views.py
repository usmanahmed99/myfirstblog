from django.shortcuts import render
from pages.namer import MyName

# Create your views here.
def home(request):
	return render(request,"home.html",{})

def about(request):
	return render(request,"about.html",{"my_stuff":MyName(35)})

def contacts(request):
	return render(request,"contacts.html",{})
