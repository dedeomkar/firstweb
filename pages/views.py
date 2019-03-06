from django.shortcuts import render
from django.http import HttpResponse
from appx.models import lsd
from django.urls import reverse
# Create your views here.
def home_view (request,*args,**kwargs): 
	cont = {
	"text"  : "the dinasours are amazing creatures",
	"num" : 4457, 
	"m_list"  : [22,22,211,332,1] 
	}
	return render(request,"home.html", cont)
 
def search_v(request,*args,**kwargs):
	x = request.GET
	x = x.get('search')
	cont = { 
	"x" : x
	}
	return render(request,"search.html", cont)
  
def about_view (request,*args,**kwargs):
	return render(request,"about.html",{})

def h_view ( *args,**kwargs):
	return HttpResponse("<h1>home yea </h1>")
		