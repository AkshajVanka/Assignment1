from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(requests):
    return HttpResponse('<h1>This is the home page!!!</h1>')

def aboutUs(requests):
    return HttpResponse('<h1>I am a student at Vasavi</h1>')

def myHobbies(requests):
    return HttpResponse('<h1>Cooking, Playing the guitar, Gaming, Sports, etc.</h1>')
