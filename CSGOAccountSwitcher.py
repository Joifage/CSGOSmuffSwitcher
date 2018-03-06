# Author:           Joif
# Purpose:          Allow fast switching between multiple steam accounts
# Version:          1.0
# Date updated:     15/02/2018

import datetime
import configparser
from configbuild import *
from winreg import *
import newaccount
import deleteaccount
import importlib
import accountread
from configparser import SafeConfigParser


def count():
    try:
        configcount = configparser.ConfigParser()
        configcount.read('count_account.ini')
        global account_count
        account_count = int(configcount['DEFAULT']['account_count'])
        if account_count >= 1:
            importlib.reload(accountread)
        else:
            print("No accounts set, please add a steam account")
            newaccount.accountsini()
    except:
        print()


def main():
    choice = 'none'
    while choice != "1" or choice != "2" or choice != "3" or choice != "add" or choice != "del":
        count()
        print("Accounts set:", account_count)
        print("\t\t\t", "\t Account", "\t Last Used", "\t\t Rank")
        importlib.reload(accountread)
        a = accountread
        try:
            if a.active1 != "":
                print("\t\t\t1.", "\t", a.username1, "\t", a.lastuse1, "\t", a.rank1)
        except:
            pass
        try:
            if a.active2 != "":
                print("\t\t\t2.", "\t", a.username2, "\t", a.lastuse2, "\t", a.rank2)
        except:
            pass
        try:
            if a.active3 != "":
                print("\t\t\t3.", "\t", a.username3, "\t", a.lastuse3, "\t", a.rank3)
        except:
            pass
        try:
            if a.active4 != "":
                print("\t\t\t4.", "\t", a.username4, "\t", a.lastuse4, "\t", a.rank4)
        except:
            pass
        try:
            if a.active5 != "":
                print("\t\t\t5.", "\t", a.username5, "\t", a.lastuse5, "\t", a.rank5)
        except:
            pass
        try:
            if a.active6 != "":
                print("\t\t\t6.", "\t", a.username6, "\t", a.lastuse6, "\t", a.rank6)
        except:
            pass
        try:
            if a.active7 != "":
                print("\t\t\t7.", "\t", a.username7, "\t", a.lastuse7, "\t", a.rank7)
        except:
            pass
        try:
            if a.active8 != "":
                print("\t\t\t8.", "\t", a.username8, "\t", a.lastuse8, "\t", a.rank8)
        except:
            pass

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
        elif choice == "del":
            deleteaccount.deleteaccount()
            importlib.reload(accountread)
        elif choice == "0":
            exit(1)
        else:
            print("Invalid Selection")


doesconfigexist()

count()

main()
