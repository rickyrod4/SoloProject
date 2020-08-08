from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def validations(self, form_data):
        errors = {}
        if(len(form_data['first_name'])<1):
            errors['first_name'] = 'Must enter a first name' 
        if(len(form_data['last_name'])<1):
            errors['last_name'] = 'Must enter a last name' 
        if(len(form_data['email'])<1):
            errors['email'] = 'Must enter an email'
        if(len(form_data['password'])<1):
            errors['password'] = 'Must enter an password'
        if(len(form_data['confirmPassword'])<1):
            errors['confirmPassword'] = 'Must confirm your password'
        if(form_data['password'] != form_data['confirmPassword']):
            errors['confirmPassword'] = 'Passwords do not match'                    
        return errors

    def register(self, form_data):
        hash1 = bcrypt.hashpw(form_data['password'].encode(),bcrypt.gensalt()).decode()
        self.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = hash1
        )

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()