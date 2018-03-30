from urllib.request import urlopen
from xml.etree.ElementTree import parse
import os
import accountread

a = accountread

REQUEST = 'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='
API_KEY = '82D92741D6E273AF3BF653BE62124FF1'


def get_stats():
    os.system('cls')
    print("Retrieve CSGO Stats")
    try:
        print("\n #  ", format("Username", '<25'))
        print(" 1. ", format(a.username1, '<25'))
        print(" 2. ", format(a.username2, '<25'))
        print(" 3. ", format(a.username3, '<25'))
        print(" 4. ", format(a.username4, '<25'))
        print(" 5. ", format(a.username5, '<25'))
        print(" 6. ", format(a.username6, '<25'))
        print(" 7. ", format(a.username7, '<25'))
        print(" 8. ", format(a.username8, '<25'))
        print(" 9. ", format(a.username9, '<25'))
        print(" 10. ", format(a.username10, '<25'))
        print(" 11. ", format(a.username11, '<25'))
        print(" 12. ", format(a.username12, '<25'))
        print(" 13. ", format(a.username13, '<25'))
        print(" 14. ", format(a.username14, '<25'))
        print(" 15. ", format(a.username15, '<25'))
        print(" 16. ", format(a.username16, '<25'))
    except:
        pass
    choice = input("\n Selection: ")
    global usr_id
    global usr_name
    if choice == "1" and a.steamid1 != "":
        usr_id = a.steamid1
        usr_name = a.username1
    elif choice == "2" and a.steamid2 != "":
        usr_id = a.steamid2
        usr_name = a.username2
    elif choice == "3" and a.steamid3 != "":
        usr_id = a.steamid3
        usr_name = a.username3
    elif choice == "4" and a.steamid4 != "":
        usr_id = a.steamid4
        usr_name = a.username4
    elif choice == "5" and a.steamid5 != "":
        usr_id = a.steamid5
        usr_name = a.username5
    elif choice == "6" and a.steamid6 != "":
        usr_id = a.steamid6
        usr_name = a.username6
    elif choice == "7" and a.steamid7 != "":
        usr_id = a.steamid7
        usr_name = a.username7
    elif choice == "8" and a.steamid8 != "":
        usr_id = a.steamid8
        usr_name = a.username8
    elif choice == "9" and a.steamid9 != "":
        usr_id = a.steamid9
        usr_name = a.username9
    elif choice == "10" and a.steamid10 != "":
        usr_id = a.steamid10
        usr_name = a.username10
    elif choice == "11" and a.steamid11 != "":
        usr_id = a.steamid11
        usr_name = a.username11
    elif choice == "12" and a.steamid12 != "":
        usr_id = a.steamid12
        usr_name = a.username12
    elif choice == "13" and a.steamid13 != "":
        usr_id = a.steamid13
        usr_name = a.username13
    elif choice == "14" and a.steamid14 != "":
        usr_id = a.steamid14
        usr_name = a.username14
    elif choice == "15" and a.steamid15 != "":
        usr_id = a.steamid15
        usr_name = a.username15
    elif choice == "16" and a.steamid16 != "":
        usr_id = a.steamid16
        usr_name = a.username16
    else:
        print("Invalid Selection or no steam profile ID has been set.")
    try:
        url = REQUEST + API_KEY + '&steamid=' + usr_id + '&format=xml'
        u = urlopen(url)
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
    except Exception as e:
        print(e)
