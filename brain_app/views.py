from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from .models import UserProfile
import os
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# import tensorflow as tf
from .forms import ImageUploadForm
import cv2
from keras.models import load_model
import numpy as np
from PIL import Image
from datetime import date
from .models import TestResult
from django.contrib.auth.decorators import login_required
from django.urls import reverse


#from tensorflow.keras.preprocessing import image

model = load_model('BrainTumor10Epochs.h5')

def home(request):
    context = {}
    return render(request,'main.html',context)

def overflow_page(request):
    context = {}
    return render(request,'overflow.html',context)

def team(request):
    context = {}
    return render(request,'ourteam.html',context)

##########
def get_className(classNo):
    if classNo == 0:
        return "No Brain Tumor"
    elif classNo == 1:
        return "Yes Brain Tumor"

def getResult(img):
    image = cv2.imread(img)
    image = Image.fromarray(image, 'RGB')
    image = image.resize((64, 64))
    image = np.array(image)
    input_img = np.expand_dims(image, axis=0)
    result = model.predict(input_img)
    return get_className(int(result[0][0]))

def model_page(request):
   if not request.user.is_authenticated:
            
            return redirect(reverse('login_required'))
   
   if request.method == 'POST':
        uploaded_file = request.FILES['file']

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        result = getResult(file_path)

        test_result = TestResult()
        test_result.user = request.user
        test_result.image = uploaded_file
        test_result.date = date.today()
        test_result.result = result
        test_result.save()
        
        # print(result)
        # return redirect('history')
        context = {
            "user" : request.user.email, 
            "result" : result,
        }
        return render(request, 'home.html',context)
   
   context = {
            "user" : request.user.email, 

        }
   return render(request, 'home.html',context)



def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        #username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
       
        password = request.POST['password']
        
        user = User.objects.create_user(
            username=email,
            password=password,
            email=email,
           
        )
        profile = UserProfile.objects.create(
            user=user,
            age =age,
            name=name
        )
       
        user.save()
        profile.save()
        
        return redirect('login')
    
    return render(request, 'Sign_up.html')

def login_view(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to colon model page instead of home 
            return redirect('model')
        else:
            return render(request, 'Log_In.html', {'error': 'Invalid email or password'})
    
    return render(request, 'Log_In.html')

def profile(request):
     if not request.user.is_authenticated:
            
            return redirect(reverse('login_required'))
   
     context = {
       "user" : request.user.email, 
   }
     return render(request,'profile.html',context=context)

def history(request):
     if not request.user.is_authenticated:
            
            return redirect(reverse('login_required'))
   
     #user_profile = UserProfile.objects.get(user=request.user)
     test_results = TestResult.objects.filter(user=request.user)
    
     context = {
          'patient_list' : test_results,
     }
     return render(request,'history.html',context=context)

def signin_required(request):
    
    return render(request, 'sign_in_redirect.html',context={})
