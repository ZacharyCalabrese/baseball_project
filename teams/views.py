from django.shortcuts import render
from django_tables2   import RequestConfig
from models import Team
from tables import TeamTable, ScheduleTable
from django.db import connection
from datetime import datetime as dt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home_page(request):
    teams_object = Team.objects.all()
    table = TeamTable(teams_object)
    RequestConfig(request, paginate={"per_page": 35}).configure(table)
    return render(request, 'teams.html', {'teams_object':table})

def schedule(request, id):
    context = request.GET.copy()
    if 'page' in context:
        del context['page']
    if 'year' not in context:
        context['year'] = 2016
        year = 2016
    else:
        year = context['year']
        
    teams_object = Team.objects.filter(team_id = id)
    schedule_by_month = get_tables_separated_by_month(teams_object, year)

    paginator = Paginator(schedule_by_month, 1, allow_empty_first_page=False)

    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'team_schedule.html', {'teams_objects':games,
                                                  'team_id':id,
                                                  'team_name':teams_object[0].club_full_name,
                                                  'params':context,
                                                  })

def get_tables_separated_by_month(teams_object, year):
    year = int(year)
    tables = []
    games = teams_object[0].home_team_games.all() | teams_object[0].away_team_games.all()
    for month in range(1, 13):
        date = dt(year=year, month=month, day=1)
        q = games.filter(original_date__year=date.year, original_date__month=date.month)
        games_table = ScheduleTable(q)
        games_table.paginate(per_page=50)
        tables.append(games_table)

    return tables
