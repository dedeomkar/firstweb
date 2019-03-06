from django.db import models  
from django.urls import reverse 

# Create your models here.

cc =(
	('a','average'),
	('b','better'),
	('g','good'),
	('bs','best'),
	)

class article (models.Model):
	
	name = models.CharField(max_length= 25)
	cate = models.CharField(max_length= 25)
	nos = models.IntegerField(default=0, blank=True)
	featu = models.CharField(max_length= 55, default="a",choices=cc)

	def get_absolute_url (self):
		return reverse("blog:details",kwargs= {"pk":self.id}) 

	def get_url_delete (self):
		return reverse("blog:delete",kwargs= {"pk":self.id}) 


class tag (models.Model):
	title = models.CharField(max_length= 25)
	tag_of = models.ManyToManyField(article, blank =True)
	
