from django import forms
from django.contrib.auth.forms import UserCreationForm

KIND = (
    ("user", "add authority 'add'"),
    ("group", "add authority 'change and delete'"),
)

class UserCreateForm(UserCreationForm):
    kind = forms.ChoiceField(label="authority settings", choices=KIND)