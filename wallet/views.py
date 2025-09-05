from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from .models import Transaction
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

