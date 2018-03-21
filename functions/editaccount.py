import configparser
import accountread


def edit():
    editchoice = "none"
    while editchoice >= "0" or editchoice <= "5":
        a = accountread
        try:
            format(a.username1, '<25')
            format(a.username2, '<25')
            format(a.username3, '<25')
            format(a.username4, '<25')
            format(a.username5, '<25')
            format(a.username6, '<25')
            format(a.username7, '<25')
            format(a.username8, '<25')
            format(a.username9, '<25')
            format(a.username10, '<25')
            format(a.username11, '<25')
            format(a.username12, '<25')
            format(a.username13, '<25')
            format(a.username14, '<25')
            format(a.username15, '<25')
            format(a.username16, '<25')
        except:
            pass
        print("Select account number to edit or '0' to go back")
        editchoice = input("Selection: ")
        print("\n0. Back")
        if editchoice == "0":
            return
        else:
            try:
                print("You have selected account", editchoice)
                config = configparser.ConfigParser()
                config.read('conf.ini')
                username = config[editchoice]['username']
                rank = config[editchoice]['rank']
                prime = config[editchoice]['prime']
                active = config[editchoice]['active']
                autolaunch = config[editchoice]['active']
                print(format("\n1. Username: ", '<16'), username)
                print(format("2. Rank: ", '<15'), rank)
                print(format("3. Prime: ", '<15'), prime)
                print(format("4. Active: ", '<15'), active)
                print(format("5. Autolaunch: ", '<15'), autolaunch)
                print(format("\n0. Back", '<15'))
                editchoice2 = input("\nSelect field to update: ")
                newvalue = input("Enter New Value: ")
                if editchoice2 == "1":
                    value = "username"
                elif editchoice2 == "2":
                    value = "rank"
                    newvalue = newvalue.upper()
                elif editchoice2 == "3":
                    value = "prime"
                    newvalue = newvalue.upper()
                elif editchoice2 == "4":
                    value = "active"
                    newvalue = newvalue.upper()
                elif editchoice2 == "5":
                    value = "autolaunch"
                    newvalue = newvalue.upper()
                cfgfile = open("conf.ini",
                                'w')
                config.set(editchoice, value, newvalue)
                config.write(cfgfile)
                cfgfile.close()
                return
            except Exception as e:
                print(e)
