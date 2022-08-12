from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('name', 'email', 'address', 'phone_number', 'is_admin')
    list_filter = ('is_admin' , )
    fieldsets = (
        (None,{'fields':('name','email', 'password')}),
        ("Personal info", {'fields':('address','phone_number')}),
        ("Permissions",{'fields':('is_admin')})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('name','email', 'address','phone_number','password1','password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email' ,)
    filter_horizontal = ()
    
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)