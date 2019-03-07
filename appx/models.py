from django.db import models 
from django.urls import reverse
from django.contrib.auth.models import User
#from django.contrib.auth import is_authenticated
 

class lsd (models.Model):
	name = models.CharField(max_length= 15, blank=False,null=False)
	nos = models.IntegerField(default=0, blank=False)
	summary = models.TextField(default= "its dope..")
		
	def get_url(self):
		return reverse("lsd:details",kwargs={"m_id":self.id})
	def get_url_all(self):
		return reverse("lsd:all_details")
	def get_url_delete(self):
		return reverse("lsd:delete",kwargs={"m_id":self.id})

class cart (models.Model):
	user1 = models.ForeignKey(User, blank =True, null = True, on_delete = models.SET_NULL) 
	prod  = models.ManyToManyField (lsd, blank =True)
	total = models.IntegerField(default = 0)

	def create (request): 
		if request.user.is_authenticated: 
			cartx = cart.objects.filter(user1 = request.user).first() 
			if  cartx is None:
				cartx = cart.objects.create(user1 = request.user)
			else :
				cartx.user1 = request.user
			return cartx  
		return cart.objects.create(user1 = None)

	def get_or_new(request):
		cartid = request.session.get('cart_id',None)
		print (cartid)
		my_cart= cart.objects.filter(id=cartid)
		if my_cart.count() == 1:
			my_cart = my_cart.first()
			if request.user.is_authenticated and my_cart.user1 is None:
			 	my_cart.user1 = request.user 
			 	my_cart.save()
		else :
			my_cart = cart.create(request)
			request.session['cart_id'] = my_cart.id 
			my_cart.save()
		return my_cart
 