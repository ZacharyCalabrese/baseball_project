from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    game_type = models.CharField(max_length=1, null=False)
    double_header_sw = models.CharField(max_length=1, null=False)
    location = models.TextField(max_length=100, null=False)
    away_time = models.TimeField(null=False)
    time = models.TimeField(null=False)
    home_time = models.TimeField(null=False)
    home_team_name = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=256, null=True)
    original_date = models.DateField(null=False)
    home_team_city = models.TextField(max_length=100, null=False)
    
    # Foreign reference eventually
    venue_id = models.IntegerField(null=True)
    gameday_sw = models.CharField(max_length=1)
    away_win = models.IntegerField(null=False)
    home_games_back_wildcard = models.CharField(max_length=5, null=False)

    # Foreign reference eventually
    away_team_id = models.IntegerField()
    home_loss = models.IntegerField()
    home_games_back = models.CharField(max_length=5, null=False)
    home_code = models.CharField(max_length=3, null=True)
    home_win = models.IntegerField()

    time_home_lg = models.TimeField(null=True)
    away_name_abbrev = models.CharField(max_length=5)
    league = models.CharField(max_length=5)
    away_games_back = models.CharField(max_length=5, null=False)
    home_file_code = models.CharField(max_length=5)
    away_split_squad = models.CharField(max_length=1)
    time_zone = models.CharField(max_length=2)
    home_team_id = models.IntegerField()
    day = models.CharField(max_length=3)
    time_aw_lg = models.TimeField()
    away_team_city = models.TextField(max_length=100)
    away_code = models.CharField(max_length=5)
    away_games_back_wildcard = models.CharField(max_length=5, null=False)
    scheduled_innings = models.IntegerField()
    first_pitch_et = models.TimeField(null=True)
    away_team_name = models.TextField(max_length=100)
    home_name_abbrev = models.CharField(max_length=5)
    ampm = models.CharField(max_length=2, default='PM')
    home_division = models.CharField(max_length=2)
    home_split_squad = models.CharField(max_length=1)
    home_time_zone = models.CharField(max_length=2)
    away_time_zone = models.CharField(max_length=2)
    hm_lg_ampm = models.CharField(max_length=2)
    hm_ampm = models.CharField(max_length=2)
    venue = models.TextField(max_length=100)
    away_loss = models.IntegerField()
    resume_date = models.DateField(null=True)
    away_file_code = models.CharField(max_length=5)
    aw_lg_ampm = models.CharField(max_length=2)
    aw_ampm = models.CharField(max_length=2)
    away_division = models.CharField(max_length=2)


    #losing pitcher
    #homeruns
    #linescore
    #winning pitcher
    #save pitcher
    #broadcast
    #status
