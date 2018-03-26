import simpradar
import os
import sys
import buysmuff
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
            buysmuff.getprice()
            return
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
