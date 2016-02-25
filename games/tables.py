import django_tables2 as tables
from models import Game

class GameTable(tables.Table):
        class Meta:
            model = Game
            # add class="paleblue" to <table> tag
            attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}

