import datetime
import time
import json
import urllib2
import django
django.setup()

from games.models import Game
from dateutil import parser

year = 2015
month = 4
day = 28

base_url = "http://mlb.mlb.com/gdcross/components/game/mlb/year_{year}/month_{month}/day_{day}/master_scoreboard.json"

url = base_url.format(year=year, month=str(month).zfill(2), day = str(day).zfill(2))

response = urllib2.urlopen(url)
json_string = response.read()

parsed_json = json.loads(json_string)
new_game = Game()
field_names = Game._meta.get_fields()
field_names = [f.name for f in field_names]
for k, v in parsed_json['data']['games']['game'][0].iteritems():
    if k in field_names and k != 'id':
        if 'date' in k:
            try:
                d = datetime.datetime.strptime(v, '%Y/%m/%d')
                setattr(new_game, k, d)
            except ValueError:
                setattr(new_game, k, None)
                pass
        elif 'time_zone' in k:
            setattr(new_game, k, v)
        elif 'time' in k:
            t = v.split(':')
            try:
                if len(t) != 0:
                    t = datetime.time(int(t[0]), int(t[1]))
                    setattr(new_game, k, t)
                else:
                    setattr(new_game, k, None)
            except ValueError:
                setattr(new_game, k, None)
                pass
        else:
            if v != '':
                setattr(new_game, k, v)
            else:
                setattr(new_game, k, None)

new_game.save()
