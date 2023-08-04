from django.urls import path
from .views import *
urlpatterns=[

path('first/',first),
path('second/',second),
path('',main),
path('cart/',cart),
path('checkout/',checkout),
path('store/',store),
path('login/',login),
path('register/',register),

]