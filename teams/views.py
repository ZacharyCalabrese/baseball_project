from django.shortcuts import render
from django_tables2   import RequestConfig
from models import Team
from tables import TeamTable

# Create your views here.
def home_page(request):
    teams_object = Team.objects.all()
    table = TeamTable(teams_object)
    RequestConfig(request).configure(table)
    return render(request, 'teams.html', {'teams_object':table})
