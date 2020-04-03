import urllib.request
import zipfile
import re
import configparser
import os
import shutil


def dlextract():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    csgo_path = str(config['general']['csgo_path']).replace('csgo.exe', '')
    if csgo_path != "N/A" and os.path.isdir(csgo_path) is True:
        print("\nChecking file exists on web server")
        url = 'http://www.simpleradar.com/downloads/CleanPat1Buy0Spec2.zip'
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
        temp_extract_path = 'temp_extract'
        final_extract_path = os.path.join(csgo_path, 'csgo\\resource\\overviews')
        try:
            os.mkdir(temp_extract_path)
        except FileExistsError:
            pass
        with zipfile.ZipFile('simpleradar.zip', "r") as zip_ref:
            zip_ref.extractall(temp_extract_path)
            zip_ref.close()
            os.remove('simpleradar.zip')
        for root, dir, files in os.walk(temp_extract_path):
            for filename in files:
                source_file = os.path.join(root, filename)
                if filename.endswith('.dds'):
                    dest_file = os.path.join(final_extract_path, filename)
                    if os.path.isfile(dest_file):
                        try:
                            os.rename(dest_file, dest_file.replace('.dds', '_original.dds'))
                        except FileExistsError:
                            pass
                    print('Installing file: {} to {}.'.format(source_file, dest_file))
                    shutil.move(source_file, dest_file)
                else:
                    os.remove(source_file)
        for root, dir, files in os.walk(temp_extract_path):
            for folder in dir:
                os.removedirs(os.path.join(root, folder))
    else:
        print("csgo path not set, will not extract")
    return True
