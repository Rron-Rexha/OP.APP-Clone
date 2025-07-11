import requests, json, os, time, math
from datetime import datetime, timezone

api_key = "RGAPI-0340816b-f6d0-4788-a807-f005932afb3a"

perk = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perks.json"
perk_styles = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perkstyles.json"

perk_json = requests.get(perk).json()
perk_styles_json = requests.get(perk).json()

def account_info_by_name(username, tagline): # Returns players puuid
  account_request_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tagline}?api_key={api_key}"
  account_info_by_name = requests.get(account_request_url).json()
  player_puuid = account_info_by_name['puuid']
  return player_puuid

def matches_list(player_puuid): # Returns matchid of last 20 matches in list
  match_puuid_request_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?start=0&count=20&api_key={api_key}"
  matches_list = requests.get(match_puuid_request_url).json()
  return matches_list

def match_info_overall(match_id, player_puuid): # Returns relevant match data that is shared between all players such as game time, date game was played, etc.
  match_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
  match_info_overall_json = requests.get(match_url).json()

  player_index = match_info_overall_json['metadata']['participants'].index(player_puuid)

  game_type = match_info_overall_json['info']['queueId']
  
  game_date = datetime.fromtimestamp(game_ms / 1000, tz=timezone.utc).strftime('%m/%d/%Y')
  did_win = match_info_overall_json['info']['participants'][player_index]['win']
  
  game_ms = match_info_overall_json['info']['gameCreation']
  game_dur_sec = match_info_overall_json['info']['gameDuration']
  min_game, game_sec = divmod(game_dur_sec, 60)
  game_hour, min_game = divmod(min_game, 60)
  if game_hour > 0:
    game_duration = f"{game_hour}h {min_game}m {game_sec}s"
  else:
    game_duration = f"{min_game}m {game_sec}s"
  
  player_champion = match_info_overall_json['info']['participants'][player_index]['championName']

  player_summoner1 = match_info_overall_json['info']['participants'][player_index]['summoner1Id']
  player_summoner2 = match_info_overall_json['info']['participants'][player_index]['summoner1Id']

  
  
  major_rune = 
  minor_rune = 

  players_kills = match_info_overall_json['info']['participants'][player_index]['kills']
  players_deaths = match_info_overall_json['info']['participants'][player_index]['deaths']
  players_assists = match_info_overall_json['info']['participants'][player_index]['assists']

  item0 =
  item1 =
  item2 =
  item3 =
  item4 =
  item5 =
  item6 =




def match_info_player_specific(match_id, player_puuid): # Returns specific match data for a specific player such as kills, deaths, assists, etc.
  match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/" + match_id + "?api_key=" + api_key
  resp = requests.get(match_url)
  match_info_overall_json = resp.json()


  player_champion = match_info_overall_json['info']['participants'][player_index]['championName']

  
  player_kda = (players_kills + players_assists) / max(1, players_deaths)



acc_info = account_info_by_name(input(), input())
plyr_puuid = account_puuid(acc_info)
match_list = matches_list(plyr_puuid)[0]
# icon = profile_icon(plyr_puuid)
# print(icon)
match_inf = match_info_overall(match_list, plyr_puuid)
print(match_inf)
