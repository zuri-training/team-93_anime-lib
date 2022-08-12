from django.urls import path
from . import views

app_name = 'docs'

urlpatterns = [
    path("best practices/", views.Best_practices.as_view(), name= 'practices'),
    path("how it all works/", views.How_it_all_works.as_view(), name= 'works'),
    path("how to guides/", views.How_to_guides.as_view(), name= 'guides'),
    path("", views.Introduction.as_view(), name= 'intro'),
    path("technical reference/", views.Technical_reference.as_view(), name= 'ref'),
    path("tutorials/", views.Tutorials.as_view(), name= 'tut'),
    path("rate us/", views.Rate_us.as_view(), name= 'rate'),
]