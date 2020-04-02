import os
import configparser


def does_config_exist():
    exist_account_conf = os.path.isfile('./conf.ini')
    if exist_account_conf:
        print("conf.ini: found")
    else:
        print("conf.ini: not found.. Generating")
        config = configparser.ConfigParser()
        config['general'] = {'csgo_path': "N/A",
                             'steam_path': "N/A",
                             'steam_api_key': "N/A"}
        config['1'] = {'username': '',
                       'password': '',
                       'lastuse': '',
                       'rank': '',
                       'prime': '',
                       'active': '',
                       'autolaunch': '',
                       'steamid': ''}
        with open('conf.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
