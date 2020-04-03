def is_running():
    import os
    import configparser
    import time
    import subprocess

    config = configparser.ConfigParser()
    config.read('conf.ini')
    steam_path = config['general']['steam_path']
    processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE).communicate()[0]
    if 'steam.exe'.encode() in processes.lower():
        retries = 0
        steam_found = True
        subprocess.check_call([steam_path, "-shutdown"])
        while steam_found is True:
            os.system('cls')
            print("Waiting for Steam to close" + "." * retries)
            processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                         stdout=subprocess.PIPE).communicate()[0]
            retries = 1
            time.sleep(1)
            if ('steam.exe' and 'steamservice.exe' and 'steamwebhelper.exe').encode() not in processes.lower():
                return True
    else:
        return False
