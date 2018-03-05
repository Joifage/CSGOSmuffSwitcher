import configparser


def read():

        try:
            config1 = configparser.ConfigParser()
            config1.read('accounts.ini')
            username1 = config1['account1']['username']
            lastuse1 = config1['account1']['lastuse']
            rank1 = config1['account1']['rank']
            active1 = config1['account1']['active']
        except:
            print("")
        try:
            config2 = configparser.ConfigParser()
            config2.read('accounts.ini')
            username2 = config2['account2']['username']
            lastuse2 = config2['account2']['lastuse']
            rank2 = config2['account2']['rank']
            active2 = config2['account2']['active']
        except:
            print("")
        try:
            config3 = configparser.ConfigParser()
            config3.read('accounts.ini')
            username3 = config3['account3']['username']
            lastuse3 = config3['account3']['lastuse']
            rank3 = config3['account3']['rank']
            active3 = config3['account3']['active']
        except:
            print("")
        try:
            config4 = configparser.ConfigParser()
            config4.read('accounts.ini')
            username4 = config4['account4']['username']
            lastuse4 = config4['account4']['lastuse']
            rank4 = config4['account4']['rank']
            active4 = config4['account4']['active']
        except:
            print("")
        try:
            config5 = configparser.ConfigParser()
            config5.read('accounts.ini')
            username5 = config5['account5']['username']
            lastuse5 = config5['account5']['lastuse']
            rank5 = config5['account5']['rank']
            active5 = config5['account5']['active']
        except:
            print("")
        try:
            config6 = configparser.ConfigParser()
            config6.read('accounts.ini')
            username6 = config6['account6']['username']
            lastuse6 = config6['account6']['lastuse']
            rank6 = config6['account6']['rank']
            active6 = config6['account6']['active']
        except:
            print("")
        try:
            config7 = configparser.ConfigParser()
            config7.read('accounts.ini')
            username7 = config7['account7']['username']
            lastuse7 = config7['account7']['lastuse']
            rank7 = config7['account7']['rank']
            active7 = config7['account7']['active']
        except:
            print("")
        try:
            config8 = configparser.ConfigParser()
            config8.read('accounts.ini')
            username8 = config8['account8']['username']
            lastuse8 = config8['account8']['lastuse']
            rank8 = config8['account8']['rank']
            active8 = config8['account8']['active']
        except:
            print("")


read()