
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from datetime import datetime
from dateutil.relativedelta import relativedelta

""" calculate age
myBirthday = datetime.datetime(1983,5,20,0,0,0,0)
now = datetime.datetime.now()

myBirthday = datetime.datetime(1983,5,20,0,0,0,0)
now = datetime.datetime.now()

"""

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX =re.compile(r'^[a-zA-Z]{3,}$')
PSWD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$')
NUM_REGEX = re.compile(r'^\d{1,120}$')
DESC_REGEX =re.compile(r'^[a-zA-Z0-9 ]{15,}$')

import bcrypt

class usersManager(models.Manager):
    def registration_validator(self, postData):
        today = datetime.now().date()
        errors = {}
        if not NAME_REGEX.match(postData['first_name']):
            errors["first_name"] = "First name must be at least 3 character long and have only letters"
        if not NAME_REGEX.match(postData['last_name']):
            errors["last_name"] = "Last name must be at least 3 character long and have only letters"
        existing = users.objects.filter(email=postData['email'])
        if len(existing) > 0:
            errors["email"] = "Email is already in use"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email2"] = "email must be at least 4 characters long and look like: x@x.x"
        if (int(postData['birthday'][:4])<1900):
            errors['birthday'] = "I seriously doubt you were born before 1900. You don't look one day older than 1905"
        if (datetime.strptime(postData['birthday'],'%Y-%m-%d').date()>today):
            errors['birthday'] = "You can't be born later than today!"
        if not PSWD_REGEX.match(postData['password']):
            errors["password"] = "Password must include letters (capital and lower case, numbers and special characters and be at least 8 characters long)"
        if postData['password'] != postData['cpswd']:
            errors['cpsw'] = "password and confirmation must match"
        return errors
    def register_user(self, postData):
        users_1=users()
        users_1.first_name = postData['first_name']
        users_1.last_name = postData['last_name']
        users_1.email = postData['email']
        pswd = postData['password']
        users_1.password = bcrypt.hashpw(pswd.encode(), bcrypt.gensalt())
        users_1.birthday = postData['birthday']
        users_1.save()
        return users_1
    
    def login_validator(self,postData):
        errors ={}
        user= []
        try: 
            user = users.objects.get(email=postData['email'])
        except:
            errors['login'] = "You have entered the wrong email and/or password"  
            return [errors, user]
        password = postData['password']
        password_db = user.password
        if not bcrypt.checkpw(password.encode(), password_db.encode()):
            errors['login'] = "You have entered the wrong email and/or password"   
        return [errors, user]



class users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length =255)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<\nusers \n\tobject {}:\n \tfirst_name: {}\n \tlast_name: {}\n \temail_address: {}\n \tpassword: '********'\n \birthday: {}\n \tcreated at: {}\n \tupdated at: {}\n>".format(self.id, self.first_name, self.last_name, self.email, self.password, self.birthday, self.created_at, self.updated_at)
    # *************************
    # Connect an instance of Manager to our model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = usersManager()
    # *************************

"""
Let's say we have class players and team:
a tema has many players but a player has only one team -
to set the one-to-many relation between team and player do:

inside the class player (is the many class or if you preffer the class that is related to a unique object in the other class):

class Team(models.Model):
    etc...

class Players(models.Model):
    etc
    team = models.ForeignKey(Team, related_name="player")

**************************************************************

if the relation is many to many ie a player can play for many teams too:
the rerlation can be defiend in either class. Do only one of the following:

class Team(models.Model):
    etc...
    player = models.ManyToManyField(Players, related_name="team")

class Players(models.Model):
    etc
    team = models.ManyToManyField(Team, related_name="player")

"""




