item_list = []


def anschliessen(item):
    item_list.append(item)


class Item():

    def __init__(self, name, schaden, gewicht, wert, beschreibung, raum, altname1=None, altname2=None):
        self.name = name
        self.schaden = schaden
        self.gewicht = gewicht
        self.wert = wert
        self.beschreibung = beschreibung
        self.raum = raum
        self.eingesammelt = False

        self.altname1 = altname1
        self.altname2 = altname2

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def ausgabe(self):
        print("Name: " + str(self.name))
        print("Damage: " + str(self.schaden))
        print("Weight: " + str(self.gewicht))
        print("Rarity: " + str(self.wert))
        print("Description: " + str(self.beschreibung))


stick = Item("Stock", 1, 0.5, 0, "Nutzlos", 0)
anschliessen(stick)
