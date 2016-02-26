from django.shortcuts import render
from django_tables2   import RequestConfig
from django.http import HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from models import Game, HomeRun
from tables import GameTable, HomeRunTable

def home_page(request):
    return render(request, 'home.html')

def search(request):
    if 'team' in request.GET:
        team = request.GET['team']

        game_object = Game.objects.filter(Q(home_team_name__iexact=team) | Q(away_team_name__iexact=team))
        table = GameTable(game_object)
        RequestConfig(request).configure(table)
        if len(game_object):
            return render(request, 'home.html',{'game_object': table})
    
    return render(request, 'home.html', {'search_error': True})

def home_runs(request, kwargs):
    print kwargs
    home_run_object = HomeRun.objects.filter(game__id = kwargs)
    table = HomeRunTable(home_run_object)
    RequestConfig(request).configure(table)
    if home_run_object:
        print 'here'
        return render(request, 'home.html',{'game_object': table})
    return render(request, 'home.html')
