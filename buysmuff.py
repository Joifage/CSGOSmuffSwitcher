import webbrowser
from lxml import html
import requests
import requests.exceptions


def buy_smurf():
    choice2 = "none"
    while choice2 >= "0" or choice2 <= "4":
        print("\t\t\tWebsite:")
        print("\n\t\t\t\t1. playerauctions.com           [Prices vary on account basis, check site]")
        print("\t\t\t\t2. csgorankedaccounts.com")
        print("\t\t\t\t3. myownrank.com")
        print("\t\t\t\t4. getasmurf.com")
        print("\t\t\t\t5. csgosmurfs.com")
        print("\n\t\t\t\t\t0. Back")
        choice2 = input("Selection: ")
        try:
            if choice2 == "1":
                webbrowser.open('https://www.playerauctions.com/csgo-account/')
                return
            elif choice2 == "2":
                webbrowser.open('https://www.csgorankedaccounts.com/our-products/silvers')
                return
            elif choice2 == "3":
                webbrowser.open('https://myownrank.com/home/3-csgo-silver-1-ranked-account.html')
                return
            elif choice2 == "4":
                webbrowser.open('https://getasmurf.com/product/silver-1/')
                return
            elif choice2 == "5":
                webbrowser.open('https://csgosmurfs.com/product/silver-i/')
                return
            elif choice2 == "0":
                return
        except OSError:
            print(OSError)