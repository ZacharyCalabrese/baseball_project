from django.shortcuts import render
from django_tables2   import RequestConfig
import django_tables2 as tables
from django.http import HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from models import Game, HomeRun, Inning
from tables import GameTable, HomeRunTable, WinningPitcherTable, LosingPitcherTable, SavingPitcherTable, InningsTable

def home_page(request):
    return render(request, 'home.html')

def search(request):
    if 'team' in request.GET:
        team = request.GET['team']

        game_object = Game.objects.filter(Q(home_team_name__iexact=team) | Q(away_team_name__iexact=team))
        table = GameTable(game_object)
        RequestConfig(request).configure(table)
        if game_object:
            return render(request, 'home.html',{'game_object': table})
    
    return render(request, 'home.html', {'search_error': True})

def home_runs(request, kwargs):
    home_run_object = HomeRun.objects.filter(game__id = kwargs)
    table = HomeRunTable(home_run_object)
    RequestConfig(request).configure(table)
    if home_run_object:
        return render(request, 'home.html',{'game_object': table})
    return render(request, 'home.html')

def box_score(request, kwargs):
    game_object = Game.objects.get(id = kwargs)

    innings_object = game_object.inning_set.all()
    away_innings = innings_object.filter(team_id = game_object.away_team_id)
    home_line = innings_object.filter(team_id = game_object.home_team_id)
    
    away_innings_date = {k:'0' for (k, v) in zip(range(1,10),range(0, 9))}
    home_innings_date = {k:'0' for (k, v) in zip(range(1,10),range(0, 9))}
    
    data = []
    for inning in away_innings:
        away_innings_date[inning.inning_number] = inning.runs_scored
    away_innings_date['Team'] = game_object.away_team_name
    data.append(away_innings_date)
    
    for inning in home_line:
        home_innings_date[inning.inning_number] = inning.runs_scored
    home_innings_date['Team'] = game_object.home_team_name
    data.append(home_innings_date)
    
    columns = ["Team", "1","2","3","4","5","6","7","8","9"]
    attrs = dict((c, tables.Column()) for c in columns)
    table = type('InningsTable', (tables.Table,), attrs)
    innings_table = table(data, attrs={'class':"table table-nonfluid table-striped table-bordered table-condensed table-responsive"})

    winning_pitcher_object = game_object.winningpitcher_set.all()
    winning_pitcher_table = WinningPitcherTable(winning_pitcher_object)

    losing_pitcher_object = game_object.losingpitcher_set.all()
    losing_pitcher_table = LosingPitcherTable(losing_pitcher_object)

    saving_pitcher_object = game_object.savingpitcher_set.all()
    saving_pitcher_table = SavingPitcherTable(saving_pitcher_object)

    home_run_object = game_object.homerun_set.all()
    if home_run_object:
        home_run_table = HomeRunTable(home_run_object)
        RequestConfig(request).configure(home_run_table)
    else:
        home_run_table = None

    RequestConfig(request).configure(winning_pitcher_table)
    RequestConfig(request).configure(losing_pitcher_table)
    RequestConfig(request).configure(saving_pitcher_table)
    RequestConfig(request).configure(innings_table)
    return render(request, 'box_score.html',{'winning_pitcher_object':winning_pitcher_table,
                                             'losing_pitcher_object':losing_pitcher_table,
                                             'saving_pitcher_object':saving_pitcher_table,
                                             'home_run_object':home_run_table,
                                             'box_score_object':innings_table,})

