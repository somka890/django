from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvykę!'
    }
    return render(request, 'pagrindinis.html', kontekstas)

def apie(request):
    context = {
        "tekstas": "Čia yra mano svetainė, kurioje demonstruoju, kaip veikia Django viewsai ir šablonai.",
        "pavadinimas": "apie",
    }
    return render(request, template_name='apie.html', context=context)