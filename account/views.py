from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


from django.contrib import messages

# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form= SignupForm()

        if request.method=='POST':
            form= SignupForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,'Account created for '+ user)
                return redirect('/account/signin')

        context={'form':form}
        return render(request,'signup.html', context)



def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
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