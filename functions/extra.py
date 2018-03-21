import simpradar
import os
import sys
sys.path.insert(0, '..')


def main():
    os.system('cls')
    choice = 'none'
    while choice >= '0' or choice <= '2':
        print("""
            Extra Functions:
            
                1. Install Simple Radar
                2. Buy a smuff
                
                9. Delete Config File (Reset)
                
                    0. Back
                """)
        choice = input("Select extra function: ")
        if choice == "0":
            return
        elif choice == "1":
            simpradar.dlextract()
            return
        elif choice == "2":
            import webbrowser
            choice2 = "none"
            while choice2 >= "0" or choice2 <= "4":
                print("""
                Website:
                
                    1. playerauctions.com           [Silver 1 - typically: $15.99]
                    2. csgorankedaccounts.com       [Silver 1 - typically: $19.99]
                    3. myownrank.com                [Silver 1 - typically: $23.99]
                    4. getasmurf.com                [Silver 1 - typically: $25.99]
                    5. csgosmurf.com                [Silver 1 - typically: $27.99]
                    
                        0. Back""")
                choice2 = input("Selection: ")
                try:
                    if choice2 == "1":
                        webbrowser.open('https://www.playerauctions.com/csgo-account/')
                        return
                    elif choice2 == "2":
                        webbrowser.open('https://www.csgorankedaccounts.com/')
                        return
                    elif choice2 == "3":
                        webbrowser.open('https://myownrank.com/')
                        return
                    elif choice2 == "4":
                        webbrowser.open('https://getasmurf.com')
                        return
                    elif choice2 == "5":
                        webbrowser.open('https://csgosmurfs.com/')
                        return
                except OSError:
                    print(OSError)

        elif choice == "9":
            try:
                os.remove('conf.ini')
                conf = os.path.isfile('./conf.ini')
                if conf is False:
                    print("Successfully deleted conf")
                    return
                else:
                    print("There was a problem deleting file")
            except OSError:
                pass
        else:
            print("Incorrect selection.. try again")
