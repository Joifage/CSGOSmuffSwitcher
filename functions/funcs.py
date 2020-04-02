import importlib
import sys
sys.path.insert(0, './functions')
import account as a
import setcsgo
import setsteam
from winreg import *
import datetime
import configparser
import webbrowser


def count_active_accounts():
    file = open('conf.ini', 'r').read()
    account_count = file.count("active = Y")
    if account_count >= 1:
        importlib.reload(a)
    else:
        setcsgo.csgo()
        setsteam.steam()
        print("\nNo accounts set, please add a steam account")
        a.accountsini()
    return int(account_count)


def end(userreg, autolaunch_flag, usrid):
    import time
    import subprocess
    import os

    lastused = str(datetime.date.today())

    print(" Setting account to:", userreg)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Software\Valve\Steam", 0, KEY_WRITE)
    SetValueEx(aKey, "AutoLoginUser", 0, REG_SZ, userreg)
    SetValueEx(aKey, "RememberPassword", 0, REG_DWORD, 1)
    CloseKey(aKey)
    CloseKey(aReg)
    config = configparser.ConfigParser()
    config.read('conf.ini')
    config.set(usrid, "lastuse", lastused)
    with open("conf.ini", 'w') as cfgfile:
        config.write(cfgfile)
    cfgfile.close()
    steam_found = False
    retries = 0
    check_pass = 0
    if autolaunch_flag == "Y":
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
            if 'steam.exe'.encode() in processes.lower():
                check_pass += 1
            if retries > 10:
                print("Unable start steam, exiting...")
                time.sleep(5)
                exit()
            if check_pass >= 3:
                steam_found = True
                exit()
    exit(0)
