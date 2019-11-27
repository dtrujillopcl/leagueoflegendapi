from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    invocador = 'thediego10x'
    url = 'https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+invocador
    args = { 'api_key': 'RGAPI-994ad1a3-95dd-44ad-9e7f-562684ba95ea' }
    response = requests.get(url, params=args)
    if response.status_code == 200:
        response_json = response.json()
        levelinvocador = response_json['summonerLevel']
        nameinvocador = response_json['name']
        iconoinvocador = response_json['profileIconId']
        data = {
            'icono':iconoinvocador,
            'nombre':nameinvocador,
            'nivel':levelinvocador
        }

    return render(request, 'core/home.html', data)