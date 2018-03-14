import configparser


def accountsini():
    try:
        file = open('conf.ini', 'r').read()
        global account_count
        account_count = file.count("active = Y")
        new_account_num = account_count + 1
        new_account_num = str(new_account_num)
        newusername = input("\nEnter Steam Username: ")
        newlastuse = "N/A"
        newrank = input("Enter Rank: ").upper()
        newprime = input("Prime? (Y/N): ").upper()
        newactive = input("Set account to active? (Y/N): ").upper()
        newauto = input("Should CSGO Autolaunch? (Y/N): ").upper()
        config = configparser.ConfigParser()
        cfgfile1 = open("conf.ini",
                        'a')
        config.add_section(new_account_num)
        config.set(new_account_num, 'username', newusername)
        config.set(new_account_num, 'lastuse', newlastuse)
        config.set(new_account_num, 'rank', newrank)
        config.set(new_account_num, 'prime', newprime)
        config.set(new_account_num, 'active', newactive)
        config.set(new_account_num, 'autolaunch', newauto)
        config.write(cfgfile1)
        cfgfile1.close()
    except Exception as e:
        print(e)
