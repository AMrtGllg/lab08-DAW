from django.shortcuts import render
from .models import DestinoTuristico

def inicio(request):
    destinos = DestinoTuristico.objects.all()

    return render(request, 'index.html', {
        'destinos': destinos
    })
