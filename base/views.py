from django.shortcuts import render
from .models import *

def mainPage(request):
    products = SmartPhone.objects.all()
    notebooks = Notebook.objects.all()
    context = {'products':products, 'notebooks':notebooks}
    return render(request, 'main.html', context)


# Create your views here.
