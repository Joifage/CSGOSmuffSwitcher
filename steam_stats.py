import urllib.request
from urllib.error import HTTPError
#from urllib.request import urlopen, HTTPError
from xml.etree.ElementTree import parse
import os
import configparser


def get_stats(account_list):
    config = configparser.ConfigParser()
    config.read('conf.ini')
    api_key = config['general']['steam_api_key']
    os.system('cls')
    print("Retrieve CSGO Stats")
    print(format("\n\t\t#", '<5'), format(" Account", '<26'), format("Last Used", '<13'), format("Rank", '<7'),
          format("Prime", '<7'), "SteamID")
    for index, (username, password, lastuse, rank, prime, active, autolaunch, steamid) in enumerate(account_list):
        if str(steamid) != '':
            print(format("\t\t{}.".format(index + 1), '<5'), format(username, '<25'), format(lastuse, '<13'),
                  format(rank, '<7'), format(prime, '<7'), steamid)
    int_choice = int(input("\n Selection: "))
    for index, (username, password, lastuse, rank, prime, active, autolaunch, steamid) in enumerate(account_list):
        if int_choice - 1 == index and active == 'Y':
            usr_id = steamid
            usr_name = username
    url = 'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={}&steamid={}&format=xml'.format(api_key, usr_id)
    try:
        u = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        if 'Internal Server Error' in str(e):
            input('Cannot access player data, may be set to private.. Enter to go back')
            return
    doc = parse(u)
    stats = []
    for item in doc.find('stats'):
        name = item.findtext('name')
        value = item.findtext('value')
        entry = (name, value)
        stats.append(entry)
    u.close()
    os.system('cls')
    kdr = int(stats[0][1]) / int(stats[1][1])
    time_played = int(stats[2][1]) / 60 / 60
    whiff = int(stats[46][1]) / int(stats[47][1]) * 100
    winrate = int(stats[127][1]) / int(stats[128][1]) * 100
    print("Stats for:", usr_name)
    print("\n Total Kills:", stats[0][1])
    print(" Total Deaths:", stats[1][1])
    print(" KDR:", str(round(kdr, 2)))
    print(" Time Played:", str(round(time_played, 2)), "hrs")
    print(" Shots Fired:", stats[47][1])
    print(" Shots Hit:", stats[46][1])
    print(" Whiff Percentage:", str(round(whiff, 2)) + "%")
    print(" Total MVP's:", stats[102][1])
    print(" Win Rate: ", str(round(winrate, 2)) + "%")
    input("\n Press Enter to continue")
    return
