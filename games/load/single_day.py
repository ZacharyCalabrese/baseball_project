import json
import urllib2

year = 2015
month = 4
day = 28

base_url = "http://mlb.mlb.com/gdcross/components/game/mlb/year_{year}/month_{month}/day_{day}/master_scoreboard.json"

url = base_url.format(year=year, month=str(month).zfill(2), day = str(day).zfill(2))

response = urllib2.urlopen(url)
json_string = response.read()

parsed_json = json.loads(json_string)
for key in parsed_json['data']['games']['game'][0].keys():
    print key
