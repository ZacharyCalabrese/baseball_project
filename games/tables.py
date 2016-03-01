import django_tables2 as tables
from models import Game, HomeRun, WinningPitcher, LosingPitcher, SavingPitcher, Inning
from django_tables2.utils import A

class GameTable(tables.Table):
    home_team_city = tables.Column(accessor="home_team_city", verbose_name="Home city")
    home_team_name = tables.Column(accessor="home_team_name", verbose_name="Home team")
    away_team_city = tables.Column(accessor="away_team_city", verbose_name="Away city")
    away_team_name = tables.Column(accessor="away_team_name", verbose_name="Away team")
    location = tables.Column(accessor="location", verbose_name="Location")
    venue = tables.Column(accessor="venue", verbose_name="Venue")
    original_date = tables.Column(accessor="original_date", verbose_name="Date")
    homeruns = tables.LinkColumn("box_score", text="View",verbose_name="Box Score",args=[A('id')], 
            empty_values=(), accessor='id')

    class Meta:
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

class HomeRunTable(tables.Table):
    first_name = tables.Column(accessor="first", verbose_name="First name")
    last_name = tables.Column(accessor="last", verbose_name="Last name")
    inning = tables.Column(accessor="inning", verbose_name="Inning")
    runners = tables.Column(accessor="runners", verbose_name="Runners on")
    numbers = tables.Column(accessor="number", verbose_name="Player number")
    class Meta:
        #model = HomeRun 
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

class WinningPitcherTable(tables.Table):

    class Meta:
        model = WinningPitcher 
        # add class="paleblue" to <table> tag
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}


class LosingPitcherTable(tables.Table):

    class Meta:
        model = LosingPitcher 
        # add class="paleblue" to <table> tag
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

class SavingPitcherTable(tables.Table):
    class Meta:
        model = SavingPitcher
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

class InningsTable(tables.Table):
    #inning_one = tables.Column(accessor="1", verbose_name="1")
    class Meta:
        pass
        #model = Linescore
        #attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}
