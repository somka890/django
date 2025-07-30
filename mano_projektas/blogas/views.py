from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvykę!'
    }
    return render(request, 'pagrindinis.html', kontekstas)