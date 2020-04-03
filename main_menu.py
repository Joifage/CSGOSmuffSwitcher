# Author:           Joif
# Purpose:          Allow fast switching between multiple steam accounts
# Version:          1.2
# Date updated:     02/04/2020

import sys
sys.path.insert(0, './functions')
import pyperclip
import winsound

import configbuild as c
import account as a
import extra
import checksteam
import funcs as f

try:
    winsound.PlaySound('./sound/music.wav', winsound.SND_ASYNC + winsound.SND_LOOP)
except:
    print("How dare you delete the choon")


def main():
    account_count = f.count_active_accounts()
    choice = 'none'
    while "0" >= choice >= str(account_count) or choice not in ("a", "d", "e", "x", "m"):
        c.does_config_exist()
        account_list = a.read_from_conf()
        print("""   _____                       __    _____         _ _       _               
  / ____|                     / _|  / ____|       (_) |     | |              
 | (___  _ __ ___  _   _ _ __| |_  | (_____      ___| |_ ___| |__   ___ _ __ 
  \___ \| '_ ` _ \| | | | '__|  _|  \___ \ \ /\ / / | __/ __| '_ \ / _ \ '__|
  ____) | | | | | | |_| | |  | |    ____) \ V  V /| | || (__| | | |  __/ |   
 |_____/|_| |_| |_|\__,_|_|  |_|   |_____/ \_/\_/ |_|\__\___|_| |_|\___|_|   
                                                                             """)
        print("Accounts set:", account_count)
        print(format("\n\t\t#", '<5'), format(" Account", '<26'), format("Last Used", '<13'), format("Rank", '<7'),
              format("Prime", '<7'), "SteamID")
        for index, (username, password, lastuse, rank, prime, active, autolaunch, steamid) in enumerate(account_list):
            if active == 'Y':
                if steamid == '':
                    steamid = 'NOT SET'
                print(format("\t\t{}.".format(index + 1), '<5'), format(username, '<25'), format(lastuse, '<13'), format(rank, '<7'), format(prime, '<7'), steamid)
        print("""                   
                 a = Add New Account
                 e = Edit Account
                 d = Delete Account

                 x = Extra
                 m = Mute Music
                 
                     0. Exit
            """)
        choice = input("Selection: ").lower()
        winsound.PlaySound('./sound/usp1.wav', winsound.SND_ASYNC)
        try:
            int_choice = int(choice)
            if 0 <= int(int_choice) <= account_count:
                if int_choice == 0:
                    print("Exiting... Bye")
                    exit(0)
                else:
                    for index, (username, password, lastuse, rank, prime, active, autolaunch, steamid) in enumerate(account_list):
                        if int_choice - 1 == index and active == 'Y':
                            userreg = username
                            pyperclip.copy(password)
                            autolaunch_flag = autolaunch
                            usrid = str(int_choice)
                            f.launch(userreg, autolaunch_flag, usrid)
                        elif int_choice == index and active == 'N':
                            input("Inactive account selected, please set account to active and try again\nPress Enter "
                                  "to continue")
            else:
                input("Invalid Selection, Press Enter to continue")
        except ValueError:
            if choice == "a":
                outcome = a.new_account()
                if outcome is True:
                    main()
            elif choice == "e":
                outcome = a.edit_account(account_list)
                if outcome is True:
                    main()
            elif choice == "d":
                outcome = a.delete_account(account_list, len(account_list))
                if outcome is True:
                    main()
            elif choice == "x":
                extra.main(account_list)
            elif choice == "m":
                winsound.PlaySound(None, winsound.SND_PURGE)
                main()
            else:
                print("Invalid Selection")
                input("Press Enter to continue")


if __name__ == '__main__':
    steam_found = checksteam.is_running()
    main()
