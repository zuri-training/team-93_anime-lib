from django.urls import path

from .views import SignUpView, homepage, library, login, about


urlpatterns = [
    path("sign up/", SignUpView.as_view(), name="sign up"),
    path('home/', homepage, name = 'home'),
    path('library', library, name = 'library'),
    path('login', login, name = 'login'),
    path('about/<int:id>', about, name = 'about'),
]