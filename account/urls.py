from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='home'),
    path('signin', views.signin, name='signin'),
    path('logout', views.signout, name='logout')

]
