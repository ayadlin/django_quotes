# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime
import random
from django.contrib import messages

from  .models import quotes
from  ..login_registration.models import users

# Create your views here.


def index(request):
    user = users.objects.get(id=request.session['user_id'])
    print user.id
    quote_list = quotes.objects.all()
    favorites = quote_list.filter(fav_user=user)
    all_others = quote_list.exclude(fav_user=user)
    print "********"
    print favorites
    print all_others
    context ={'name':user.first_name, 'quotes': quote_list, 'fav':favorites, 'rest':all_others}
    print quote_list
    print quote_list[0].quote
    return render(request, 'quotable/quotes.html', context)

def create_quote(request):
    if request.method == 'POST':
        errors = quotes.objects.quotes_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            quotes_1 = quotes.objects.register_quote(request.POST)
            quotes_1.save()
        
        return redirect('/quotes')


def dashboard(request):
    return redirect(quotes)

def view_user_quotes(request,user_id):
        user = users.objects.get(id=user_id)
        quote_list=quotes.objects.filter(user_id=user.id)
        number = quote_list.count()
        context={"name":user.first_name, "quotes":quote_list,'count':number}
        return render(request, 'quotable/user.html', context)

def add_favorite(request):
    if request.method == 'POST':
        quotes_1 = quotes.objects.add_favorite(request.POST)
        quotes_1.save()
    return redirect('/quotes')

def remove_favorite(request):
    if request.method == 'POST':
        quotes_1 = quotes.objects.remove_favorite(request.POST)
        quotes_1.save()
    return redirect('/quotes')



def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def goHome(request):
    return redirect('/')