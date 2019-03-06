from django.contrib import admin

# Register your models here.
from .models import lsd
from .models import cart

admin.site.register(lsd)
admin.site.register(cart)