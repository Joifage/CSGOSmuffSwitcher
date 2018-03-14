import os
import configparser


def doesconfigexist():
    exist_accountconf = os.path.isfile('./conf.ini')
    if exist_accountconf is True:
        print("Ini Found: True")
    else:
        print("Ini Found: False.. Generating")
        config = configparser.ConfigParser()
        config['general'] = {'csgo_path': "N/A",
                             'steam_path': "N/A"}
        config['0'] = {'username': 'DUMMY',
                       'lastuse': 'DUMMY',
                       'rank': 'DUMMY',
                       'prime': 'DUMMY',
                       'active': 'DUMMY',
                       'autolaunch': 'DUMMY'}
        with open('conf.ini', 'w') as configfile1:
            config.write(configfile1)
            configfile1.close()
