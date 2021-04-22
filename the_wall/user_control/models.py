from django.db import models
import bcrypt
from datetime import datetime
import re


class User_Manager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}

        if len(post_data['first_name_input']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(post_data['last_name_input']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."

        user_list = User.objects.filter(email = post_data['email_input'])

        if len(user_list) > 0:
            errors['email'] = "Email is already in use."

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(post_data['email']):          
            errors['email'] = "Invalid email address!"
        else:
            user_list = User.objects.filter(email = post_data['email_input'])
            if len(user_list) > 0:
                errors['email'] = "Email is already in use."

        if len(post_data['password_input']) < 4:
            errors['password'] = "Password must be at least 4 characters."
        if post_data['password_input'] != post_data['password_check']:
            errors['password_check'] = "Password does not match."

        if len(post_data['date_input']) < 1:
            errors['date'] = "You must enter a birth date."
        else:
            form_date = datetime.strptime(post_data['date_input'], "%Y-%m-%d")
            if datetime.now() < form_date:
                errors["date"] = "Are you a terminator?"
            elif datetime.now().year - form_date.year < 13:
                errors["date"] = "You must be at least 13. Set year to 2007 to proceed. Promise not to lie."
        return errors


    def login_validator(self, post_data):
        errors = {}
        user_list = User.objects.filter(email = post_data['login_email'])
        if len(user_list) > 0:
            user = user_list[0]
            if not bcrypt.checkpw(post_data['login_password'].encode(), user.password.encode()):
                errors['password'] = "Invalid Credentials"
        else:
            errors['email'] = "Invalid Credentials"
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    age=models.DateField()
    email=models.EmailField()
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = User_Manager()