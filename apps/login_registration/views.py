# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime
import random
from django.contrib import messages

from  .models import users
from ..quotable.models import quotes

# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        return render(request, 'login_registration/index.html')
    return redirect('/quotes')

def create(request):
    errors={}
    if request.method == 'POST':
        errors = users.objects.registration_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            user = users.objects.register_user(request.POST)
            request.session['user_id'] =user.id
            return redirect ('/quotes')

def login(request):
    # errors={}
    # output={}
    if request.method == 'POST':
        output = users.objects.login_validator(request.POST)
        errors = output[0]
        print errors
        if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')
        else:
            user = users.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            return redirect('/quotes')


def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')



def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def goHome(request):
    return redirect('/')
