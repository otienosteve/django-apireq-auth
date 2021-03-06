from ast import Return
from multiprocessing import context
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.shortcuts import redirect, render
# register
# login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from urllib import request
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,CustomRegisterForm,PostForm
from .models import Post
from django.views.decorators.csrf import csrf_exempt
#sjnago rewst framework
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import PostSerializer

import json

def home(request):

    return render(request,'home.html')

def logout_user(request):
    logout(request)
    return redirect('home')
   
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
            usern=form.cleaned_data['email']
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
def cuser(request):
    form=CustomRegisterForm()
    if request.method=='POST':
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse(form)
    context={'form':form}
    return render(request,'customreg.html',context)
@csrf_exempt
def addpost(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            post=form.cleaned_data['post']
            data=Post.objects.filter(post=post).first()
            serialisedData=serializers.serialize('json',[data])
        return JsonResponse({'resp':serialisedData},status=200)




    return HttpResponse("You just called me")

@api_view(['GET'])
def getposts(request):
    data=Post.objects.all()
    serialz=PostSerializer(data,many=True)
    return Response(serialz.data)
    
@api_view(['POST'])
def addpost(request):
    reqdata=PostSerializer(data=request.data)
    if reqdata.is_valid():
        reqdata.save()

    return Response(reqdata.data)
@api_view(['GET'])
def single(request,id):
    inst=Post.objects.get(id=id)
    serdinst=PostSerializer(inst,many=False)
    # query model/db using passed in id
    #return the data to the view in Json format


    return Response(serdinst.data)
@api_view(['DELETE'])
def deletepost(request,id):
    inst=Post.objects.get(id=id)
    inst.delete()
    return Response("ITEM DELETED SUCCESSFULY")

@api_view(['PUT'])
def updatepart(request,id):
    #query the DB
    instnce=Post.objects.get(id=id)
    #serializer (inst==id,req.data)
    updtinst=PostSerializer(instance=instnce,data=request.data)
    # if valid
    if updtinst.is_valid():
        updtinst.save()
    return Response(updtinst.data)
    #save()

#install django restframework
#

# postgres://cagzbadjktqskl:e19305d64cc34d869f29e238dd6ba15d81337d06f982d1cca54eaaca43489874@ec2-54-164-40-66.compute-1.amazonaws.com:5432/da6qr5t4ifav2a
# postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName
#APIS is gjango
#how to access and get data from an API
# urllib/
# djangorestframework
# FastAPI

#make a request to an API
#get the data
# display it in a template


#customise the registration form


#create an authentication backend- (username / password) -(email/ password)