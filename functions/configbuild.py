import os
import configparser


def does_config_exist():
    exist_account_conf = os.path.isfile('./conf.ini')
    if exist_account_conf is True:
        print("Ini Found: True")
    else:
        print("Ini Found: False.. Generating")
        config = configparser.ConfigParser()
        config['general'] = {'csgo_path': "N/A",
                             'steam_path': "N/A"}
        with open('conf.ini', 'w') as configfile1:
            config.write(configfile1)
            configfile1.close()
