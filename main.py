# Author:           Joif
# Purpose:          Allow fast switching between multiple steam accounts
# Version:          1.0
# Date updated:     14/03/2018

import sys
sys.path.insert(0, './functions')
import importlib
from winreg import *
import subprocess
import time
import datetime
import configparser
import webbrowser

import newaccount
import deleteaccount
import editaccount
import accountread
import setcsgo
import setsteam
from configbuild import *


def main():
    choice = 'none'
    while choice >= "0" or choice <= "10" or choice != "a" or choice != "d" or choice != "e":
        count()
        importlib.reload(accountread)
        a = accountread
        print("\nAccounts set:", account_count)
        print(format("\n\t\t#", '<7'), format(" Account", '<16'), format("Last Used", '<13'), format("Rank", '<7'), format("Prime", '<10'))
        try:
            if a.active1 == "Y":
                print(format("\t\t1.", '<7'), format(a.username1, '<15'), format(a.lastuse1, '<13'), format(a.rank1, '<7'), format(a.prime1, '<10'))
        except:
            pass
        try:
            if a.active2 == "Y":
                print(format("\t\t2.", '<7'), format(a.username2, '<15'), format(a.lastuse2, '<13'), format(a.rank2, '<7'), format(a.prime2, '<10'))
        except:
            pass
        try:
            if a.active3 == "Y":
                print(format("\t\t3.", '<7'), format(a.username3, '<15'), format(a.lastuse3, '<13'), format(a.rank3, '<7'), format(a.prime3, '<10'))
        except:
            pass
        try:
            if a.active4 == "Y":
                print(format("\t\t4.", '<7'), format(a.username4, '<15'), format(a.lastuse4, '<13'), format(a.rank4, '<7'), format(a.prime4, '<10'))
        except:
            pass
        try:
            if a.active5 == "Y":
                print(format("\t\t5.", '<7'), format(a.username5, '<15'), format(a.lastuse5, '<13'), format(a.rank5, '<7'), format(a.prime5, '<10'))
        except:
            pass
        try:
            if a.active6 == "Y":
                print(format("\t\t6.", '<7'), format(a.username6, '<15'), format(a.lastuse6, '<13'), format(a.rank6, '<7'), format(a.prime6, '<10'))
        except:
            pass
        try:
            if a.active7 == "Y":
                print(format("\t\t7.", '<7'), format(a.username7, '<15'), format(a.lastuse7, '<13'), format(a.rank7, '<7'), format(a.prime7, '<10'))
        except:
            pass
        try:
            if a.active8 == "Y":
                print(format("\t\t8.", '<7'), format(a.username8, '<15'), format(a.lastuse8, '<13'), format(a.rank8, '<7'), format(a.prime8, '<10'))
        except:
            pass

        print("""                   
                 a = Add New Account
                 e = Edit Account
                 d = Delete Account
            
                     0. Exit
            """)
        choice = input("Selection: ").lower()
        global usrid
        global userreg
        global autolaunch
        global lastused
        lastused = str(datetime.date.today())
        usrid = choice
        if choice == "1":
            userreg = a.username1
            autolaunch = a.autolaunch1
            end()
        elif choice == "2":
            userreg = a.username2
            autolaunch = a.autolaunch2
            end()
        elif choice == "3":
            userreg = a.username3
            autolaunch = a.autolaunch3
            end()
        elif choice == "4":
            userreg = a.username4
            autolaunch = a.autolaunch4
            end()
        elif choice == "5":
            userreg = a.username5
            autolaunch = a.autolaunch5
            end()
        elif choice == "6":
            userreg = a.username6
            autolaunch = a.autolaunch6
            end()
        elif choice == "7":
            userreg = a.username7
            autolaunch = a.autolaunch7
            end()
        elif choice == "8":
            userreg = a.username8
            autolaunch = a.autolaunch8
            end()
        elif choice == "9":
            print("I don't know how to do 9 smuffs sorry")
        elif choice == "a":
            newaccount.accountsini()
        elif choice == "e":
            editaccount.edit()
        elif choice == "d":
            deleteaccount.deleteaccount()
            importlib.reload(accountread)
        elif choice == "0":
            print("Exiting... Bye")
            exit(1)
        else:
            print("Invalid Selection")

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


def checksteam():
    try:
        global steam_path
        config = configparser.ConfigParser()
        config.read('conf.ini')
        steam_path = config['general']['steam_path']
        processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
        if 'Steam.exe'.encode() in processes:
            steamfound = True
            print("Steam Running:", steamfound, "...Closing")
            subprocess.call([steam_path, "-shutdown"])
            time.sleep(2)
        else:
            steamfound = False
            print("Steam Running:", steamfound)
    except:
        pass


def end():
    print("Setting account to:", userreg)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Valve\Steam", 0, KEY_WRITE)
    try:
        SetValueEx(aKey, "AutoLoginUser", 0, REG_SZ, userreg)
        SetValueEx(aKey, "RememberPassword", 0, REG_DWORD, 1)
        config = configparser.ConfigParser()
        config.read('conf.ini')
        config.set(usrid, "lastuse", lastused)
        with open("conf.ini", 'w') as cfgfile:
            config.write(cfgfile)
        cfgfile.close()
        if autolaunch == "Y":
            print("Launching CSGO")
            webbrowser.open('steam://rungameid/730')
        else:
            print("Launching Steam")
            webbrowser.open('steam://open/main')
    except Exception as e:
        print(e)
    CloseKey(aKey)
    CloseKey(aReg)
    exit(1)


checksteam()

doesconfigexist()

count()

main()
