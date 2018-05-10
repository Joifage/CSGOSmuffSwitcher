import configparser
import accountread

config = configparser.ConfigParser()
a = accountread


def edit():
    edit_choice = "none"
    while edit_choice >= "0" or edit_choice <= "16":
        try:
            print("\n#  ", format("Username", '<25'), "Active")
            print("1. ", format(a.username1, '<25'), a.active1)
            print("2. ", format(a.username2, '<25'), a.active2)
            print("3. ", format(a.username3, '<25'), a.active3)
            print("4. ", format(a.username4, '<25'), a.active4)
            print("5. ", format(a.username5, '<25'), a.active5)
            print("6. ", format(a.username6, '<25'), a.active6)
            print("7. ", format(a.username7, '<25'), a.active7)
            print("8. ", format(a.username8, '<25'), a.active8)
            print("9. ", format(a.username9, '<25'), a.active9)
            print("10. ", format(a.username10, '<25'), a.active10)
            print("11. ", format(a.username11, '<25'), a.active11)
            print("12. ", format(a.username12, '<25'), a.active12)
            print("13. ", format(a.username13, '<25'), a.active13)
            print("14. ", format(a.username14, '<25'), a.active14)
            print("15. ", format(a.username15, '<25'), a.active15)
            print("16. ", format(a.username16, '<25'), a.active16)
        except:
            pass
        print("\n0. Back")
        print("\nSelect account number to edit or '0' to go back")
        edit_choice = input("Selection: ")
        while edit_choice >= '0' or edit_choice <= '16':
            if edit_choice == "0":
                return
            elif edit_choice >= '0' or edit_choice <= '16':
                try:
                    print("You have selected account", edit_choice)
                    try:
                        config.read('conf.ini')
                        username = config[edit_choice]['username']
                        rank = config[edit_choice]['rank']
                        prime = config[edit_choice]['prime']
                        active = config[edit_choice]['active']
                        auto_launch = config[edit_choice]['autolaunch']
                        steam_id = config[edit_choice]['steamid']
                    except:
                        pass
                    try:
                        print(format("\n1. Username: ", '<16'), username)
                        print(format("2. Rank: ", '<15'), rank)
                        print(format("3. Prime: ", '<15'), prime)
                        print(format("4. Active: ", '<15'), active)
                        print(format("5. Autolaunch: ", '<15'), auto_launch)
                        print(format("6. SteamID: ", '<15'), steam_id)
                        print(format("\n0. Back", '<15'))
                    except:
                        pass
                    edit_choice2 = input("\nSelect field to update: ")
                    global value
                    if edit_choice >= "0" and edit_choice <= "6":
                        new_value = input("Enter New Value: ")
                        if edit_choice2 == "1":
                            value = "username"
                        elif edit_choice2 == "2":
                            value = "rank"
                            new_value = new_value.upper()
                        elif edit_choice2 == "3":
                            value = "prime"
                            new_value = new_value.upper()
                        elif edit_choice2 == "4":
                            value = "active"
                            new_value = new_value.upper()
                        elif edit_choice2 == "5":
                            value = "autolaunch"
                            new_value = new_value.upper()
                        elif edit_choice2 == "6":
                            value = "steamid"
                            new_value = new_value.upper()
                        cfg_file = open("conf.ini", 'w')
                        config.set(edit_choice, value, new_value)
                        config.write(cfg_file)
                        cfg_file.close()
                        return
                    else:
                        print("Invalid selection")
                except Exception as e:
                    print(e)
            else:
                print("Incorrect Selection")
                input("Press Enter to continue")
    else:
        print("Incorrect Selection")
        input("Press Enter to continue")
