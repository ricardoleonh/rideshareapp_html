from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import json


# Create your views here.
def index(request):
    return render(request, 'forms/ajax.html')

def UserNameValidationView(request):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use'}, status=400)
        return JsonResponse({'username_valid': True})
