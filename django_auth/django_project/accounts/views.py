from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, authenticate

from .forms import UserRegistrationForm
from .forms import LoginForm

def homepage(request):
    return render(request, 'home.html')


def library(request):
    return render(request, 'library.html')

def about(request,id):
    return render(request, 'about.html',{'id':id})

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
