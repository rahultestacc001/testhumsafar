from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    search_fields = ('name',)


# Register your models here.
admin.site.register(User,UserAdmin)



