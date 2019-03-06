from django.shortcuts import render , get_object_or_404, redirect 
from .models import lsd , cart
from .forms import RawForm

def lsd_details(request,m_id):
	#o = lsd.objects.get(id=m_id)
	o=get_object_or_404(lsd,id=m_id)
	cont = {
	'ob' : o	
	}
	return render(request, "lsd/details.html", cont)

def all_details(request):
	#o = lsd.objects.get(id=m_id)
	o=lsd.objects.all()
	cont = {
	'ob' : o	 
	}
	return render(request, "lsd/all_details.html", cont)


def lsd_delete(request,m_id):
	#o = lsd.objects.get(id=m_id)
	o=get_object_or_404(lsd,id=m_id)
	if request.method == "POST":
		o.delete()
		return redirect("../../") 
	cont = {
	'ob' : o	
	}
	return render(request, "lsd/delete.html", cont)

def lsd_create (request): 
	my_form  = RawForm(request.POST or None ) 
	if my_form.is_valid(): 
		my_form.save()
		return redirect("../../")
	cont ={
	"form"  : my_form
	}
	return render (request, "lsd/create.html",cont)

def cart_v (request):
	my_cart = cart.get_or_new(request)
	obj = my_cart.prod.all()
	return render(request,"cart.html",{'ob':obj})

def add_v(request,m_id):
	my_cart = cart.get_or_new(request)
	if my_cart.prod.filter(id=m_id).first() is None:
		my_cart.prod.add(m_id)
	qs = my_cart.prod.all()
	return render(request,"cart.html" , {'ob':qs })

def del_v(request,m_id):
	my_cart = cart.get_or_new(request)
	my_cart.prod.remove(m_id)
	qs = my_cart.prod.all()
	return render(request,"cart.html" , {'ob':qs })
