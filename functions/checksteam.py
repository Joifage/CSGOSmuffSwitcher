def isrunning():
    import os
    import configparser
    import time
    os.system('cls')
    try:
        import subprocess
        global steam_path
        config = configparser.ConfigParser()
        config.read('conf.ini')
        steam_path = config['general']['steam_path']
        processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                     stdout=subprocess.PIPE).communicate()[0]
        if 'Steam.exe'.encode() in processes:
            steam_found = True
            subprocess.check_call([steam_path, "-shutdown"])
            while steam_found is True:
                print("Waiting for Steam to close" + "." * retries)
                processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                             stdout=subprocess.PIPE).communicate()[0]
                retries = 1
                time.sleep(1)
                if ('Steam.exe' and 'SteamService.exe' and 'steamwebhelper.exe').encore() not in processes:
                    return
        else:
            steam_found = False
            print("Steam Running:", steam_found)
            return
    except:
        pass
