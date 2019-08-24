from django.contrib import admin
from .models import Sign

# Register your models here.

class SignAdmin(admin.ModelAdmin):  
    list_display = ('title','description') 

admin.site.register(Sign, SignAdmin)
