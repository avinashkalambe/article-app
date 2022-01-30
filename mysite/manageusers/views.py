import email
from django.shortcuts import render, redirect
from .forms import Register, Login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
# Create your views here.

def register(request):
    """ this will register a user

    Args:
        request (): either post or get request 

    Returns:
        [type]: return a render template 
    """
    if request.method == 'POST':
        form = Register(request.POST)       
        if form.is_valid():

            data = {'first_name':form.cleaned_data.get('name'),
            'email':form.cleaned_data.get('email'),
            'password':form.cleaned_data.get('password')
            }
            print(data)
            newuser = User.objects.create_user(username=data['first_name'],email=data['email'],password=data['password'])
            newuser.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form })        

    form = Register()
    return render(request, 'register.html', {'form': form})


def login(request):
    """ this will login a user

    Args:
        request (): either post or get request 

    Returns:
        [type]: return a render template 
    """
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(request,username= form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            print(user)
            if user is not None :
                print("user present")
                login_user(request,user)
                return redirect('home')
            else:            
                return render(request, 'login.html', {'form': form, 'error': 'username or password is invalid'})
        else:
            return render(request, 'login.html', {'form': form})
    
    form = Login()
    return render(request, 'login.html', {'form': form})


def logout(request):
    logout_user(request)
    return redirect('login')
