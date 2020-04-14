from django.contrib import admin
from .models import Csuser

# Register your models here.

class CsuserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(Csuser, CsuserAdmin)
