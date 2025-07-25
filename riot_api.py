import requests, json, math
from datetime import datetime, timezone

api_key = "RGAPI-0340816b-f6d0-4788-a807-f005932afb3a"

VERSION_URL = "https://ddragon.leagueoflegends.com/api/versions.json"
DD_URL = "https://ddragon.leagueoflegends.com/cdn"

def account_info_by_name(username, tagline):
  account_request_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tagline}?api_key={api_key}"
  account_info_by_name = requests.get(account_request_url).json()
  player_puuid = account_info_by_name['puuid']
  return player_puuid

def matches_list(player_puuid): # Returns matchid of last 20 matches in list
  match_puuid_request_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?start=0&count=20&api_key={api_key}"
  matches_list = requests.get(match_puuid_request_url).json()
  return matches_list

def get_static_summoners():
  latest_patch = requests.get(VERSION_URL)
  summoner_json = requests.get(f"{DD_URL}/{latest_patch}/data/en_US/summoner.json")
  summoners_dict = {int(summoner["key"]): summoner["name"] for summoner in summoner_json["data"].values()}
  summoners_icon = {summoner["key"]: summoner["image"]["sprite"] for summoner in summoner_json["data"].values()}
  return summoners_dict, summoners_icon


def get_static_items():
  latest_patch = requests.get(VERSION_URL)
  item_json = requests.get(f"{DD_URL}/{latest_patch}/data/en_US/item.json")
  item_dict = {int(item_id): item_info["name"] for item_id, item_info in item_json["data"].items()}
  item_icon = {int(item_id): item_info["image"]["sprite"] for item_id, item_info in item_json["data"].items()}
  return item_dict, item_icon

def get_static_runes():
  latest_patch = requests.get(VERSION_URL)
  rune_json = requests.get(f"{DD_URL}/{latest_patch}/data/en_US/runesReforged.json")
  rune_dict = {int(rune_info["id"]): rune_info["name"] for rune_info in rune_json}
  rune_icon = {int(rune_info["id"]): rune_info["icon"] for rune_info in rune_json}
  return rune_dict, rune_icon


def match_info_overall(match_id, player_puuid): # Returns relevant match data that is shared between all players such as game time, date game was played, etc.
  match_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
  match_info_overall_json = requests.get(match_url).json()
  summoners_dict, summoners_icon = get_static_summoners()
  rune_dict, rune_icon = get_static_runes()
  item_dict, item_icon = get_static_items()

  player_index = match_info_overall_json['metadata']['participants'].index(player_puuid)

  game_type = match_info_overall_json['info']['queueId']

  player_specific_info = match_info_overall_json['info']['participants'][player_index]
  
  did_win = player_specific_info['win']
  
  game_ms = match_info_overall_json['info']['gameCreation']
  game_dur_sec = match_info_overall_json['info']['gameDuration']
  min_game, game_sec = divmod(game_dur_sec, 60)
  game_hour, min_game = divmod(min_game, 60)
  if game_hour > 0:
    game_duration = f"{game_hour}h {min_game}m {game_sec}s"
  else:
    game_duration = f"{min_game}m {game_sec}s"
  
  game_date = datetime.fromtimestamp(game_ms / 1000, tz=timezone.utc).strftime('%m/%d/%Y')
  
  player_champion = player_specific_info['championName']

  summoner1id = player_specific_info['summoner1Id']
  summoner2id = player_specific_info['summoner2Id']

  summoner1 = summoners_dict[summoner1id]
  summoner2 = summoners_dict[summoner2id]
  summoner1_icon = summoners_icon[summoner1]
  summoner2_icon = summoners_icon[summoner2]
  
  major_rune_id = player_specific_info['perks'][0]['style']
  minor_rune_id = player_specific_info['perks'][1]['style']

  major_rune = rune_dict[major_rune_id]
  minor_rune = rune_dict[minor_rune_id]
  major_rune_icon = rune_icon[major_rune_id]
  mainor_rune_icon = rune_icon[minor_rune_id]

  players_kills = player_specific_info['kills']
  players_deaths = player_specific_info['deaths']
  players_assists = player_specific_info['assists']

  item_ids = [player_specific_info[f'item{number}'] for number in range(7)]

  item0 =
  item1 =
  item2 =
  item3 =
  item4 =
  item5 =
  item6 =


