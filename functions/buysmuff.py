import webbrowser
from lxml import html
import requests


def getprice():
    print("Fetching Prices")

    page2 = requests.get('https://www.csgorankedaccounts.com/our-products/silvers')
    tree2 = html.fromstring(page2.content)
    price2 = tree2.xpath('/html/body/section[3]/div[3]/div/div[3]/div[1]/div[2]/div[3]/div/h2/text()')
    price2 = price2[0].lstrip()

    page3 = requests.get('https://myownrank.com/home/3-csgo-silver-1-ranked-account.html')
    tree3 = html.fromstring(page3.content)
    price3 = tree3.xpath('//*[@id="our_price_display"]/text()')
    price3 = price3[0].lstrip()

    page4 = requests.get('https://getasmurf.com/product/silver-1/')
    tree4 = html.fromstring(page4.content)
    price4 = tree4.xpath('//*[@id="product-321"]/div/div[1]/div/div[2]/div[2]/p/ins/span/text()')
    price4 = '$' + price4[0].lstrip()

    page5 = requests.get('https://csgosmurfs.com/product/silver-i/')
    tree5 = html.fromstring(page5.content)
    price5 = tree5.xpath('//*[@id="product-15685"]/div[2]/p[1]/span/text()')
    price5 = '$' + price5[0].lstrip()
    choice2 = "none"
    while choice2 >= "0" or choice2 <= "4":
        print("\t\t\tWebsite:")
        print("\n\t\t\t\t1. playerauctions.com           [Prices vary on account basis, check site]")
        print("\t\t\t\t2. csgorankedaccounts.com       [Silver 1 -", price2 + "]")
        print("\t\t\t\t3. myownrank.com                [Silver 1 -", price3 + "]")
        print("\t\t\t\t4. getasmurf.com                [Silver 1 -", price4 + "]")
        print("\t\t\t\t5. csgosmurfs.com               [Silver 1 -", price5 + "]")
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