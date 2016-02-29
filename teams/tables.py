import django_tables2 as tables
from models import Team
from django_tables2.utils import A
from games.models import Game

class TeamTable(tables.Table):
    team = tables.Column(accessor='club_full_name', verbose_name='Team')
    stadium = tables.Column(accessor='field', verbose_name='Home Field')
    division = tables.Column(accessor='division', verbose_name='Division')
    league = tables.Column(accessor='league', verbose_name='League')
    city = tables.Column(accessor='location', verbose_name='City')
    state = tables.Column(accessor='state_province', verbose_name='State')
    schedule = tables.LinkColumn('teams_schedule', text="View", verbose_name="Team Schedule", args=[A('team_id')]
        ,empty_values=(), accessor='id')
    class Meta:
        #model = Team
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

class ScheduleTable(tables.Table):
    away_team = tables.Column(accessor='away_team_name', verbose_name='Away Team')
    home_team = tables.Column(accessor='home_team_name', verbose_name='Home Team')
    location = tables.Column(accessor='location', verbose_name='Location')
    time = tables.Column(accessor='time', verbose_name='Time')
    date = tables.Column(accessor='original_date', verbose_name='Date')
    stadium = tables.Column(accessor='venue', verbose_name='Stadium')
    class Meta:
        #model = Game
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}
