from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
# register
# login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from urllib import request
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SilverUserForm

import json
def home(request):

    return render(request,'home.html')

def logout_user(request):
    logout(request)
    return redirect('home')
def customuser(request):
    form=SilverUserForm()
    if request.method=='POST':
        form=SilverUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'cform.html',{'form':form})    
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse(form)
    context={'form':form}
    return render(request,'register.html',context)

def login_user(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            usern=form.cleaned_data['username']
            passw=form.cleaned_data['password']
            user=authenticate(request,username=usern,password=passw)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    context={'form':form}
    return render(request,'login.html',context)

def api(req):
    res=request.urlopen('https://www.fishwatch.gov/api/species')
    print(res)
    results=res.read()
    print(type(results))
    data=json.loads(results)
    print(type(data))
    
    return render(req,'api.html',{'data':data[3]['Image Gallery']})

#APIS is gjango
#how to access and get data from an API
# urllib/
# djangorestframework
# FastAPI

#make a request to an API
#get the data
# display it in a template