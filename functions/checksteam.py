def isrunning():
    import os
    import configparser
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
            steamfound = True
            print("Steam Running:", steamfound, "...Closing")
            subprocess.check_call([steam_path, "-shutdown"])
            return
        else:
            steamfound = False
            print("Steam Running:", steamfound)
            return
    except:
        pass
