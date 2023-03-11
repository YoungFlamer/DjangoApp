from django.shortcuts import render

from django.contrib.auth import authenticate, login


def registration(request):
    return render(request, 'registration.html')
