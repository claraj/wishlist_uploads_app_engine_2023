import requests 

from .models import CatFact
from django.http import HttpResponse, HttpResponseNotAllowed

def get_cat_fact(request):
    if request.method == 'POST':
        response = requests.get('https://catfact.ninja/fact').json()
        fact = response['fact']
        CatFact(fact=fact).save()
        return HttpResponse(f'Saved fact: {fact}')
    else:
        return HttpResponseNotAllowed(['POST'])

