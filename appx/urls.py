from django.urls import path
from appx.views import lsd_details, lsd_create, lsd_delete, all_details,cart_v, add_v,del_v

app_name = "lsd"
urlpatterns = [
    path ('details/<int:m_id>/',lsd_details, name="details"),
    path ('details/<int:m_id>/delete/',lsd_delete, name="delete" ),
    path ('details/',all_details,name="all_details"),
    path ('create/',lsd_create,name ="create"),
    path ('cart/',cart_v,name ="cart"),
    path ('details/<int:m_id>/add/',add_v,name = "cart_add"),
    path ('details/<int:m_id>/del/',del_v,name ="del"),
]