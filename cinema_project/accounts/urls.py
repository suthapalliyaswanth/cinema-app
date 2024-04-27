from django.urls import path
from .views import register, user_login, signout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', signout, name='logout'),

]


