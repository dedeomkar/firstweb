from django import forms
from .models import lsd

class RawForm (forms.ModelForm):
	name = forms.CharField(label='The name of lsd')
	nos = forms.IntegerField(initial= 0)
	summary = forms.CharField(widget=forms.Textarea(
								attrs={
								"placeholder" : "sum up",
								"cols" : 90
								}))

	class Meta:
		model =lsd 
		fields =[
			'name',
			'nos',
			'summary'
			]

	def clean_name(self,*args,**kwargs):
	    n = self.cleaned_data.get("name")
	    if n=="ffs":
	    	raise forms.ValidationError("incorect name") 
	    return n