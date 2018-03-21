import urllib.request
import zipfile
import re
import configparser
import os


def dlextract():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    csgo_path = config['general']['csgo_path']
    csgo_path = csgo_path.replace('csgo.exe', '')
    if csgo_path != "N/A":
        try:
            print("\nChecking file exists on web server")
            url = 'http://simpleradar.com/downloads/fullpack.zip'
            extract_path = 'csgo\\resource\\overviews'
            weburl = urllib.request.urlopen(url)
            zipstatus = str(weburl.getcode())
            match = re.match('(^2)',
                             zipstatus) is not None
            if match is True:
                print("Status", zipstatus, "- File found on remote server")
            else:
                print("Status", zipstatus, "- An error may have occurred locating the remote file")
            print("\nRetrieving SimpleRadar from web server")
            urllib.request.urlretrieve(url, "simpleradar.zip")
        except Exception as e:
            print(e)
            return None

        try:
            print("Extracting contents to:")
            print(csgo_path + extract_path)
            with zipfile.ZipFile("simpleradar.zip", "r") as zip_ref:
                zip_ref.extractall(csgo_path + extract_path)
                zip_ref.close()
                os.remove('simpleradar.zip')
                print("\nDone!")
        except Exception as e:
            print(e)
    else:
        print("csgo path not set, will not extract")
