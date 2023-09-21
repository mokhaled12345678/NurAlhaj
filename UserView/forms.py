from django import forms
from users.models import CustomUser

class NewUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'box'}),
        help_text='Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'box'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password']  # Include 'phone_number' field here
        widgets = {
            'username': forms.TextInput(attrs={'class': 'box'}),
            'email': forms.EmailInput(attrs={'class': 'box'}),
            'phone_number': forms.TextInput(attrs={'class': 'box'}),  # Add widget for 'phone_number'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')

        return email
    
class BookingForm(forms.Form):
    email = forms.CharField(label='email')
    title = forms.CharField(label='Package Title')