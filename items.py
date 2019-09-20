class Item():

    def __init__(self, name, schaden, gewicht, wert, beschreibung, raum):
        self.name = name
        self.schaden = schaden
        self.gewicht = gewicht
        self.wert = wert
        self.beschreibung = beschreibung
        self.raum = raum

    def ausgabe(self):
        print("Name: " + str(self.name))
        print("Damage: " + str(self.schaden))
        print("Weight: " + str(self.gewicht))
        print("Rarity: " + str(self.wert))
        print("Description: " + str(self.beschreibung))


stick = Item("Stick", 1, 0.5, "useless", "A stick found in your garden", 0)

