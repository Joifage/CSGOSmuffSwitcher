import configparser
import os

config = configparser.ConfigParser()


def read_from_conf():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    account_list = []

    for i in range(1, 17):
        try:
            list_data = [config.items(str(i))]
            for entry in list_data:
                username = entry[0][1]
                password = entry[1][1]
                lastuse = entry[2][1]
                rank = entry[3][1]
                prime = entry[4][1]
                active = entry[5][1]
                autolaunch = entry[6][1]
                steamid = entry[7][1]
                account_list.append((username, password, lastuse, rank, prime, active, autolaunch, steamid))
                del username, password, lastuse, rank, prime, active, autolaunch, steamid
        except configparser.NoSectionError:
            pass
    return account_list


def delete_account(account_list, num_accounts):
    os.system('cls')
    print("DELETE ACCOUNT:-")
    print(format("\n\t\t#", '<5'), format(" Account", '<26'), format("Last Used", '<13'), format("Rank", '<7'),
          format("Prime", '<7'), "SteamID")
    for index, (username, password, lastuse, rank, prime, active, autolaunch, steamid) in enumerate(account_list):
        print(format("\t\t{}.".format(index + 1), '<5'), format(username, '<25'), format(lastuse, '<13'),
              format(rank, '<7'), format(prime, '<7'), steamid)
    delete = input("\nSelect the account id to delete: ")
    parser = configparser.ConfigParser()
    parser.read('conf.ini')
    parser.remove_section(delete)
    parser.write(open('conf.ini', "w"))
    delete = int(delete) + 1
    for i in range(delete, num_accounts + 1):
        with open('conf.ini') as config_file:
            parser.read_file(config_file)
            rename_section = i
            rename_section = str(rename_section)
            section_items = parser.items(rename_section)
            section_new_name = str(i - 1)
            config_file.close()
            cfg_file = open("conf.ini", 'w')
            parser.add_section(section_new_name)
            for option, value in section_items:
                parser.set(section_new_name, option, value)
                parser.remove_section(rename_section)
            parser.write(cfg_file)
            cfg_file.close()
    input('Account deleted, press enter to go back to main menu')
    return True


def edit_account(account_list):
    os.system('cls')
    input_valid = False
    while input_valid is not True:
        print("EDIT ACCOUNT:-")
        print(format("\n\t\t#", '<5'), format(" Account", '<26'), format("Last Used", '<13'), format("Rank", '<7'),
              format("Prime", '<7'), format("Active", '<7'), "SteamID")
        for index, (username, password, lastuse, rank, prime, active, autolaunch, steamid) in enumerate(account_list):
            print(format("\t\t{}.".format(index + 1), '<5'), format(username, '<25'), format(lastuse, '<13'),
                  format(rank, '<7'), format(prime, '<7'), format(active, '<7'), steamid)
        print("\n0. Back")
        edit_choice = int(input("\nSelect account number to edit or '0' to go back: "))
        if edit_choice == 0:
            return True
        elif 0 < int(edit_choice) <= len(account_list):
            input_valid = True
            print("You have selected account", edit_choice)
            edit_choice = str(edit_choice)
            config.read('conf.ini')
            username = config[edit_choice]['username']
            pwd = config[edit_choice]['password']
            rank = config[edit_choice]['rank']
            prime = config[edit_choice]['prime']
            active = config[edit_choice]['active']
            auto_launch = config[edit_choice]['autolaunch']
            steam_id = config[edit_choice]['steamid']
            choice2_valid = False
            while choice2_valid != True:
                print(format("\n1. Username: ", '<16'), username)
                print(format("2. Password: ", '<15'), pwd)
                print(format("3. Rank: ", '<15'), rank)
                print(format("4. Prime: ", '<15'), prime)
                print(format("5. Active: ", '<15'), active)
                print(format("6. Autolaunch: ", '<15'), auto_launch)
                print(format("7. SteamID: ", '<15'), steam_id)
                print(format("\n0. Back", '<15'))
                edit_choice2 = int(input("\nSelect field to update: "))
                value = ''
                if 0 <= edit_choice2 <= 7:
                    choice2_valid = True
                    new_value = input("Enter New Value: ")
                    if edit_choice2 == 1:
                        value = "username"
                    elif edit_choice2 == 2:
                        value = "password"
                        new_value = new_value.upper()
                    elif edit_choice2 == 3:
                        value = "rank"
                        new_value = new_value.upper()
                    elif edit_choice2 == 4:
                        value = "prime"
                        new_value = new_value.upper()
                    elif edit_choice2 == 5:
                        value = "active"
                        new_value = new_value.upper()
                    elif edit_choice2 == 6:
                        value = "autolaunch"
                        new_value = new_value.upper()
                    elif edit_choice2 == 7:
                        value = "steamid"
                        new_value = new_value.upper()
                    else:
                        input("Invalid selection, press entry to try again")
                        input("Press Enter to go back")
                    cfg_file = open("conf.ini", 'w')
                    config.set(edit_choice, value, new_value)
                    config.write(cfg_file)
                    cfg_file.close()
                    print("Account details updated")
                    return True
                else:
                    print("Invalid selection")
                    input("Press Enter to go back")
        else:
            print("Invalid selection")
            input("Press Enter to try again")


def new_account():
    os.system('cls')
    print("NEW ACCOUNT:-")
    file = open('conf.ini', 'r').read()
    account_count = file.count("active = Y")
    new_account_num = account_count + 1
    new_account_num = str(new_account_num)
    print('(*) indicates optional')
    new_username = input("\nEnter Steam Username: ")
    new_password = input("Enter Steam Password (*): ")
    new_last_use = "N/A"
    new_rank = input("Enter Rank (*): ").upper()
    new_prime = input("Prime? (Y/N) (*): ").upper()
    new_active = input("Set account to active? (Y/N): ").upper()
    new_auto = input("Should CSGO Autolaunch? (Y/N): ").upper()
    new_id = input("Enter Steam ID? (Y/N) (*): ").upper()
    config = configparser.ConfigParser()
    cfg_file = open("conf.ini", 'a')
    config.add_section(new_account_num)
    config.set(new_account_num, 'username', new_username)
    config.set(new_account_num, 'password', new_password)
    config.set(new_account_num, 'lastuse', new_last_use)
    config.set(new_account_num, 'rank', new_rank)
    config.set(new_account_num, 'prime', new_prime)
    config.set(new_account_num, 'active', new_active)
    config.set(new_account_num, 'autolaunch', new_auto)
    config.set(new_account_num, 'steamid', new_id)
    config.write(cfg_file)
    cfg_file.close()
    input("Account created, press enter to return to menu.")
    return True
