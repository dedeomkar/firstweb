from django  import forms
from .models import article
from django.contrib.auth.models import User

class mform(forms.ModelForm):
	class Meta:
		model = article
		fields = [
		"name",
		"cate",
		"nos",
		"featu",
		]
class uform (forms.ModelForm):
	class Meta:
		model  = User
		fields = ['username','password','email']