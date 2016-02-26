import datetime
import time
import json
import urllib2
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baseball_project.settings")
django.setup()

from games.models import Game, HomeRun, WinningPitcher, LosingPitcher, SavingPitcher
from dateutil import parser

base_url = "http://mlb.mlb.com/gdcross/components/game/mlb/year_{year}/month_{month}/day_{day}/master_scoreboard.json"

field_names = Game._meta.get_fields()
field_names = [f.name for f in field_names]

def load_month(num_month, year):
    for day in range(1, 32):
        print day
        parsed_json = get_json_response_for_day(num_month, day, year)
        try:
            games = parsed_json['data']['games']['game']
        except KeyError:
            return None

        if isinstance(games, dict):
            add_game_to_db(games)
        else:
            for game in games:
                add_game_to_db(game)

def get_json_response_for_day(month, day, year):
    formatted_url = base_url.format(year=year, month=str(month).zfill(2), day = str(day).zfill(2))
    try:
        response = urllib2.urlopen(formatted_url)
    except urllib2.HTTPError:
        return {}
    json_string = response.read()

    parsed_json = json.loads(json_string)
    return parsed_json

def add_game_to_db(game):
    new_game = Game()
    for k, v in game.iteritems():
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
        elif k == 'home_runs':
            home_runs_object = v 
        elif k == 'winning_pitcher':
            winning_pitcher_object = v
        elif k == 'losing_pitcher':
            losing_pitcher_object = v
        elif k == 'save_pitcher':
            saving_pitcher_object = v

    new_game.save()
    try:
        add_home_runs_to_game(new_game, home_runs_object)
    except UnboundLocalError as e:
        pass

    try:
        add_pitcher_to_game(new_game, winning_pitcher_object, 'winning')
    except UnboundLocalError as e:
        pass

    try:
        add_pitcher_to_game(new_game, losing_pitcher_object, 'losing')
    except UnboundLocalError as e:
        pass

    try:
        add_pitcher_to_game(new_game, saving_pitcher_object, 'saving')
    except UnboundLocalError as e:
        pass

def add_home_runs_to_game(game, home_run_object):
    home_run_field_names = HomeRun._meta.get_fields()
    home_run_field_names = [f.name for f in home_run_field_names]
    def add_home_run_to_game(home_run):
        new_home_run = HomeRun()
        setattr(new_home_run, 'game', game)
        for k, v in home_run.iteritems():
            if k in home_run_field_names and k != 'id':
                if v == 'null' or v == '':
                    setattr(new_home_run, k, None)
                else:
                    setattr(new_home_run, k, v)
            elif k == 'id':
                if v != '':
                    setattr(new_home_run, 'player_id', v)
                else:
                    setattr(new_home_run, 'player_id', 0)
        new_home_run.save()

    home_runs = home_run_object['player']

    if isinstance(home_runs, dict):
        add_home_run_to_game(home_runs)
    else:
        for home_run in home_runs:
            add_home_run_to_game(home_run) 

def add_pitcher_to_game(game, pitcher_object, type):
    if type == 'winning':
        field_names = WinningPitcher._meta.get_fields()
        new_pitcher = WinningPitcher()
    elif type == 'losing':
        field_names = LosingPitcher._meta.get_fields()
        new_pitcher = LosingPitcher()
    elif type == 'saving':
        field_names = SavingPitcher._meta.get_fields()
        new_pitcher = SavingPitcher()

    field_names = [f.name for f in field_names]
    
    setattr(new_pitcher, 'game', game)
    for k, v in pitcher_object.iteritems():
        if k in field_names and k != 'id':
            if v == 'null' or v == '':
                setattr(new_pitcher, k, None)
            elif v == '-':
                setattr(new_pitcher, k, None)
            else:
                setattr(new_pitcher, k, v)
        elif k == 'id':
            if v != '':
                setattr(new_pitcher, 'player_id', v)
            else:
                setattr(new_pitcher, 'player_id', 0)

    new_pitcher.save()
        
if __name__ == '__main__':
    load_month(4, 2015)
