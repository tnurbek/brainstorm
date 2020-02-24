from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import SignUpFOrm, LoginForm
from django.contrib.auth import authenticate, login
from passlib.hash import pbkdf2_sha256
from django.core.exceptions import ValidationError
from User.models import Player



def SignUp(request):
    if request.method == 'POST':
        form = SignUpFOrm(request.POST)

        if form.is_valid():
            # enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
            # form.password1 = enc_password
            form.save()
            return HttpResponse('good')
        else:
            return HttpResponse('wrong')
    else:
        form = SignUpFOrm()
        return render(request, 'registration/register.html', {'form':form})



def SignIn(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password= data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('good')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})





# Create your views here.
