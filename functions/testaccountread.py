import configparser

username1 = "Boobs1"
lastuse1 = "Boobs1"
rank1 = "Boobs1"
prime1 = "Boobs1"
active1 = "Boobs1"
autolaunch1 = "Boobs1"

username2 = "Boobs2"
lastuse2 = "Boobs2"
rank2 = "Boobs2"
prime2 = "Boobs2"
active2 = "Boobs2"
autolaunch2 = "Boobs2"

username3 = "Boobs3"
lastuse3 = "Boobs3"
rank3 = "Boobs3"
prime3 = "Boobs3"
active3 = "Boobs3"
autolaunch3 = "Boobs3"

max_accounts = 20

usernames = []

for i in range(max_accounts):
    try:
        config = configparser.ConfigParser()
        config.read('conf.ini')
        i = str(i)
        configread = 'config[' + i + '][username]'
        print(configread)
        username = configread
        usernames.append(username)
    except Exception as e:
        print(e)

print(usernames[0:20])
