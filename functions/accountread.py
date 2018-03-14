import configparser

username1 = None
lastuse1 = None
rank1 = None
prime1 = None
active1 = None
autolaunch1 = None

username2 = None
lastuse2 = None
rank2 = None
prime2 = None
active2 = None
autolaunch2 = None

username3 = None
lastuse3 = None
rank3 = None
prime3 = None
active3 = None
autolaunch3 = None

username4 = None
lastuse4 = None
rank4 = None
prime4 = None
active4 = None
autolaunch4 = None

username5 = None
lastuse5 = None
rank5 = None
prime5 = None
active5 = None
autolaunch5 = None

username6 = None
lastuse6 = None
rank6 = None
prime6 = None
active6 = None
autolaunch6 = None

username7 = None
lastuse7 = None
rank7 = None
prime7 = None
active7 = None
autolaunch7 = None

username8 = None
lastuse8 = None
rank8 = None
prime8 = None
active8 = None
autolaunch8 = None

try:
    config1 = configparser.ConfigParser()
    config1.read('conf.ini')
    username1 = config1['1']['username']
    lastuse1 = config1['1']['lastuse']
    rank1 = config1['1']['rank']
    prime1 = config1['1']['prime']
    active1 = config1['1']['active']
    autolaunch1 = config1['1']['autolaunch']
except:
    pass
try:
    config2 = configparser.ConfigParser()
    config2.read('conf.ini')
    username2 = config2['2']['username']
    lastuse2 = config2['2']['lastuse']
    rank2 = config2['2']['rank']
    prime2 = config1['2']['prime']
    active2 = config2['2']['active']
    autolaunch2 = config1['2']['autolaunch']
except:
    pass
try:
    config3 = configparser.ConfigParser()
    config3.read('conf.ini')
    username3 = config3['3']['username']
    lastuse3 = config3['3']['lastuse']
    rank3 = config3['3']['rank']
    prime3 = config1['3']['prime']
    active3 = config3['3']['active']
    autolaunch3 = config1['3']['autolaunch']
except:
    pass
try:
    config4 = configparser.ConfigParser()
    config4.read('conf.ini')
    username4 = config4['4']['username']
    lastuse4 = config4['4']['lastuse']
    rank4 = config4['4']['rank']
    prime4 = config1['4']['prime']
    active4 = config4['4']['active']
    autolaunch4 = config1['4']['autolaunch']
except:
    pass
try:
    config5 = configparser.ConfigParser()
    config5.read('conf.ini')
    username5 = config5['5']['username']
    lastuse5 = config5['5']['lastuse']
    rank5 = config5['5']['rank']
    prime5 = config1['5']['prime']
    active5 = config5['5']['active']
    autolaunch5 = config1['5']['autolaunch']
except:
    pass
try:
    config6 = configparser.ConfigParser()
    config6.read('conf.ini')
    username6 = config6['6']['username']
    lastuse6 = config6['6']['lastuse']
    rank6 = config6['6']['rank']
    prime6 = config1['6']['prime']
    active6 = config6['6']['active']
    autolaunch6 = config1['6']['autolaunch']
except:
    pass
try:
    config7 = configparser.ConfigParser()
    config7.read('conf.ini')
    username7 = config7['7']['username']
    lastuse7 = config7['7']['lastuse']
    rank7 = config7['7']['rank']
    prime7 = config1['7']['prime']
    active7 = config7['7']['active']
    autolaunch7 = config1['7']['autolaunch']
except:
    pass
try:
    config8 = configparser.ConfigParser()
    config8.read('conf.ini')
    username8 = config8['8']['username']
    lastuse8 = config8['8']['lastuse']
    rank8 = config8['8']['rank']
    prime8 = config1['8']['prime']
    active8 = config8['8']['active']
    autolaunch8 = config1['8']['autolaunch']
except:
    pass
