from django.urls import path
from .views import clist_view, cmform_v ,cdetails_view, cdelete_v,cupdate_v,regis, login_v ,logout_v 

app_name = "blog" 
urlpatterns =[
	path ("",clist_view.as_view(), name = "list"),
	path ("<int:pk>/",cdetails_view.as_view(), name = "details"),
	path ("<int:pk>/ud",cupdate_v.as_view(), name = "update"),
	path ("<int:pk>/delete/", cdelete_v.as_view(),name ="delete"),
	path ("add/",cmform_v.as_view(), name ="add"),
	path ("regis/",regis.as_view(),name="regis"),
	path ("login/",login_v,name= "login"),
	path ("logout/",logout_v,name= "logout"),
]