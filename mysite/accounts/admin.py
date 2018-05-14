from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

# Register your models here.
@admin.register(User)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields':('username','password')}),
        (gettext_lazy('Personal info'), {'fields':('full_name',)}),
    )
    list_display = ('username', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name')