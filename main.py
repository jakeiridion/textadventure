import items
import map

current_room = 0
player_inventory = []

while True:
    if __name__ == '__main__':
        string = input("> ").strip().split()


        # Inventory Commands Methoden:
        def i_show():
            print(player_inventory)


        def i_add():
            if len(string) == 1:
                print("What should I take ?")
                answer = input("> ").strip()
                for item in items.item_list:
                    if item.eingesammelt == True:
                        print("Bereits eingesamelt !")
                        break

                    if item.raum == current_room and (
                            answer == item.name or answer == item.altname1 or answer == item.altname2) and item.eingesammelt == False:
                        player_inventory.append(item)
                        item.eingesammelt = True
                        print(item.name + " Wurde eingesammelt !")

            else:
                for item in items.item_list:
                    if item.eingesammelt == True:
                        print("Bereits eingesamelt !")
                        break

                    if item.raum == current_room and (
                            string[1] == item.name or string[1] == item.altname1 or string[
                        1] == item.altname2) and item.eingesammelt == False:
                        player_inventory.append(item)
                        item.eingesammelt = True
                        print(item.name + " Wurde eingesammelt !")


        # fix drop

        def i_drop():
            if len(string) == 1:
                print("What should I drop ?")
                answer = input("> ").strip()
                for item in player_inventory:
                    if answer == item.name and item.eingesammelt == True:
                        player_inventory.remove(item)
                        item.eingesammelt = False
                        print(item.name + " Wurde hingelegt")





        # Inventory Commands Abfragen:
        if string[0] == "take":
            i_add()

        if string[0] == "drop":
            i_drop()

        if string[0] == "i":
            i_show()
