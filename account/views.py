from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from order.decorators import unauthenticated_user
from django.contrib.auth.models import Group
from order.models import Customer


from django.contrib import messages

# Create your views here.

@unauthenticated_user
def signup(request):
    
        form= SignupForm()

        if request.method=='POST':
            form= SignupForm(request.POST)
            if form.is_valid():
                user=form.save()
                group= Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(user=user)
                username= form.cleaned_data.get('username')
                messages.success(request,'Account created for '+ username)
                return redirect('/account/signin')

        context={'form':form}
        return render(request,'signup.html', context)


@unauthenticated_user
def signin(request):
    
            if request.method=='POST':
                username= request.POST.get('username')
                password= request.POST.get('password')

                user= authenticate(request,username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                
                else:
                    messages.info(request,'username or password incorrect')
                    # return render(request, 'signin.html')
                
            # context={'form':form}
            return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('/account/signin')