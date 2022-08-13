from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, authenticate

from .forms import UserRegistrationForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def library(request):
    return render(request, 'library.html')

def main2(request):
    return render(request, 'library2.html')

@login_required(login_url='login')
def account(request):
    return render(request, 'index-account.html')

@login_required(login_url='login')
def download(request):
    return render(request, 'download.html')

@login_required(login_url='login')
def saved(request):
    return render(request, 'saved.html')

@login_required(login_url='login')
def home2(request):
    return render(request, 'home2.html')

def password_reset(request):
    return render(request, 'reset_password.html')

def password_form(request):
    return render(request, 'reset_password_form.html')

def password_done(request):
    return render(request, 'reset_password_done.html')

def password_complete(request):
    return render(request, 'reset_password_complete.html')

def password_confirm(request):
    return render(request, 'reset_password_confirm.html')


class SignUpView(View):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    initial = {'key': 'value'}
    template_name = 'registration/sign up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect('login')

        return render(request, self.template_name, {'form': form})
    
    class LogInView(View):
        form_class = LoginForm
        success_url = reverse_lazy("library")
        initial = {'key': 'value'}
        template_name = 'registration/login.html'
    
        def login(request):
            form = LoginForm(request.POST or None)
            if form.is_valid():
                    email = form.cleaned_data.get('email')
                    password = form.cleaned_data.get('password')
                    user = authenticate(email=email, password=password)
                    login(request, user)
                    return redirect("library")

            context = {
                    'form':form,
            }
            return render(request, "login.html", context)
# Create your views here.
