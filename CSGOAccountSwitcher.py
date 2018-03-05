# Author:           Joif
# Purpose:          Allow fast switching between multiple steam accounts
# Version:          1.0
# Date updated:     15/02/2018

import datetime
import configparser
from winreg import *
import newaccount
import deleteaccount
from accountread import *

from configparser import SafeConfigParser

def count():    
    print("\nChecking for conf files...")
    configcount = configparser.ConfigParser()
    configcount.read('count_account.ini')
    global account_count
    account_count = int(configcount['DEFAULT']['account_count'])
    if account_count >= 1:
        print("Loading Account Details")
        read()
    else:
        print("No accounts set, please add a steam account")
        newaccount.accountsini()


def main():
    choice = 'none'
    while choice != "1" or choice != "2" or choice != "3" or choice != "add" or choice != "del":
        count()
        read()
        print("Accounts set:", account_count)
        print("\t\t\t", "\t Account", "\t Last Used", "\t\t Rank")
        if active1 != "":
            print("\t\t\t1.", "\t", username1, "\t", lastuse1, "\t", rank1)
        if read().active2 != "":
            print("\t\t\t2.", "\t", read().username2, "\t", read().lastuse2, "\t", read().rank2)
        if read().active3 != "":
            print("\t\t\t3.", "\t", read().username3, "\t", read().lastuse3, "\t", read().rank3)
        if read().active4 != "":
            print("\t\t\t4.", "\t", read().username4, "\t", read().lastuse4, "\t", read().rank4)
        if read().active5 != "":
            print("\t\t\t5.", "\t", read().username5, "\t", read().lastuse5, "\t", read().rank5)
        if read().active6 != "":
            print("\t\t\t6.", "\t", read().username6, "\t", read().lastuse6, "\t", read().rank6)
        if read().active7 != "":
            print("\t\t\t7.", "\t", read().username7, "\t", read().lastuse7, "\t", read().rank7)
        if read().active8 != "":
            print("\t\t\t8.", "\t", read().username8, "\t", read().lastuse8, "\t", read().rank8)
        print("""                    
                 add = Add New Account
                 del = Delete Account
                
                     0. Exit
        """)
        choice = input("Selection: ").lower()
        if choice == "1":
            print("You have selected account one")
            print("Do action blablabla")
        elif choice == "add":
            newaccount.accountsini()
            read()
        elif choice == "del":
            deleteaccount.deleteaccount()
        elif choice == "0":
            exit(1)


count()

main()

exit(1)
