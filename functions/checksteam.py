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
            for i in range(0, 4):
                os.system('cls')
                print("Steam Running:", steam_found, "Closing." + "." * i)
                time.sleep(1)
            subprocess.check_call('taskkill /f /im Steam.exe')
            return
        else:
            steam_found = False
            print("Steam Running:", steam_found)
            return
    except:
        pass
