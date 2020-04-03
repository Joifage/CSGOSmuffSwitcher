from winreg import *


def csgo():
    import os
    import configparser
    config = configparser.ConfigParser()
    config.read('conf.ini')
    csgo_path = config['general']['csgo_path']
    if csgo_path == "N/A":
        validation = False
        while not validation:
            try:
                reg_key = 'SOFTWARE\Classes\Applications\csgo.exe\shell\open\command'
                hreg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
                hkey = OpenKey(hreg, reg_key)
                dir_path_new = QueryValueEx(hkey, '')[0]
                CloseKey(hkey)
                dir_path_new = dir_path_new.strip(
                    '"%1 ')
                validation = os.path.isfile(dir_path_new)
                if validation is True:
                    cfgfile = open("conf.ini", 'w')
                    config.set('general', 'csgo_path', dir_path_new)
                    config.write(cfgfile)
                    cfgfile.close()
                    print("CSGO Path Set Successfully")
                    return
                else:
                    print("csgo.exe not found")
                    return
            except Exception as e:
                print('ERROR: Please try again -', e)
                validation = True
        choice = None
        while choice != "1" or choice != "2" or choice != "3":
            print("""   
                 Select a search method for CSGO Installation
    
                     1. Automatic (Scan Drive - Slow)
                     2. Manual    (Select Directory)
    
                     0. Exit
               """
                  )
            choice = input("Selection: ")
            choice = choice.upper()
            if choice == "1":
                drive = input("Select drive letter where csgo is located, example \'c\' or \'d\': ")
                print("Scanning for csgo.exe, please wait...")
                try:
                    found = False
                    for root, dirs, files in os.walk(drive + ':\\',
                                                     topdown=True):
                        for file in files:
                            if file == "csgo.exe":
                                print("File Found: ", os.path.join(root, file))
                                dir_path_new = os.path.join(
                                    root + '\\')
                                cfgfile = open("conf.ini",
                                               'w')
                                config.set('general', 'csgo_path', dir_path_new)
                                config.write(cfgfile)
                                cfgfile.close()
                                print("CSGO Path Set Successfully")
                                return
                    if not found:
                        print("No file matched the criteria on drive", drive + ":")
                except Exception as e:
                    print(e)
            elif choice == "2":
                validation = False
                while not validation:
                    dir_path_new = input("\nPlease enter the root directory csgo.exe: ")
                    dir_path_new = os.path.join(dir_path_new,
                                                '')
                    validation1 = os.path.isdir(
                        dir_path_new)
                    validation2 = os.path.isfile(dir_path_new + '\\' + "csgo.exe")
                    if validation1 is False:
                        print("Not a valid directory")
                    elif validation2 is False:
                        print("csgo.exe not found in selected directory")
                    elif validation1 is True and validation2 is True:
                        validation = True
                        if validation is True:
                            cfgfile = open("conf.ini", 'w')
                            config.set('general', 'csgo_path', dir_path_new)
                            config.write(cfgfile)
                            cfgfile.close()
                            print("CSGO Path Set Successfully")
                            return
                        else:
                            print("Not a valid directory please retry")
                    else:
                        print("Not a valid directory please retry")
            elif choice == "0":
                print("Quitting... Goodbye!")
                exit(1)
            else:
                print("Incorrect Selection, Try again")
    else:
        print("CSGO Path: Set")
