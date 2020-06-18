
from django.shortcuts import render, redirect


def index(request):
	return redirect(request,'index.html')


def login(request):
	return redirect(request, 'login.html')


def register(request):
	return redirect(request, 'register.html')
