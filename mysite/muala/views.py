from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os

from .models import Question

def index(request):
    private_key = os.environ.get('API_PRIVATE_KEY')
    return render(request, 'muala/index.html', {'private_key': private_key})

