import django_tables2 as tables
from models import Team
from django_tables2.utils import A

class TeamTable(tables.Table):
    team = tables.Column(accessor='club_full_name', verbose_name='Team')
    stadium = tables.Column(accessor='field', verbose_name='Home Field')
    division = tables.Column(accessor='division', verbose_name='Division')
    league = tables.Column(accessor='league', verbose_name='League')
    city = tables.Column(accessor='location', verbose_name='City')
    state = tables.Column(accessor='state_province', verbose_name='State')
    class Meta:
        #model = Team
        attrs = {"class": "table-striped table-bordered table-condensed table-responsive"}
