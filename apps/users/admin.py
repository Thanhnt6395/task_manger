from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


from .forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    #TODO: the forms to add and change users instance
    form = UserChangeForm
    add_form = UserCreationForm
    
    #TODO: Các fields được sử dụng để hiển thị User Model
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permisstions'), {'fields': ('is_staff', 'is_active', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    
#TODO: register UserAdmin
admin.site.register(User, UserAdmin)
#TODO: unregister Group model from admin
admin.site.unregister(Group)