from django.shortcuts import render
from django.http import HttpResponse


def setNameAndPosition(request):
    return render(request, 'Home.html', {'name': 'Christopher', 'position': 'Admin'})