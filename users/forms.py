from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(label=_("phone number"), max_length=20, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "username", "phone_number")


class CustomUserChangeForm(UserChangeForm):
    phone_number = forms.CharField(label=_("phone number"), max_length=20, required=False)

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ("email", "phone_number")