# Author:           Joif
# Purpose:          Allow fast switching between multiple steam accounts
# Version:          1.1
# Date updated:     21/03/2018

import sys
sys.path.insert(0, './functions')
import importlib
from winreg import *
import datetime
import configparser
import winsound
import webbrowser

from configbuild import does_config_exist
import newaccount
import deleteaccount
import editaccount
import accountread
import setcsgo
import setsteam
import extra
import checksteam

try:
    winsound.PlaySound('./sound/music.wav', winsound.SND_ASYNC + winsound.SND_LOOP)
except:
    print("How dare you delete the choon")


def main():
    choice = 'none'
    count()
    while choice <= "0" and choice >= str(account_count) or choice not in ("a", "d", "e", "x", "m"):
        does_config_exist()
        importlib.reload(accountread)
        a = accountread
        countdown2 = (datetime.datetime(2018, 9, 20, 10, 00, 00) - datetime.datetime.now())
        print("\n Major Start:", str(countdown2).split(".", 1)[0])
        print("""   _____                       __    _____         _ _       _               
  / ____|                     / _|  / ____|       (_) |     | |              
 | (___  _ __ ___  _   _ _ __| |_  | (_____      ___| |_ ___| |__   ___ _ __ 
  \___ \| '_ ` _ \| | | | '__|  _|  \___ \ \ /\ / / | __/ __| '_ \ / _ \ '__|
  ____) | | | | | | |_| | |  | |    ____) \ V  V /| | || (__| | | |  __/ |   
 |_____/|_| |_| |_|\__,_|_|  |_|   |_____/ \_/\_/ |_|\__\___|_| |_|\___|_|   
                                                                             """)
        print(" Accounts set:", account_count)
        print(format("\n\t\t#", '<5'), format(" Account", '<26'), format("Last Used", '<13'), format("Rank", '<7'),
              format("Prime", '<10'))
        try:
            if a.active1 == "Y":
                print(format("\t\t1.", '<5'), format(a.username1, '<25'), format(a.lastuse1, '<13'),
                      format(a.rank1, '<7'), format(a.prime1, '<10'))
            if a.active2 == "Y":
                print(format("\t\t2.", '<5'), format(a.username2, '<25'), format(a.lastuse2, '<13'),
                      format(a.rank2, '<7'), format(a.prime2, '<10'))
            if a.active3 == "Y":
                print(format("\t\t3.", '<5'), format(a.username3, '<25'), format(a.lastuse3, '<13'),
                      format(a.rank3, '<7'), format(a.prime3, '<10'))
            if a.active4 == "Y":
                print(format("\t\t4.", '<5'), format(a.username4, '<25'), format(a.lastuse4, '<13'),
                      format(a.rank4, '<7'), format(a.prime4, '<10'))
            if a.active5 == "Y":
                print(format("\t\t5.", '<5'), format(a.username5, '<25'), format(a.lastuse5, '<13'),
                      format(a.rank5, '<7'), format(a.prime5, '<10'))
            if a.active6 == "Y":
                print(format("\t\t6.", '<5'), format(a.username6, '<25'), format(a.lastuse6, '<13'),
                      format(a.rank6, '<7'), format(a.prime6, '<10'))
            if a.active7 == "Y":
                print(format("\t\t7.", '<5'), format(a.username7, '<25'), format(a.lastuse7, '<13'),
                      format(a.rank7, '<7'), format(a.prime7, '<10'))
            if a.active8 == "Y":
                print(format("\t\t8.", '<5'), format(a.username8, '<25'), format(a.lastuse8, '<13'),
                      format(a.rank8, '<7'), format(a.prime8, '<10'))
            if a.active9 == "Y":
                print(format("\t\t9.", '<5'), format(a.username9, '<25'), format(a.lastuse9, '<13'),
                      format(a.rank9, '<7'), format(a.prime9, '<10'))
            if a.active10 == "Y":
                print(format("\t\t10.", '<5'), format(a.username10, '<25'), format(a.lastuse10, '<13'),
                      format(a.rank10, '<7'), format(a.prime10, '<10'))
            if a.active11 == "Y":
                print(format("\t\t11.", '<5'), format(a.username11, '<25'), format(a.lastuse11, '<13'),
                      format(a.rank11, '<7'), format(a.prime11, '<10'))
            if a.active12 == "Y":
                print(format("\t\t12.", '<5'), format(a.username12, '<25'), format(a.lastuse12, '<13'),
                      format(a.rank12, '<7'), format(a.prime12, '<10'))
            if a.active13 == "Y":
                print(format("\t\t13.", '<5'), format(a.username13, '<25'), format(a.lastuse13, '<13'),
                      format(a.rank13, '<7'), format(a.prime13, '<10'))
            if a.active14 == "Y":
                print(format("\t\t14.", '<5'), format(a.username14, '<25'), format(a.lastuse14, '<13'),
                      format(a.rank14, '<7'), format(a.prime14, '<10'))
            if a.active15 == "Y":
                print(format("\t\t15.", '<5'), format(a.username15, '<25'), format(a.lastuse15, '<13'),
                      format(a.rank15, '<7'), format(a.prime15, '<10'))
            if a.active16 == "Y":
                print(format("\t\t16.", '<5'), format(a.username16, '<25'), format(a.lastuse16, '<13'),
                      format(a.rank16, '<7'), format(a.prime16, '<10'))
        except:
            pass

        print("""                   
                 a = Add New Account
                 e = Edit Account
                 d = Delete Account

                 x = Extra
                 m = Mute Music
                 
                     0. Exit
            """)
        choice = input(" Selection: ").lower()
        winsound.PlaySound('./sound/usp1.wav', winsound.SND_ASYNC)
        global usrid
        global userreg
        global autolaunch
        global lastused
        lastused = str(datetime.date.today())
        usrid = choice
        if choice == "1" and a.active1 == "Y":
            userreg = a.username1
            autolaunch = a.autolaunch1
            end()
        elif choice == "2" and a.active2 == "Y":
            userreg = a.username2
            autolaunch = a.autolaunch2
            end()
        elif choice == "3" and a.active3 == "Y":
            userreg = a.username3
            autolaunch = a.autolaunch3
            end()
        elif choice == "4" and a.active4 == "Y":
            userreg = a.username4
            autolaunch = a.autolaunch4
            end()
        elif choice == "5" and a.active5 == "Y":
            userreg = a.username5
            autolaunch = a.autolaunch5
            end()
        elif choice == "6" and a.active6 == "Y":
            userreg = a.username6
            autolaunch = a.autolaunch6
            end()
        elif choice == "7" and a.active7 == "Y":
            userreg = a.username7
            autolaunch = a.autolaunch7
            end()
        elif choice == "8" and a.active8 == "Y":
            userreg = a.username8
            autolaunch = a.autolaunch8
            end()
        elif choice == "9" and a.active9 == "Y":
            userreg = a.username9
            autolaunch = a.autolaunch9
            end()
        elif choice == "10" and a.active10 == "Y":
            userreg = a.username10
            autolaunch = a.autolaunch10
            end()
        elif choice == "11" and a.active11 == "Y":
            userreg = a.username11
            autolaunch = a.autolaunch11
            end()
        elif choice == "12" and a.active12 == "Y":
            userreg = a.username12
            autolaunch = a.autolaunch12
            end()
        elif choice == "13" and a.active13 == "Y":
            userreg = a.username13
            autolaunch = a.autolaunch13
            end()
        elif choice == "14" and a.active14 == "Y":
            userreg = a.username14
            autolaunch = a.autolaunch14
            end()
        elif choice == "15" and a.active15 == "Y":
            userreg = a.username15
            autolaunch = a.autolaunch15
            end()
        elif choice == "16" and a.active16 == "Y":
            userreg = a.username16
            autolaunch = a.autolaunch16
            end()
        elif choice == "a":
            newaccount.accountsini()
        elif choice == "e":
            editaccount.edit()
        elif choice == "d":
            deleteaccount.deleteaccount()
            importlib.reload(accountread)
        elif choice == "x":
            extra.main()
        elif choice == "m":
            winsound.PlaySound(None, winsound.SND_PURGE)
        elif choice == "0":
            print("Exiting... Bye")
            exit(0)
        else:
            print(" Invalid Selection")
            input(" Press Enter to continue")


def count():
    try:
        file = open('conf.ini', 'r').read()
        global account_count
        account_count = file.count("active = Y")
        if account_count >= 1:
            importlib.reload(accountread)
        else:
            setcsgo.csgo()
            setsteam.steam()
            print("\nNo accounts set, please add a steam account")
            newaccount.accountsini()
    except:
        pass


def end():
    import time
    import subprocess
    import os
    print(" Setting account to:", userreg)
    try:
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"Software\Valve\Steam", 0, KEY_WRITE)
        SetValueEx(aKey, "AutoLoginUser", 0, REG_SZ, userreg)
        SetValueEx(aKey, "RememberPassword", 0, REG_DWORD, 1)
        config = configparser.ConfigParser()
        config.read('conf.ini')
        config.set(usrid, "lastuse", lastused)
        with open("conf.ini", 'w') as cfgfile:
            config.write(cfgfile)
        cfgfile.close()
        steam_found = False
        retries = 0
        check_pass = 0
        if autolaunch == "Y":
            while steam_found is False:
                os.system('cls')
                print("Launching CSGO and exiting" + "." * retries)
                if retries in (0, 5, 10):
                    webbrowser.open('steam://rungameid/730')
                time.sleep(2)
                retries += 1
                processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                             stdout=subprocess.PIPE).communicate()[0]
                if 'csgo.exe'.encode() in processes:
                    exit()
        else:
            while steam_found is False:
                os.system('cls')
                print("Launching Steam and exiting" + "." * retries)
                if retries in (0, 5, 10):
                    webbrowser.open('steam://open/main')
                processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                             stdout=subprocess.PIPE).communicate()[0]
                time.sleep(5)
                retries += 1
                if 'Steam.exe'.encode() in processes:
                    check_pass += 1
                if retries > 10:
                    print("Unable start steam, exiting...")
                    time.sleep(5)
                    exit()
                if check_pass >= 3:
                    steam_found = True
                    exit()
    except FileNotFoundError:
        print("Steam registry key not found, ensure steam is installed correctly")
        exit()
    except Exception as e:
        print(e)
    CloseKey(aKey)
    CloseKey(aReg)
    exit(0)


if __name__ == '__main__':
    checksteam.isrunning()
    main()
