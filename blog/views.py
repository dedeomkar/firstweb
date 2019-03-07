from django.shortcuts import render,redirect, get_object_or_404
from .models import article
from .forms import mform, uform
from django.urls import reverse
from django.views.generic import( ListView, DetailView, CreateView,UpdateView,DeleteView , View)  
from django.contrib.auth  import authenticate,login,logout
# Create your views here.

class clist_view(ListView):
	template_name='list_all.html'
	queryset=article.objects.all() 
	
class cdetails_view(DetailView):
	template_name = 'details.html'
	queryset = article.objects.all() 

class cmform_v(CreateView):
	template_name = "add.html"
	form_class = mform 
	queryset = article.objects.all()  

class regis(View):
	template_name = "add.html"
	form_class = uform 
	def get(self,request):
		cform = self.form_class(None)
		return render(request,self.template_name, {'form' : cform})

	def post(self,request):
		uform = self.form_class(request.POST)
		if uform.is_valid():
			user = uform.save(commit = False) 			# cz password cant be saved directly
			un = uform.cleaned_data ['username']
			pw = uform.cleaned_data ['password']
			user.set_password(pw)
			user.save()									#user is added 
				#logging in the user now
			user1= authenticate(username = un,password =pw)
			if user1 is not None :
				if user1.is_active:
					login (request,user1)
					return redirect("../../../")
		return render(request,self.template_name, {'form' : uform}) 
 
def login_v (request): 
	if not request.user.is_authenticated: 
		form = uform(request.POST) 
		un = form['username']
		pw = form['password']
		user1 = authenticate(username = un.value(),password = pw.value()) 
		if user1 is not None :
			if user1.is_active:
				login(request,user1) 
				return redirect("../../../")
		elif un.value() is not None: 
			er = {
			'username' : 'error',
			'password' : 'error'
			}
			form = uform(er)
		return render(request,"add.html", {'form':form})
	return redirect ("../../../")

def logout_v (request): 
	logout(request)
	return redirect ("../../../")
 

class cupdate_v(UpdateView):	
	template_name= "add.html"
	form_class= mform
	queryset=article.objects.all()

class cdelete_v(DeleteView):
	template_name="delete.html"
	queryset=article.objects.all()
	
	def get_success_url(self):	
		return reverse("blog:list")
 