from django.shortcuts import render
from django.conf import settings
from . import ml_model
import os
from Home.models import Register
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def image(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        image_path = os.path.join(settings.MEDIA_ROOT, 'user uploaded', image_file.name)
        with open(image_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)
        pred = ml_model.pred_Cancer_NonCancer(Cancer_or_NonCancer=image_path)
        print(pred)
        return render(request, 'output.html', {'pred_output': pred, 'user_image': image_path})
    else:
        return render(request, 'image.html')
    
def output(request):
    if request.method == 'POST':
        file = request.FILES['image']
        filename = file.name
        print('@@input post= ', filename)
        file_path = os.path.join(settings.MEDIA_ROOT, 'user uploaded', filename)

        with open(file_path, 'wb') as f:
            f.write(file.read())
            
        print("@@ Predicting class......")
        pred = ml_model.pred_Cancer_NonCancer(Cancer_or_NonCancer=file_path)
        return render(request, 'output.html', {'pred_output': pred, 'user_image': file_path[len(settings.MEDIA_ROOT):]})
    else:
        return render(request, 'output.html')
    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Profile')
        else:
            return redirect('/login')
    else:
        return render(request,'Login.html')


def Registation(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Re_Password = request.POST.get('Re_Password')

        UserRegister = Register(Name = Name, Email = Email, Password = Password, Re_Password = Re_Password)

        UserRegister.save()
        user = User.objects.create_user(Email,Email,Password)
        user.save()
        return redirect('login')
    else:
        return render(request,'Registation.html')
    
def Profile(request):
    return render(request, 'Profile.html')
    
    

