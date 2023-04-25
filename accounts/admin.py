from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ManfiUserCreationForm, ManfiUserChangeForm
from .models import ManfiUser

class ManfiUserAdmin(UserAdmin):
    add_form = ManfiUserCreationForm
    form = ManfiUserChangeForm
    model = ManfiUser
    list_display = ['email', 'username',]

admin.site.register(ManfiUser, ManfiUserAdmin)