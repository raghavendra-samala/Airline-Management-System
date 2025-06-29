from django.http import HttpResponse
from django.shortcuts import render


def help_main(request):
    return render(request, 'help_main.html')


def homepage(request):
    return render(request, 'homepage.html')

def creators(request):
    return render(request, 'who_we_are.html')
