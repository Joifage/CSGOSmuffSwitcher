import os
import configparser


def doesconfigexist():
    exist_accountconf = os.path.isfile('./accounts.ini')
    count_account = os.path.isfile('./count_account.ini')

    if exist_accountconf == True:
        print("accounts.ini file found")
    else:
        print("accounts.ini file not found.. Generating")
        config = configparser.ConfigParser()
        config['account'] = {'username': 'DUMMY',
                             'lastuse': 'DUMMY',
                             'rank': 'DUMMY',
                             'active': 'DUMMY'}
        with open('accounts.ini', 'w') as configfile1:
            config.write(configfile1)
            configfile1.close()

    if count_account == True:
        print("count_account.ini file found")
    else:
        print("count_account.ini file not found.. Generating")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'account_count': '0'}
        with open('count_account.ini', 'w') as configfile2:
            config.write(configfile2)
            configfile2.close()
