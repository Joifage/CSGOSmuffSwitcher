import configparser

username1 = None
lastuse1 = None
rank1 = None
prime1 = None
active1 = None
autolaunch1 = None
steamid1 = None

username2 = None
lastuse2 = None
rank2 = None
prime2 = None
active2 = None
autolaunch2 = None
steamid2 = None

username3 = None
lastuse3 = None
rank3 = None
prime3 = None
active3 = None
autolaunch3 = None
steamid3 = None

username4 = None
lastuse4 = None
rank4 = None
prime4 = None
active4 = None
autolaunch4 = None
steamid4 = None

username5 = None
lastuse5 = None
rank5 = None
prime5 = None
active5 = None
autolaunch5 = None
steamid5 = None

username6 = None
lastuse6 = None
rank6 = None
prime6 = None
active6 = None
autolaunch6 = None
steamid6 = None

username7 = None
lastuse7 = None
rank7 = None
prime7 = None
active7 = None
autolaunch7 = None
steamid7 = None

username8 = None
lastuse8 = None
rank8 = None
prime8 = None
active8 = None
autolaunch8 = None
steamid8 = None

username9 = None
lastuse9 = None
rank9 = None
prime9 = None
active9 = None
autolaunch9 = None
steamid9 = None

username10 = None
lastuse10 = None
rank10 = None
prime10 = None
active10 = None
autolaunch10 = None
steamid10 = None

username11 = None
lastuse11 = None
rank11 = None
prime11 = None
active11 = None
autolaunch11 = None
steamid11 = None

username12 = None
lastuse12 = None
rank12 = None
prime12 = None
active12 = None
autolaunch12 = None
steamid12 = None

username13 = None
lastuse13 = None
rank13 = None
prime13 = None
active13 = None
autolaunch13 = None
steamid13 = None

username14 = None
lastuse14 = None
rank14 = None
prime14 = None
active14 = None
autolaunch14 = None
steamid14 = None

username15 = None
lastuse15 = None
rank15 = None
prime15 = None
active15 = None
autolaunch15 = None
steamid15 = None

username16 = None
lastuse16 = None
rank16 = None
prime16 = None
active16 = None
autolaunch16 = None
steamid16 = None

config = configparser.ConfigParser()

try:
    config.read('conf.ini')
    username1 = config['1']['username']
    lastuse1 = config['1']['lastuse']
    rank1 = config['1']['rank']
    prime1 = config['1']['prime']
    active1 = config['1']['active']
    autolaunch1 = config['1']['autolaunch']
    steamid1 = config['1']['steamid']
except: pass
try:
    username2 = config['2']['username']
    lastuse2 = config['2']['lastuse']
    rank2 = config['2']['rank']
    prime2 = config['2']['prime']
    active2 = config['2']['active']
    autolaunch2 = config['2']['autolaunch']
    steamid2 = config['2']['steamid']
except: pass
try:
    username3 = config['3']['username']
    lastuse3 = config['3']['lastuse']
    rank3 = config['3']['rank']
    prime3 = config['3']['prime']
    active3 = config['3']['active']
    autolaunch3 = config['3']['autolaunch']
    steamid3 = config['3']['steamid']
except: pass
try:
    username4 = config['4']['username']
    lastuse4 = config['4']['lastuse']
    rank4 = config['4']['rank']
    prime4 = config['4']['prime']
    active4 = config['4']['active']
    autolaunch4 = config['4']['autolaunch']
    steamid4 = config['4']['steamid']
except: pass
try:
    username5 = config['5']['username']
    lastuse5 = config['5']['lastuse']
    rank5 = config['5']['rank']
    prime5 = config['5']['prime']
    active5 = config['5']['active']
    autolaunch5 = config['5']['autolaunch']
    steamid5 = config['5']['steamid']
except: pass
try:
    username6 = config['6']['username']
    lastuse6 = config['6']['lastuse']
    rank6 = config['6']['rank']
    prime6 = config['6']['prime']
    active6 = config['6']['active']
    autolaunch6 = config['6']['autolaunch']
    steamid6 = config['6']['steamid']
except: pass
try:
    username7 = config['7']['username']
    lastuse7 = config['7']['lastuse']
    rank7 = config['7']['rank']
    prime7 = config['7']['prime']
    active7 = config['7']['active']
    autolaunch7 = config['7']['autolaunch']
    steamid7 = config['7']['steamid']
except: pass
try:
    username8 = config['8']['username']
    lastuse8 = config['8']['lastuse']
    rank8 = config['8']['rank']
    prime8 = config['8']['prime']
    active8 = config['8']['active']
    autolaunch8 = config['8']['autolaunch']
    steamid8 = config['8']['steamid']
except: pass
try:
    username9 = config['9']['username']
    lastuse9 = config['9']['lastuse']
    rank9 = config['9']['rank']
    prime9 = config['9']['prime']
    active9 = config['9']['active']
    autolaunch9 = config['9']['autolaunch']
    steamid9 = config['9']['steamid']
except: pass
try:
    username10 = config['10']['username']
    lastuse10 = config['10']['lastuse']
    rank10 = config['10']['rank']
    prime10 = config['10']['prime']
    active10 = config['10']['active']
    autolaunch10 = config['10']['autolaunch']
    steamid10 = config['10']['steamid']
except: pass
try:
    username11 = config['11']['username']
    lastuse11 = config['11']['lastuse']
    rank11 = config['11']['rank']
    prime11 = config['11']['prime']
    active11 = config['11']['active']
    autolaunch11 = config['11']['autolaunch']
    steamid11 = config['11']['steamid']
except: pass
try:
    username12 = config['12']['username']
    lastuse12 = config['12']['lastuse']
    rank12 = config['12']['rank']
    prime12 = config['12']['prime']
    active12 = config['12']['active']
    autolaunch12 = config['12']['autolaunch']
    steamid12 = config['12']['steamid']
except: pass
try:
    username13 = config['13']['username']
    lastuse13 = config['13']['lastuse']
    rank13 = config['13']['rank']
    prime13 = config['13']['prime']
    active13 = config['13']['active']
    autolaunch13 = config['13']['autolaunch']
    steamid13 = config['13']['steamid']
except: pass
try:
    username14 = config['14']['username']
    lastuse14 = config['14']['lastuse']
    rank14 = config['14']['rank']
    prime14 = config['14']['prime']
    active14 = config['14']['active']
    autolaunch14 = config['14']['autolaunch']
    steamid14 = config['14']['steamid']
except: pass
try:
    username15 = config['15']['username']
    lastuse15 = config['15']['lastuse']
    rank15 = config['15']['rank']
    prime15 = config['15']['prime']
    active15 = config['15']['active']
    autolaunch15 = config['15']['autolaunch']
    steamid15 = config['15']['steamid']
except: pass
try:
    username16 = config['16']['username']
    lastuse16 = config['16']['lastuse']
    rank16 = config['16']['rank']
    prime16 = config['16']['prime']
    active16 = config['16']['active']
    autolaunch16 = config['16']['autolaunch']
    steamid16 = config['16']['steamid']
except: pass
