import configparser


def delete_account():
    try:
        delete = input("Select the account number to delete: ")
        parser = configparser.ConfigParser()
        parser.read('conf.ini')
        parser.remove_section(delete)
        parser.write(open('conf.ini', "w"))
        delete = int(delete) + 1
        for i in range(delete, 11):
            try:
                with open('conf.ini') as config_file:
                    parser.read_file(config_file)
                    rename_section = i
                    rename_section = str(rename_section)
                    section_items = parser.items(rename_section)
                    section_new_name = i - 1
                    section_new_name = str(section_new_name)
                    config_file.close()
                    cfg_file = open("conf.ini", 'w')
                    parser.add_section(section_new_name)
                    for option, value in section_items:
                        parser.set(section_new_name, option, value)
                        parser.remove_section(rename_section)
                    parser.write(cfg_file)
                    cfg_file.close()
            except:
                pass
    except Exception as e:
        print(e)
