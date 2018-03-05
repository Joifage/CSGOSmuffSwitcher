import configparser
import datetime


def accountsini():

    config = configparser.ConfigParser()
    config.read('count_account.ini')
    account_count = int(config['DEFAULT']['account_count'])
    print("Amount of accounts set:", account_count)
    new_account_count = account_count + 1
    new_account_count = str(new_account_count)
    new_account_num = str(new_account_count)
    new_account_num = "account" + new_account_num
    newusername = input("Enter Steam Username:")
    newlastuse = str(datetime.date.today())
    newrank = input("Enter rank:")
    newactive = input("Set account to active? (Y/N):").upper()
    config1 = configparser.ConfigParser()
    cfgfile1 = open("accounts.ini",
                    'a')
    config1.add_section(new_account_num)
    config1.set(new_account_num, 'username', newusername)
    config1.set(new_account_num, 'lastuse', newlastuse)
    config1.set(new_account_num, 'rank', newrank)
    config1.set(new_account_num, 'active', newactive)
    config1.write(cfgfile1)
    cfgfile1.close()

    config2 = configparser.ConfigParser()
    cfgfile2 = open("count_account.ini",
                    'w')
    config2.set('DEFAULT', 'account_count', new_account_count)
    config2.write(cfgfile2)
    cfgfile2.close()
