from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# removed the styles you used here so we use the styles frontend gave which should match design more
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Email", max_length=100,
                               required=True,
                               widget=forms.EmailInput(attrs={'placeholder': 'Oraka514@gmail.com',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(label="Password", max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(label="Confirm", max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'email-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id':'password-input'}))
    
    class Meta:
            model = User
            fields = ['email', 'password']
            
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist, please <a href="/sign up">register</a>')
            if not user.check_password(password):
                raise forms.ValidationError('You have entered the wrong password. <a href="#">Did you forget your password?</a>')
            if not user.is_active:
                raise forms.ValidationError('This account is not active. Please <a href="#">contact support</a>')
            return super(LoginForm, self).clean(*args, **kwargs)