from django.contrib import admin
from .models import CustomUser,Notes


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Notes)