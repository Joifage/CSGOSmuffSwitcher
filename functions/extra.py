import simpradar
import os
import sys
import buysmuff
import steam_stats
import main_menu
sys.path.insert(0, '..')


def main(account_list):
    os.system('cls')
    choice = 'none'
    while choice >= '0' or choice <= '2':
        print("""
            Extra Functions:
            
                1. Install Simple Radar
                2. Buy a smuff
                3. CSGO Stats
                
                9. Delete Config File (Reset)
                
                    0. Back
                """)
        choice = input("Select extra function: ")
        if choice == "0":
            main_menu.main()
        elif choice == "1":
            simpradar.dlextract()
            main_menu.main()
        elif choice == "2":
            buysmuff.buy_smurf()
            main_menu.main()
        elif choice == "3":
            steam_stats.get_stats(account_list)
            main_menu.main()
        elif choice == "9":
            try:
                os.remove('conf.ini')
                conf = os.path.isfile('./conf.ini')
                if conf:
                    print("There was a problem deleting file")
                else:
                    print("Successfully deleted conf")
            except OSError:
                pass
        else:
            print("Incorrect selection.. try again")
