import os
import configparser
from winreg import *


def steam():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    steam_path = config['general']['steam_path']
    if steam_path == "N/A":
        choice = None
        while choice != "1" or choice != "2" or choice != "3":
            print("""
                Select a search method for Steam Installation

                    1. Automatic (Scan Drive - Slow)
                    2. Manual    (Select Directory)
                    3. Registry  (Fast)

                    0. Exit
              """
                  )
            choice = input("Selection: ")
            choice = choice.upper()
            if choice == "1":
                drive = input("Select drive letter where Steam is located, example \'c\' or \'d\': ")
                print("Scanning for Steam.exe, please wait...")
                try:
                    found = False
                    for root, dirs, files in os.walk(drive + ':\\',
                                                     topdown=True):
                        for file in files:
                            if file == "Steam.exe":
                                print("File Found: ", os.path.join(root, file))
                                dir_path_new = os.path.join(
                                    root + '\\' + file)
                                cfgfile = open("conf.ini",
                                               'w')
                                config.set('general', 'steam_path', dir_path_new)
                                config.write(cfgfile)
                                cfgfile.close()
                                print("Steam Path Set Successfully")
                                return
                    if not found:
                        print("No file matched the criteria on drive", drive + ":")
                except Exception as e:
                    print(e)
            elif choice == "2":
                validation = False
                while not validation:
                    dir_path_new = input("\nPlease enter the root directory Steam.exe: ")
                    dir_path_new = os.path.join(dir_path_new,
                                                '')
                    validation1 = os.path.isdir(
                        dir_path_new)
                    validation2 = os.path.isfile(dir_path_new + '\\' + "Steam.exe")
                    if validation1 is False:
                        print("Not a valid directory")
                    elif validation2 is False:
                        print("Steam.exe not found in selected directory")
                    elif validation1 is True and validation2 is True:
                        cfgfile = open("conf.ini", 'w')
                        config.set('general', 'steam_path', dir_path_new + "Steam.exe")
                        config.write(cfgfile)
                        cfgfile.close()
                        print("Steam Path Set Successfully")
                        return
                    else:
                        print("Not a valid directory please retry")
            elif choice == "3":
                validation = False
                while not validation:
                    try:
                        reg_key = 'Software\Valve\Steam'
                        hreg = ConnectRegistry(None, HKEY_CURRENT_USER)
                        hkey = OpenKey(hreg, reg_key)
                        dir_path_new = QueryValueEx(hkey, 'SteamExe')[0]
                        CloseKey(hkey)
                        dir_path_new = dir_path_new.strip(
                            '"%1 ')
                        dir_path_new = dir_path_new.replace("Steam.exe",
                                                            '')
                        validation = os.path.isfile(dir_path_new + '\\')
                        if validation is True:
                            cfgfile = open("conf.ini", 'w')
                            config.set('general', 'steam_path', dir_path_new)
                            config.write(cfgfile)
                            cfgfile.close()
                            print("Steam Path Set Successfully")
                            return
                        else:
                            print("Steam.exe not found")
                    except Exception as e:
                        print('ERROR: Please try again -', e)
                        validation = True
            elif choice == "0":
                print("Quitting... Goodbye!")
                exit(1)
            else:
                print("Incorrect Selection, Try again")
    else:
        print("Steam Path: Set")
