import configparser


def deleteaccount():
    try:
        delete = input("Select account to delete: ")
        delete = "account" + delete
        print("I'm trying to delete section", delete)
        parser = configparser.ConfigParser()
        parser.read('accounts.ini')
        parser.remove_section(delete)
        parser.write(open('accounts.ini', "w"))
        account_countnew = "none"
        parser.read('count_account.ini')
        account_countnew = int(parser['DEFAULT']['account_count'])
        account_countnew = account_countnew - 1
        account_countnew = str(account_countnew)
        open("count_account.ini", 'a')
        cfgfile2 = open("count_account.ini",
                        'w')
        parser.set('DEFAULT', 'account_count', account_countnew)
        parser.write(cfgfile2)
        cfgfile2.close()
    except:
        print("Something went wrong deleting section")
