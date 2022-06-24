from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint 
import os
import random

pp = pprint.PrettyPrinter(indent=2, depth=2)
# number = math.floor(math.random() * 899)
def index(request):
    
    number = random.randint(0,899)
    
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{number}'
    
    API_response = HTTP_Client.get(endpoint)
    responseJSON = API_response.json()
   

    preview_url = responseJSON['sprites']['front_default']
    type_url = responseJSON['types'][0]['type']['url']

    type_response = HTTP_Client.get(type_url)
    typeJSON = type_response.json()
    poke_urls = []
    
    poke_urls.append(preview_url)
    while len(poke_urls) < 6 :
        potPoke_response = HTTP_Client.get(typeJSON['pokemon'][random.randint(0,len(typeJSON['pokemon']))]['pokemon']['url'])
        potPoke_JSON = potPoke_response.json()
        poke_urls.append(potPoke_JSON['sprites']['front_default'])
        
    
    
    response = render(request, 'pages/index.html',{"poke_urls": poke_urls})
    
    return response

def index_params(request, poke_id):

    
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{poke_id}'
    
    API_response = HTTP_Client.get(endpoint)
    responseJSON = API_response.json()
   

    preview_url = responseJSON['sprites']['front_default']
    type_url = responseJSON['types'][0]['type']['url']

    type_response = HTTP_Client.get(type_url)
    typeJSON = type_response.json()
    poke_urls = []
    
    poke_urls.append(preview_url)
    while len(poke_urls) < 6 :
        potPoke_response = HTTP_Client.get(typeJSON['pokemon'][random.randint(0,len(typeJSON['pokemon']))]['pokemon']['url'])
        potPoke_JSON = potPoke_response.json()
        poke_urls.append(potPoke_JSON['sprites']['front_default'])
        
    
    
    response = render(request, 'pages/index.html',{"poke_urls": poke_urls})
    
    return response