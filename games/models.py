from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    game_type = models.CharField(max_length=5, )
    double_header_sw = models.CharField(max_length=5, )
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
    away_win = models.IntegerField(default=0, null=False)
    home_games_back_wildcard = models.CharField(max_length=5, null=True)

    # Foreign reference eventually
    away_team_id = models.IntegerField(null=True)
    home_loss = models.IntegerField(default=0, null=False)
    home_games_back = models.CharField(max_length=5, null=True)
    home_code = models.CharField(max_length=3, null=True)
    home_win = models.IntegerField(default=0, null=False)

    time_hm_lg = models.TimeField(null=True)
    away_name_abbrev = models.CharField(max_length=5, null=True)
    league = models.CharField(max_length=5, null=True)
    away_games_back = models.CharField(max_length=5, null=True)
    home_file_code = models.CharField(max_length=5, null=True)
    away_split_squad = models.CharField(max_length=5, null=True)
    time_zone = models.CharField(max_length=5, null=True)
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
    ampm = models.CharField(max_length=5, null=True)
    home_division = models.CharField(max_length=5, null=True)
    home_split_squad = models.CharField(max_length=5, null=True)
    home_time_zone = models.CharField(max_length=5, null=True)
    away_time_zone = models.CharField(max_length=5, null=True)
    hm_lg_ampm = models.CharField(max_length=5, null=True)
    home_ampm = models.CharField(max_length=5, null=True)
    venue = models.TextField(max_length=100)
    away_loss = models.IntegerField()
    resume_date = models.DateField(null=True)
    away_file_code = models.CharField(max_length=5, null=True)
    aw_lg_ampm = models.CharField(max_length=5, null=True)
    away_ampm = models.CharField(max_length=5, null=True)
    away_division = models.CharField(max_length=5, null=True)


    #losing pitcher
    #homeruns
    #linescore
    #winning pitcher
    #save pitcher
    #broadcast#status

class HomeRun(models.Model):
    player_id = models.IntegerField(null=True)
    std_hr = models.IntegerField(null=True)
    hr = models.IntegerField(null=True)
    last = models.TextField(max_length=200)
    team_code = models.CharField(max_length=3, null=True)
    inning = models.IntegerField(null=True)
    runners = models.IntegerField(default=0, null=True)
    number = models.IntegerField(null=True)
    name_display_roster = models.TextField(max_length=200, null=True)
    first = models.TextField(max_length=200, null=True)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class WinningPitcher(models.Model):
    player_id = models.IntegerField(null=True)
    last = models.TextField(max_length=200, null=True)
    losses = models.IntegerField(null=True)
    era = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    number = models.IntegerField(null=True)
    name_display_roster = models.TextField(max_length=200, null=True)
    first = models.TextField(max_length=200, null=True)
    wins = models.IntegerField(null=True)
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class LosingPitcher(models.Model):
    player_id = models.IntegerField(null=True)

    last = models.TextField(max_length=200, null=True)
    losses = models.IntegerField(null=True)
    era = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    number = models.IntegerField(null=True)
    name_display_roster = models.TextField(max_length=200, null=True)
    first = models.TextField(max_length=200, null=True)
    wins = models.IntegerField(null=True)
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class SavingPitcher(models.Model):
    player_id = models.IntegerField(null=True)
    last = models.TextField(max_length=200, null=True)
    saves = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    era = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    name_display_roster = models.TextField(max_length=200, null=True)
    number = models.IntegerField(null=True)
    svo = models.IntegerField(null=True)
    first = models.TextField(max_length=200, null=True)
    wins = models.IntegerField(null=True)
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
