import django_tables2 as tables
from models import Game, HomeRun
from django_tables2.utils import A

class GameTable(tables.Table):
    home_team_city = tables.Column(accessor="home_team_city", verbose_name="Home city")
    home_team_name = tables.Column(accessor="home_team_name", verbose_name="Home team")
    away_team_city = tables.Column(accessor="away_team_city", verbose_name="Away city")
    away_team_name = tables.Column(accessor="away_team_name", verbose_name="Away team")
    location = tables.Column(accessor="location", verbose_name="Location")
    venue = tables.Column(accessor="venue", verbose_name="Venue")
    original_date = tables.Column(accessor="original_date", verbose_name="Date")
    homeruns = tables.LinkColumn("homeruns", text="View",verbose_name="Homeruns",args=[A('id')], empty_values=())



    class Meta:
        #model = Game
        # add class="paleblue" to <table> tag
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

class HomeRunTable(tables.Table):
    class Meta:
        model = HomeRun 
        # add class="paleblue" to <table> tag
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}
