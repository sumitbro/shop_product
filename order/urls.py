
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('customer/<int:id>', views.customer, name='=customer'),
    path('create/<int:id>', views.createview, name='create'),
    path('update/<int:id>', views.updateorder, name='update'),
    path('delete/<int:id>', views.deleteorder, name='delete'),
    path('profile/', views.userpage, name= 'profile'),
    # path('account/', views.account, name='account')




]

