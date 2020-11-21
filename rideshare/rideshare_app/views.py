from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import bcrypt
from .models import *
import json


# Create your views here.
def index(request):
    return render(request, 'sign_in.html')

def log_in(request):
    return render(request, 'log_in.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def registration(request):
    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST) #to validate the form is completed correctly
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/')
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() #to hash the password
        new_user = User.objects.create ( #to create a new user
            user_name = request.POST['user_name'],
            email = request.POST['email'],
            password = hashed_pw
        )
        request.session['user_user_name'] = new_user.user_name
        request.session['user_email'] = new_user.email
        request.session['user_id'] = new_user.id
        return redirect ('/dashboard')
    return redirect ('/')

def loggedin(request):
    if request.method == 'POST':
        errors = User.objects.log_validator(request.POST) #to validate the form is completed correctly
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/')
        this_user = User.objects.get(email=request.POST['email'])
        request.session['user_email'] = this_user.email
        request.session['user_id'] = this_user.id
        return redirect('/dashboard')
    return redirect('/') 

def logout(request):
    request.session.flush()
    return redirect('/')
