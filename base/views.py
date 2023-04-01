from django.shortcuts import render
from .models import *

def BaseView():

    context={}
    
    return render(request, '', context)



# Create your views here.
