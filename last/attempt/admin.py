from django.contrib import admin
#from.models import User
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm,UserAdminCreationForm
User=get_user_model()

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields=["email"]
    form=UserAdminChangeForm
    add_form=UserAdminCreationForm
admin.site.register(User,UserAdmin)

from . models import city

class cityname(admin.ModelAdmin):

    list_display = ['id','cyty','counrycode','district','population',]

    class META:

        model=city

admin.site.register (city)

from  . models import   country

class countryname(admin.ModelAdmin):
    class meta:
        model= country
admin.site.register (country)