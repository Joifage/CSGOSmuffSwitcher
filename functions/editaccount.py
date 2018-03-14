import configparser


def edit():
    editchoice = None
    while editchoice != "1" or editchoice != "2" or editchoice != "3" or editchoice != "4" or editchoice != "5":
        editchoice = input("Select account number to edit: ")
        print("You have selected account", editchoice)
        try:
            config = configparser.ConfigParser()
            config.read('conf.ini')
            username = config[editchoice]['username']
            rank = config[editchoice]['rank']
            prime = config[editchoice]['prime']
            active = config[editchoice]['active']
            autolaunch = config[editchoice]['active']
            print("1. Username: ", username)
            print("2. Rank: ", rank)
            print("3. Prime: ", prime)
            print("4. Active: ", active)
            print("5. Autolaunch: ", autolaunch)
            editchoice2 = input("\nSelect field to update: ")
            newvalue = input("Enter New Value: ")
            if editchoice2 == "1":
                value = "username"
            elif editchoice2 == "2":
                value = "rank"
            elif editchoice2 == "3":
                value = "prime"
            elif editchoice2 == "4":
                value = "active"
            elif editchoice2 == "5":
                value = "autolaunch"
            cfgfile = open("conf.ini",
                            'w')
            config.set(editchoice, value, newvalue)
            config.write(cfgfile)
            cfgfile.close()
            return
        except Exception as e:
            print(e)
