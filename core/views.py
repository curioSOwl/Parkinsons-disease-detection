from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Uploads
from tensorflow.keras.models import load_model
import pandas as pd
import cv2
import numpy as np


global input_image
global input_voice

# Create your views here.
def index(request):
    return render(request,'index.html')


@login_required(login_url='signin')
def userpage(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request,'userpage.html',{'user_profile':user_profile})

def preprocess_voice(request):
    return render(request,'userpage.hmtl')

def preprocess_image(request):
    
    return render(request,'userpage.hmtl')

def svm_prediction(request):
    return render(request,'userpage.hmtl')

def cnn_prediction(request):
    cnnModel = load_model('static/assets/models/spiral.h5')
    return render(request,'userpage.hmtl')

def lr_prediction(request):    
    return render(request,'userpage.hmtl')

def upload(request):
    if request.method == 'POST':
        user=request.user.username
        input_image=request.FILES.get('my_image')
        input_voice=request.FILES.get('my_voice')

        new_post = Uploads.objects.create(user=user, image=input_image,voice=input_voice)
        new_post.save()
        return redirect('/record')

        #to call all the functions after saving the image and voice to the database
        preprocess_image()
        preprocess_voice()
        svm_prediction()
        cnn_prediction()
        lr_prediction()


        return redirect('/userpage')
    else:
        return redirect('/userpage')
    return HttpResponse('<h1>upload view</h1>')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        age =  request.POST['age']
        gender = request.POST['gender']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup')
        else:
            user =  User.objects.create_user(username=email, email=email,password=password)
            user.save()


             #log user in and redirect to settings page
            user_login = auth.authenticate(username=email, password=password)
            auth.login(request, user_login)


            user_model = User.objects.get(username=email)
            new_profile = Profile.objects.create(user=user_model, idusers=user_model.id,firstname=firstname,lastname=lastname,age=age,gender=gender,)
            new_profile.save()
            return redirect('settings')
        
    else:
        return render(request,'signup.html')


def record(request):
    user_profile=Uploads.objects.filter(user=request.user).order_by('created_at')
    context={
        'user_profile':user_profile,
    }

    
    return render(request,'record.html',context)

   

def result(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request,'result.html')
def signin(request):

    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/userpage')
        else:
            messages.info(request,'credentials invalid')
            return redirect('signin')
    return render(request,'loginpage.html')



@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        user_profile.save()
        return redirect('settings')
    return render(request,'settings.html',{'user_profile':user_profile})





@login_required(login_url='signin')    
def logout(request):
    auth.logout(request)
    return redirect('signin')

