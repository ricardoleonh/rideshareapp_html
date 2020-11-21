from django.db import models
import re
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def reg_validator(self, postData):  # Validates the regitration form is complete and the email is not in use
        errors = {}
        if len(postData['user_name']) == 0:
            errors['user_name'] = "User Name is Required"
        if len(postData['user_name']) < 5:
            errors['user_name'] = "User Name must be at least 5 characters long"
        existing_user_name = User.objects.filter(user_name=postData['user_name'])
        if len(existing_user_name) > 0:
            errors['user_name'] = "User Name already in use"
        if len(postData['email']) == 0:
            errors['email'] = "Email is required"
        existing_user = User.objects.filter(email=postData['email'])  #IMPORTANT
        if len(existing_user) > 0:
            errors['email'] = "Email already in use"
        elif not email_regex.match(postData['email']):
            errors['emnail'] = "Invalid Email Format"
        if len(postData['password']) == 0:
            errors['email'] = "Password is required"
        elif len(postData['email']) < 8:
            errors['email'] = "Password must be at least 8 characters long"
        elif postData['password'] != postData['confirm_pw']:
            errors['password'] = "Password and Confirm Password must match!"
        return errors
    
    def log_validator(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors['email'] = "Email is required"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Invalid Email Format"
        existing_user =User.objects.filter(email=postData['email']) #IMPORTANT
        if len(existing_user) != 1: #validates if the user is in the database or not
            errors['email'] = "User not Found!"
        elif len(postData['password']) == 0:
            errors['password'] = "Password Required"
        elif not bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()):
            errors['user_name'] = "User Name and password do no match"
        return errors
    
class User(models.Model):
    user_name = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=40)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
