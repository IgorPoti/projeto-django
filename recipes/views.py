from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        
        'name': 'Igor Cardoso'})


def sobre(request):
    return render(request, 'recipes/temp.html')


def contato(request):
    return HttpResponse('CONTATO')