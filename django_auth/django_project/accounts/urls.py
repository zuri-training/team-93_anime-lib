from django.urls import path, include

from .views import SignUpView, homepage, library, login, main2, download, saved, account, home2, password_reset, password_complete, password_confirm, password_done, password_form


urlpatterns = [
    path("sign up/", SignUpView.as_view(), name="sign up"),
    path('home/', homepage, name = 'home'),
    path('library', library, name = 'library'),
    path('login', login, name = 'login'),
    path('main2', main2, name = 'main2'),
    path('download', download, name = 'download'),
    path('saved', saved, name = 'saved'),
    path('account', account, name = 'account'),
    path('home2', home2, name="home2"),
    path('password_reset', password_reset, name="password_reset"),
    path('password_complete', password_complete, name="password_complete"),
    path(' password_confirm', password_confirm, name=" password_confirm"),
    path('password_done', password_done, name="password_done"),
    path('password_form', password_form, name="password_form"),
]
