import json
import datetime
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import requests
from .forms import SigninForm


def hotel(request):
    user = request.user
    context = {'username': user.username, }
    return render(request, 'hotel/hotel.html', context)


def about(request):
    user = request.user
    context = {'username': user.username, }
    return render(request, 'hotel/about_us.html', context)


def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/signin/')
    else:
        form = SigninForm()

    context = {'form': form}
    return render(request, 'hotel/sign_up.html', context)

