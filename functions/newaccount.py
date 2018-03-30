import configparser


def accounts_ini():
    try:
        file = open('conf.ini', 'r').read()
        global account_count
        account_count = file.count("active = Y")
        new_account_num = account_count + 1
        new_account_num = str(new_account_num)
        new_username = input("\nEnter Steam Username: ")
        new_last_use = "N/A"
        new_rank = input("Enter Rank: ").upper()
        new_prime = input("Prime? (Y/N): ").upper()
        new_active = input("Set account to active? (Y/N): ").upper()
        new_auto = input("Should CSGO Autolaunch? (Y/N): ").upper()
        new_id = input("Enter Steam ID? (Y/N) (optional for stat retrieval): ").upper()
        config = configparser.ConfigParser()
        cfg_file = open("conf.ini", 'a')
        config.add_section(new_account_num)
        config.set(new_account_num, 'username', new_username)
        config.set(new_account_num, 'lastuse', new_last_use)
        config.set(new_account_num, 'rank', new_rank)
        config.set(new_account_num, 'prime', new_prime)
        config.set(new_account_num, 'active', new_active)
        config.set(new_account_num, 'autolaunch', new_auto)
        config.set(new_account_num, 'steamid', new_id)
        config.write(cfg_file)
        cfg_file.close()
    except Exception as e:
        print(e)
