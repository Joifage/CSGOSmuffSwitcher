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

username9 = None
lastuse9 = None
rank9 = None
prime9 = None
active9 = None
autolaunch9 = None

username10 = None
lastuse10 = None
rank10 = None
prime10 = None
active10 = None
autolaunch10 = None

username11 = None
lastuse11 = None
rank11 = None
prime11 = None
active11 = None
autolaunch11 = None

username12 = None
lastuse12 = None
rank12 = None
prime12 = None
active12 = None
autolaunch12 = None

username13 = None
lastuse13 = None
rank13 = None
prime13 = None
active13 = None
autolaunch13 = None

username14 = None
lastuse14 = None
rank14 = None
prime14 = None
active14 = None
autolaunch14 = None

username15 = None
lastuse15 = None
rank15 = None
prime15 = None
active15 = None
autolaunch15 = None

username16 = None
lastuse16 = None
rank16 = None
prime16 = None
active16 = None
autolaunch16 = None

config = configparser.ConfigParser()

try:
    config.read('conf.ini')
    username1 = config['1']['username']
    lastuse1 = config['1']['lastuse']
    rank1 = config['1']['rank']
    prime1 = config['1']['prime']
    active1 = config['1']['active']
    autolaunch1 = config['1']['autolaunch']

    username2 = config['2']['username']
    lastuse2 = config['2']['lastuse']
    rank2 = config['2']['rank']
    prime2 = config['2']['prime']
    active2 = config['2']['active']
    autolaunch2 = config['2']['autolaunch']

    username3 = config['3']['username']
    lastuse3 = config['3']['lastuse']
    rank3 = config['3']['rank']
    prime3 = config['3']['prime']
    active3 = config['3']['active']
    autolaunch3 = config['3']['autolaunch']

    username4 = config['4']['username']
    lastuse4 = config['4']['lastuse']
    rank4 = config['4']['rank']
    prime4 = config['4']['prime']
    active4 = config['4']['active']
    autolaunch4 = config['4']['autolaunch']

    username5 = config['5']['username']
    lastuse5 = config['5']['lastuse']
    rank5 = config['5']['rank']
    prime5 = config['5']['prime']
    active5 = config['5']['active']
    autolaunch5 = config['5']['autolaunch']

    username6 = config['6']['username']
    lastuse6 = config['6']['lastuse']
    rank6 = config['6']['rank']
    prime6 = config['6']['prime']
    active6 = config['6']['active']
    autolaunch6 = config['6']['autolaunch']

    username7 = config['7']['username']
    lastuse7 = config['7']['lastuse']
    rank7 = config['7']['rank']
    prime7 = config['7']['prime']
    active7 = config['7']['active']

    autolaunch7 = config['7']['autolaunch']
    username8 = config['8']['username']
    lastuse8 = config['8']['lastuse']
    rank8 = config['8']['rank']
    prime8 = config['8']['prime']
    active8 = config['8']['active']
    autolaunch8 = config['8']['autolaunch']

    username1 = config['9']['username']
    lastuse1 = config['9']['lastuse']
    rank1 = config['9']['rank']
    prime1 = config['9']['prime']
    active1 = config['9']['active']
    autolaunch1 = config['9']['autolaunch']

    username2 = config['10']['username']
    lastuse2 = config['10']['lastuse']
    rank2 = config['10']['rank']
    prime2 = config['10']['prime']
    active2 = config['10']['active']
    autolaunch2 = config['10']['autolaunch']

    username3 = config['11']['username']
    lastuse3 = config['11']['lastuse']
    rank3 = config['11']['rank']
    prime3 = config['11']['prime']
    active3 = config['11']['active']
    autolaunch3 = config['11']['autolaunch']

    username4 = config['12']['username']
    lastuse4 = config['12']['lastuse']
    rank4 = config['12']['rank']
    prime4 = config['12']['prime']
    active4 = config['12']['active']
    autolaunch4 = config['12']['autolaunch']

    username5 = config['13']['username']
    lastuse5 = config['13']['lastuse']
    rank5 = config['13']['rank']
    prime5 = config['13']['prime']
    active5 = config['13']['active']
    autolaunch5 = config['13']['autolaunch']

    username6 = config['14']['username']
    lastuse6 = config['14']['lastuse']
    rank6 = config['14']['rank']
    prime6 = config['14']['prime']
    active6 = config['14']['active']
    autolaunch6 = config['14']['autolaunch']

    username7 = config['15']['username']
    lastuse7 = config['15']['lastuse']
    rank7 = config['15']['rank']
    prime7 = config['15']['prime']
    active7 = config['15']['active']
    autolaunch7 = config['15']['autolaunch']

    username8 = config['16']['username']
    lastuse8 = config['16']['lastuse']
    rank8 = config['16']['rank']
    prime8 = config['16']['prime']
    active8 = config['16']['active']
    autolaunch8 = config['16']['autolaunch']
except:
    pass
