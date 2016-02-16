from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    game_type = models.CharField(max_length=1, )
    double_header_sw = models.CharField(max_length=1, )
    location = models.TextField(max_length=100, )
    away_time = models.TimeField()
    time = models.TimeField()
    home_time = models.TimeField()
    home_team_name = models.TextField(max_length=100, )
    description = models.TextField(max_length=256, null=True)
    original_date = models.DateField()
    home_team_city = models.TextField(max_length=100, )
    
    # Foreign reference eventually
    venue_id = models.IntegerField(null=True)
    gameday_sw = models.CharField(max_length=1)
    away_win = models.IntegerField()
    home_games_back_wildcard = models.CharField(max_length=5, )

    # Foreign reference eventually
    away_team_id = models.IntegerField()
    home_loss = models.IntegerField()
    home_games_back = models.CharField(max_length=5, )
    home_code = models.CharField(max_length=3, null=True)
    home_win = models.IntegerField()

    time_hm_lg = models.TimeField(null=True)
    away_name_abbrev = models.CharField(max_length=5, null=True)
    league = models.CharField(max_length=5, null=True)
    away_games_back = models.CharField(max_length=5, null=True)
    home_file_code = models.CharField(max_length=5, null=True)
    away_split_squad = models.CharField(max_length=1, null=True)
    time_zone = models.CharField(max_length=2, null=True)
    home_team_id = models.IntegerField()
    day = models.CharField(max_length=3, null=True)
    time_aw_lg = models.TimeField()
    away_team_city = models.TextField(max_length=100)
    away_code = models.CharField(max_length=5, null=True)
    away_games_back_wildcard = models.CharField(max_length=5, null=True)
    scheduled_innings = models.IntegerField()
    first_pitch_et = models.TimeField(null=True)
    away_team_name = models.TextField(max_length=100)
    home_name_abbrev = models.CharField(max_length=5, null=True)
    ampm = models.CharField(max_length=2, null=True)
    home_division = models.CharField(max_length=2, null=True)
    home_split_squad = models.CharField(max_length=1, null=True)
    home_time_zone = models.CharField(max_length=2, null=True)
    away_time_zone = models.CharField(max_length=2, null=True)
    hm_lg_ampm = models.CharField(max_length=2, null=True)
    home_ampm = models.CharField(max_length=2, null=True)
    venue = models.TextField(max_length=100)
    away_loss = models.IntegerField()
    resume_date = models.DateField(null=True)
    away_file_code = models.CharField(max_length=5, null=True)
    aw_lg_ampm = models.CharField(max_length=2, null=True)
    away_ampm = models.CharField(max_length=2, null=True)
    away_division = models.CharField(max_length=2, null=True)


    #losing pitcher
    #homeruns
    #linescore
    #winning pitcher
    #save pitcher
    #broadcast
    #status
