from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ManfiUser

class ManfiUserCreationForm(UserCreationForm):
    class Meta:
        model = ManfiUser
        fields = ('username', 'email')

class ManfiUserChangeForm(UserChangeForm):
    class Meta:
        model = ManfiUser
        fields = ('username', 'email')