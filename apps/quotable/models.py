
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
NAME_REGEX =re.compile(r'^[a-zA-Z]{1,}$')
PSWD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*[appointments appoints!%*?&])[A-Za-z\d%*?&]{8,}$')
NUM_REGEX = re.compile(r'^\d{1,120}$')
DESC_REGEX =re.compile(r'^[a-zA-Z0-9 ]{15,}$')

from ..login_registration.models import users



class quotesManager(models.Manager):
    def quotes_validator(self, postData):
        errors = {}
        if len(postData['quoted_by']) < 3:
            errors['quoted_by'] = "Quote author must be at least 3 characters long"
        if len(postData['quote']) < 10:
            errors['quoted'] = "quote must be at least 10 characters long"
        return errors
    def register_quote(self, postData):
        quotes_1=quotes()
        quotes_1.quoted_by = postData['quoted_by']
        quotes_1.quote = postData['quote']
        quotes_1.user = users.objects.get(id = int( postData['user']))
        quotes_1.save()
        return quotes_1
    def add_favorite(self,postData):
        quotes_1 = quotes.objects.get(id=int(
            postData['quote_id']))
        print "$$$$$$$$$$$$"
        print quotes_1.quote
        users_1 = users.objects.get(id=int(postData['user_id']))
        print users_1.first_name
        quotes_1.fav_user.add(users_1)
        quotes_1.save()
        return quotes_1 
    def remove_favorite(self,postData):
        quotes_1 = quotes.objects.get(id=int(
            postData['quote_id']))
        print "$$$$$$$$$$$$"
        print quotes_1.quote
        users_1 = users.objects.get(id=int(postData['user_id']))
        print users_1.first_name
        quotes_1.fav_user.remove(users_1)
        quotes_1.save()
        return quotes_1 




class quotes(models.Model):
    user = models.ForeignKey(users, related_name ="quote")
    quoted_by = models.CharField(max_length=225)
    quote = models.TextField(null=True)
    fav_user = models.ManyToManyField(users, related_name="fav_quote")    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = quotesManager()
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
    team = models.ManyToManyField(Team, related_name="player

 self join query:

        team=models.ManyToManyField("self", symetrical =False)
        team=models.OneToOneField("self", symetrical =False)




"""



