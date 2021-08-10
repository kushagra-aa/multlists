from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('new_search', views.new_search, name='new_search')
]
