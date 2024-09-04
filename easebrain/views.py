from django.shortcuts import render
import os


def index(request):
    context = {}
    return render(request, 'easebrain/index.html', context)
