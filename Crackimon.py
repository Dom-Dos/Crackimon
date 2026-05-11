#Crackimon_labor
import random
import time

# KLASSEN

class spieler:
    def __init__(self, name, sex, abhängigkeit, inventar, c_tot, c_lebend,geld,cracki_aktiv):
        self.name = name
        self.sex = sex
        self.abhängigkeit = abhängigkeit
        self.inventar = inventar
        self.c_tot = c_tot
        self.c_lebend = c_lebend
        self.geld = geld
        self.cracki_aktiv = cracki_aktiv



class crackimon:
    def __init__(self, status, lvl, name, werte, fähigkeiten):
        self.name = name
        self.status = status
        self.lvl = lvl
        self.werte = werte.copy()           # .copy() gibt jedem Objekt eigene Werte
        self.fähigkeiten = fähigkeiten.copy()
        self.max_leben = self.werte["Leben"]
        
    def level_up(self):
        self.lvl += 1
        self.max_leben = self.max_leben *(1+ (self.lvl * 0.05))         
        self.werte["Leben"] = self.werte["Leben"] * (1+ (self.lvl *0.05))
        self.werte["Schaden"] = self.werte["Schaden"] * (1+ (self.lvl * 0.05))
        print(50*"=")
        print(f"Dein {self.name} ist nun Level {self.lvl} !!!")
        print(f"Maximales Leben {self.max_leben} | Neuerangriffswerte {self.werte["Schaden"]}")

class haendler:
    def __init__(self, name, inventar):
        self.name = name
        self.inventar = inventar

    def zeige_waren(self):
        print(f"\n--- {self.name} ---")
        for k, v in self.inventar.items():
            print(f"{k}) {v['Name']} - {v['Preis']} Gold ({v['Info']})")

    def kaufen(self, spieler, wahl):
        if wahl not in self.inventar:
            print("Item nicht verfügbar!")
            return

        ware = self.inventar[wahl]

        if spieler.geld < ware["Preis"]:
            print("Nicht genug Geld!")
            return

        spieler.geld -= ware["Preis"]

        # INS INVENTAR LEGEN ODER ANZAHL ERHÖHEN
        for item in spieler.inventar.values():
            if item["Name"] == ware["Name"]:
                item["anzahl"] += 1
                print(f"{ware['Name']} gekauft! (Anzahl erhöht)")
                return

        # Neues Item ins Inventar
        neue_id = str(len(spieler.inventar) + 1)
        spieler.inventar[neue_id] = {
            "Name": ware["Name"],
            "Preis": ware["Preis"],
            "Info": ware["Info"],
            "anzahl": 1
        }

        print(f"{ware['Name']} neu ins Inventar gelegt!")

# WERTE & FÄHIGKEITEN 


shitmanda_werte = {"Leben": 150, "Schaden": 30, "Ausdauer": 60, "Element": "Süchtiger"}
shitmanda_fähigkeiten = {
    "1": {"Name": "Spritze werfen",  "Schaden": 3, "Kosten": 7},
    "2": {"Name": "Verfall",         "Schaden": 1, "Kosten": 3},
    "3": {"Name": "Preise drücken",  "Schaden": 2, "Kosten": 4},
    "4": {"Name": "LSD-Beschuss",    "Schaden": 4, "Kosten": 8},
}

opiati_werte = {"Leben": 190, "Schaden": 22, "Ausdauer": 60, "Element": "Prostituierte"}
opiati_fähigkeiten = {
    "1": {"Name": "Strippen",     "Schaden": 1, "Kosten": 2},
    "2": {"Name": "Lapdance",     "Schaden": 1, "Kosten": 4},
    "3": {"Name": "Pole Wurf",    "Schaden": 4, "Kosten": 9},
    "4": {"Name": "Money Theft",  "Schaden": 3, "Kosten": 6},
}

cracki_werte = {"Leben": 160, "Schaden": 25, "Ausdauer": 75, "Element": "Dealer"}
cracki_fähigkeiten = {
    "1": {"Name": "Ware strecken",              "Schaden": 1, "Kosten": 3},
    "2": {"Name": "LSD untermischen",           "Schaden": 2, "Kosten": 5},
    "3": {"Name": "Arschhaare ins Gras packen", "Schaden": 3, "Kosten": 6},
    "4": {"Name": "Preise erhöhen",             "Schaden": 4, "Kosten": 8},
}

walium_werte = {"Leben": 140, "Schaden": 32, "Ausdauer": 65, "Element": "Psycho"}
walium_fähigkeiten = {
    "1": {"Name": "Depressions Schrei", "Schaden": 1, "Kosten": 3},
    "2": {"Name": "Brückensprung",      "Schaden": 1, "Kosten": 3},
    "3": {"Name": "Stein Wurf",         "Schaden": 1, "Kosten": 3},
    "4": {"Name": "Eiterregen",         "Schaden": 1, "Kosten": 3},
}

kemonon_werte = {"Leben": 170, "Schaden": 24, "Ausdauer": 85, "Element": "Prostituierte"}
kemonon_fähigkeiten = {
    "1": {"Name": "Strippen",    "Schaden": 1, "Kosten": 2},
    "2": {"Name": "Lapdance",    "Schaden": 1, "Kosten": 4},
    "3": {"Name": "Pole Wurf",   "Schaden": 4, "Kosten": 9},
    "4": {"Name": "Money Theft", "Schaden": 3, "Kosten": 6},
}

# FIX: densur_fähigkeiten hatte "schaden" (klein) statt "Schaden" – vereinheitlicht
densur_werte = {"Leben": 145, "Schaden": 28, "Ausdauer": 90, "Element": "Süchtiger"}
densur_fähigkeiten = {
    "1": {"Name": "Spritze werfen", "Schaden": 3, "Kosten": 7},
    "2": {"Name": "Verfall",        "Schaden": 1, "Kosten": 3},
    "3": {"Name": "Preise drücken", "Schaden": 2, "Kosten": 4},
    "4": {"Name": "LSD-Beschuss",   "Schaden": 4, "Kosten": 8},
}

steifling_werte = {"Leben": 200, "Schaden": 26, "Ausdauer": 45, "Element": "Prostituierte"}
steifling_fähigkeiten = {
    "1": {"Name": "Strippen",    "Schaden": 1, "Kosten": 2},
    "2": {"Name": "Lapdance",    "Schaden": 1, "Kosten": 4},
    "3": {"Name": "Pole Wurf",   "Schaden": 4, "Kosten": 9},
    "4": {"Name": "Money Theft", "Schaden": 3, "Kosten": 6},
}

hebuta_werte = {"Leben": 180, "Schaden": 23, "Ausdauer": 100, "Element": "Süchtiger"}
hebuta_fähigkeiten = {
    "1": {"Name": "Spritze werfen", "Schaden": 3, "Kosten": 7},
    "2": {"Name": "Verfall",        "Schaden": 1, "Kosten": 3},
    "3": {"Name": "Preise drücken", "Schaden": 2, "Kosten": 4},
    "4": {"Name": "LSD-Beschuss",   "Schaden": 4, "Kosten": 8},
}

ögula_werte = {"Leben": 155, "Schaden": 27, "Ausdauer": 20, "Element": "Dealer"}
ögula_fähigkeiten = {
    "1": {"Name": "Ware strecken",              "Schaden": 1, "Kosten": 3},
    "2": {"Name": "LSD untermischen",           "Schaden": 2, "Kosten": 5},
    "3": {"Name": "Arschhaare ins Gras packen", "Schaden": 3, "Kosten": 6},
    "4": {"Name": "Preise erhöhen",             "Schaden": 4, "Kosten": 8},
}

Jacklee_werte = {"Leben": 150, "Schaden": 30, "Ausdauer": 60, "Element": "Psycho"}
Jacklee_fähigkeiten = {
    "1": {"Name": "Depressions Schrei", "Schaden": 1, "Kosten": 3},
    "2": {"Name": "Brückensprung",      "Schaden": 1, "Kosten": 3},
    "3": {"Name": "Stein Wurf",         "Schaden": 1, "Kosten": 3},
    "4": {"Name": "Eiterregen",         "Schaden": 1, "Kosten": 3},
}



# FUNKTIONEN


def inventar_öffnen(inventar):
    inventar_anzeigen = inventar

    while True:
        print("\n--- Inventar ---")

        if not inventar_anzeigen:
            print("(leer)")
        else:
            for k, v in inventar_anzeigen.items():
                print(f"{k}) {v['Name']} - {v['Preis']} Gold ({v['Info']}) | Anzahl: {v['anzahl']}")
        print("0) Verlassen")

        wahl= input("Möchtest du etwas nutzen?!")

        if wahl == "0":
            break
        ziel = spieler1.cracki_aktiv
        if wahl in inventar_anzeigen:
            item = inventar_anzeigen[wahl]
            if item["anzahl"] > 0:
                item["anzahl"] -= 1
                if item['Name'] == "Canabis":
                    heilung = ziel.max_leben / 2
                    ziel.werte["Leben"] += heilung
                    print(f"{ziel.name} wurde um {heilung} hp geheilt")
                    print(f"{item['Name']} benutzt!")
                elif item['Name'] == "Speed":
                    
                    ziel.werte["Schaden"] *= 1.2
                    schaden = ziel.werte["Schaden"]
                    print(f"{ziel.name} Schaden wurde erhöht und beträgt nun {schaden} Schaden")
                    print(f"{item['Name']} benutzt!")
                elif item['Name'] == "Heroin":
                    
                    ziel.werte["Leben"] = ziel.max_leben 
                    print(f"{ziel.name} wurde vollständig geheilt geheilt")
                    print(f"{item['Name']} benutzt!")
                elif item["Name"] == "Crackpfeife":
                    print("Du bist jetzt ein bisschen benebelt und die Pfeife verschwendet, SIE IST ZUM FANGEN GEDACHT")
            else:
                print("Kein Vorrat mehr!")
        else:
            print("\nUngültige Wahl.")


def fähigkeiten_anzeigen(liste):
    print("\nFähigkeiten:")
    for k, v in liste.items():
        print(f"  {k})  {v['Name']}  Schaden({v['Schaden']})  Ausdauer-Kosten({v['Kosten']})")


def fähigkeiten_nutzen(angreifer, ziel):
    fähigkeiten_anzeigen(angreifer.fähigkeiten)
    text = True
    while True:
        try:
            auswahl = int(input("Welche Fähigkeit möchtest du benutzen? (5) = warten: "))
            if auswahl == 5:
                print(f"Dein {angreifer.name} setzt aus!")
                text = False
                break
            elif 1 <= auswahl <= 4:
                umwandeln = list(angreifer.fähigkeiten.items())
                paar = umwandeln[auswahl - 1]
                daten = paar[1]
                name   = daten["Name"]
                schaden = daten["Schaden"]
                kosten  = daten["Kosten"]

                if angreifer.werte["Ausdauer"] < kosten:
                    print("Nicht genug Ausdauer für diese Attacke!")
                    continue
                else:
                    break
            else:
                print("Bitte 1-4 oder 5 eingeben.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")
        except IndexError:
            print("Außerhalb der Liste.")

    if text:
        gesamt_schaden =  schaden * angreifer.werte["Schaden"]
        ziel.werte["Leben"] -= schaden * angreifer.werte["Schaden"]
        angreifer.werte["Ausdauer"] -= kosten
        print(f"Dein {angreifer.name} benutzt {name}  und verursacht {gesamt_schaden}!")


def gegner_greift_an(angreifer, ziel):
    text = True
    while True:
        try:
            auswahl = random.randint(1, 5)
            if auswahl == 5:
                print(f"Das gegnerische {angreifer.name} setzt aus!")
                text = False
                break
            else:
                umwandeln = list(angreifer.fähigkeiten.items())
                paar  = umwandeln[auswahl - 1]
                daten = paar[1]
                name   = daten["Name"]
                schaden = daten["Schaden"]
                kosten  = daten["Kosten"]

                if angreifer.werte["Ausdauer"] < kosten:
                    continue          # zu wenig Ausdauer → nächste Runde
                else:
                    break
        except IndexError:
            continue

    if text:
        gesamt_schaden =  schaden * angreifer.werte["Schaden"]
        ziel.werte["Leben"] -= schaden * angreifer.werte["Schaden"]
        angreifer.werte["Ausdauer"] -= kosten
        print(f"Gegnerischer {angreifer.name} greift mit {name} an und verursacht {gesamt_schaden} Schaden!")


def cracki_auswahl():
    print("\n--- Deine Crackimons ---")
    for i, c in enumerate(spieler1.c_lebend):
        print(f"  {i + 1}. {c.name}  (Leben: {c.werte['Leben']}  Ausdauer: {c.werte['Ausdauer']})")
    # ... (deine Anzeige-Logik)
    while True:
        try:
            wahl = int(input("Welches Crackimon soll kämpfen? "))
            gewählt = spieler1.c_lebend[wahl - 1]
            if gewählt.werte["Leben"] <= 0:
                print("Das ist tot, nimm ein anderes!")
                continue
            
            spieler1.cracki_aktiv = gewählt
            print(f"{gewählt.name} tritt vor!")
            return gewählt
        except:
            print("Ungültig!")


def kampf_starten(spieler_crackimon, gegner_crackimon):
    print(f"\nEin {gegner_crackimon.status} {gegner_crackimon.name} erscheint!")


    while spieler_crackimon.werte["Leben"] > 0 and gegner_crackimon.werte["Leben"] > 0:

        print(f"\n--- {spieler_crackimon.name}: {spieler_crackimon.werte['Leben']} LP | "
              f"{gegner_crackimon.name}: {gegner_crackimon.werte['Leben']} LP ---")
        print(f"--- {spieler_crackimon.name}: {spieler_crackimon.werte['Ausdauer']} Ausdauer | "
              f"{gegner_crackimon.name}: {gegner_crackimon.werte['Ausdauer']} Ausdauer ---")
        time.sleep(2)
        print(50 * "=")
        print(4 * "-" + "Kämpfen  (1)|(2)  Inventar" + 4 * "-")
        print(4 * "-" + "Crackis  (3)|(4)  Crackpfeife" + 4 * "-")
        print(50 * "=")
        wahl = input("--     Wähle eine Option     --     ")
        print()

        if wahl == "1":
            fähigkeiten_nutzen(spieler_crackimon, gegner_crackimon)
            time.sleep(2)
        elif wahl == "2":
            inventar_öffnen(spieler1.inventar)
            time.sleep(2)
        elif wahl == "3":
            gewählt = cracki_auswahl()
            spieler_crackimon = gewählt
            spieler1.cracki_aktiv = gewählt

            time.sleep(2)
            continue
        elif wahl == "4":
            print("Crackpfeife werfen")
            fangen(gegner_crackimon)
            time.sleep(2)
        else:
            print("Hast du auch Drogen genommen?")
            time.sleep(2)

      
        # Prüfen, ob Gegner besiegt
        if gegner_crackimon.werte["Leben"] <= 0:
            print("\n" + 50 * "=")
            print(f"{gegner_crackimon.name} wurde besiegt! Du hast gewonnen!")
            
            spieler_crackimon.level_up()
            spieler1.cracki_aktiv.werte["Leben"] = spieler1.cracki_aktiv.max_leben
            reset_gegner() 
            geld()
            time.sleep(2)
            print()
            for cracki in spieler1.c_lebend:
                cracki.werte["Leben"] = cracki.max_leben
            print("Alle deine Crackimons wurden geheilt!")
            return True 
                    
        # Gegner greift an
        gegner_greift_an(gegner_crackimon, spieler_crackimon)

        # Prüfen, ob Spieler besiegt
        if spieler_crackimon.werte["Leben"] <= 0:
            print("\n" + 50 * "=")
            print(f"DEIN {spieler_crackimon.name} IST K.O.!")
            
            # Prüfen, ob noch jemand lebt
            noch_lebende = [c for c in spieler1.c_lebend if c.werte["Leben"] > 0]
            
            if not noch_lebende:
                print("Alle deine Crackimons sind am Ende. Du hast den Kampf verloren!")
                reset_gegner()
                return False 
            else:
                print("Wähle ein anderes Crackimon!")
                cracki_auswahl()
                spieler_crackimon = spieler1.cracki_aktiv
                time.sleep(2)
   

def fangen(ziel):
  
    pfeifen_anzahl = 0
    pfeifen_item = None
    
    for item in spieler1.inventar.values():
        if item["Name"] == "Crackpfeife":
            pfeifen_anzahl = item["anzahl"]
            pfeifen_item = item
            break


    if ziel.status != "Wild":
        print("Dieses Crackimon gehört schon jemandem oder ist nicht fangbar!")
        return

    if pfeifen_anzahl <= 0:
        print("DU HAST KEINE CRACKPFEIFEN! Geh zum Dealer!")
        return


    pfeifen_item["anzahl"] -= 1  
    lebens_prozent = ziel.werte["Leben"] / ziel.max_leben
    

    fang_chance = 0.10 + (1 - lebens_prozent) * 0.70
    wurf = random.random()

    print(f"Du wirfst eine Crackpfeife auf {ziel.name}...")
    
    if wurf <= fang_chance:
        print(f"Erfolg! {ziel.name} ist jetzt dein Sklave.")
        ziel.status = "Gefangen"
        spieler1.c_lebend.append(ziel)
        alle_crackimon.remove(ziel)

        ziel.werte["Leben"] = 0 
    else:
        print(f"Verdammt! {ziel.name} hat die Pfeife einfach weggekickt!")

# CRACKIMON ERSTELLEN

shitmanda0 = crackimon("Gefangen", 1, "Shitmanda", shitmanda_werte, shitmanda_fähigkeiten)
kemonon0 = crackimon("Gefangen", 1, "Kemonon", kemonon_werte, kemonon_fähigkeiten)
Densur0 = crackimon("Gefangen", 1, "Densur", densur_werte, densur_fähigkeiten)
steifling0 = crackimon("Gefangen", 1, "Steifling", steifling_werte, steifling_fähigkeiten)
walium0 = crackimon("Gefangen", 1, "Walium", walium_werte, walium_fähigkeiten)
hebuta0 = crackimon("Gefangen", 1, "Hebuta", hebuta_werte, hebuta_fähigkeiten)
opiati0 = crackimon("Gefangen", 1, "Opiati", opiati_werte, opiati_fähigkeiten)
ögula0 = crackimon("Gefangen", 1, "Ögula", ögula_werte, ögula_fähigkeiten)
jacklee0 = crackimon("Gefangen", 1, "Jacklee", Jacklee_werte, Jacklee_fähigkeiten)
cracki0 = crackimon("Gefangen", 1, "Cracki", cracki_werte, cracki_fähigkeiten)

shitmanda = crackimon("Wild", 1, "Shitmanda", shitmanda_werte, shitmanda_fähigkeiten)
kemonon = crackimon("Wild", 1, "Kemonon", kemonon_werte, kemonon_fähigkeiten)
Densur = crackimon("Wild", 1, "Densur", densur_werte, densur_fähigkeiten)
steifling = crackimon("Wild", 1, "Steifling", steifling_werte, steifling_fähigkeiten)
walium = crackimon("Wild", 1, "Walium", walium_werte, walium_fähigkeiten)
hebuta = crackimon("Wild", 1, "Hebuta", hebuta_werte, hebuta_fähigkeiten)
opiati = crackimon("Wild", 1, "Opiati", opiati_werte, opiati_fähigkeiten)
ögula = crackimon("Wild", 1, "Ögula", ögula_werte, ögula_fähigkeiten)
jacklee = crackimon("Wild", 1, "Jacklee", Jacklee_werte, Jacklee_fähigkeiten)
cracki = crackimon("Wild", 1, "Cracki", cracki_werte, cracki_fähigkeiten)

alle_crackimon = [cracki,opiati,walium,Densur,shitmanda,kemonon,steifling,hebuta,ögula,jacklee ]

def reset_gegner():
    zufall_lvl = random.randint(1,6)
    global shitmanda,Densur,walium,opiati,cracki,kemonon,steifling,hebuta,ögula,jacklee
    shitmanda = crackimon("Wild", 1, "Shitmanda", shitmanda_werte, shitmanda_fähigkeiten)
    Densur = crackimon("Wild", 1, "Densur", densur_werte, densur_fähigkeiten)
    walium = crackimon("Wild", 1, "Walium", walium_werte, walium_fähigkeiten)
    opiati = crackimon("Wild", 1, "Opiati", opiati_werte, opiati_fähigkeiten)
    cracki = crackimon("Wild", 1, "Cracki", cracki_werte, cracki_fähigkeiten)
    shitmanda = crackimon("Wild", 1, "Shitmanda", shitmanda_werte, shitmanda_fähigkeiten)
    kemonon = crackimon("Wild", 1, "Kemonon", kemonon_werte, kemonon_fähigkeiten)
    Densur = crackimon("Wild", 1, "Densur", densur_werte, densur_fähigkeiten)
    steifling = crackimon("Wild", 1, "Steifling", steifling_werte, steifling_fähigkeiten)
    walium = crackimon("Wild", 1, "Walium", walium_werte, walium_fähigkeiten)
    Hebuta = crackimon("Wild", 1, "Hebuta", hebuta_werte, hebuta_fähigkeiten)
    opiati = crackimon("Wild", 1, "Opiati", opiati_werte, opiati_fähigkeiten)
    Ögula = crackimon("Wild", 1, "Ögula", ögula_werte, ögula_fähigkeiten)
    Jacklee = crackimon("Wild", 1, "Jacklee", Jacklee_werte, Jacklee_fähigkeiten)
    cracki = crackimon("Wild", 1, "Cracki", cracki_werte, cracki_fähigkeiten)


def neuer_kampf():
    global alle_crackimon
    reset_gegner()
    gegner = random.choice(alle_crackimon)


    while spieler1.cracki_aktiv.werte["Leben"] <= 0:
        print("\nDEIN AKTIVES CRACKIMON IST KO!")
        print("1) Anderes Crackimon wählen | 2) Zum Dealer (Heilen)")
        wahl = input("Was tust du? ")
        
        if wahl == "1":
            cracki_auswahl() 
        elif wahl == "2":
            besuche_dealer()
        
    win = kampf_starten(spieler1.cracki_aktiv, gegner)
    return win

def hauptmenü():
    hauptmenü = True
    while hauptmenü:
        aktion = input("\nWas willst du tun? (Kampf / Dealer / Inventar / Ende): ").lower()
        if aktion == "kampf":
            sieg = neuer_kampf()
            if sieg:
              geld()
        elif aktion == "dealer":
            besuche_dealer()
        elif aktion == "inventar":
            inventar_öffnen(spieler1.inventar)
        elif aktion == "ende":
            break

def geld():
    kohle = random.randint(60,150)
    print(f"{spieler1.name} an {kohle} von den zerstörten Crackimon gestohlen!")
    spieler1.geld += kohle
    print(f"Der Kontostand: {spieler1.geld} Crack-Dolars")

# SPIELSTART


inventar = {}
c_lebend = []
c_tot    = []



# HÄNDLER ERSTELLEN

shop = haendler("Dealer Bob", {
    "1": {"Name": "Canabis", "Preis": 20, "Info": "Beruhigt die Nerven"},
    "2": {"Name": "Speed",   "Preis": 35, "Info": "Erhöht Fokus"},
    "3": {"Name": "Heroin",  "Preis": 50, "Info": "Heilt stark"},
    "4": {"Name": "Crackpfeife", "Preis": 50, "Info": "Wird zum Fangen benutzt"}
})


def besuche_dealer():
    while True:
        shop.zeige_waren()
        print("0) Verlassen")
        print(f"Gold: {spieler1.geld}")

        wahl = input("Was möchtest du kaufen? ").strip()

        if wahl == "0":
            break

        shop.kaufen(spieler1, wahl)



# STORY-MODUS 


def story_modus():
    print("\n" + 60 * "━")
    print("KAPITEL 1: DER AUFSTIEG IM CRACK-VIERTEL")
    print(60 * "━")
    print(f"Nach deinem ersten Sieg hat {spieler1.name} Blut geleckt.")
    print("Dein Ziel: Der ultimative Crack-König der Stadt zu werden.")
    

    print("\n[STATION: Der dunkle Hinterhof]")
    print("Ein wildes Crackimon versperrt dir den Weg zum nächsten Dealer!")
    #spieler1.cracki_aktiv.werte["Leben"] = spieler1.cracki_aktiv.max_leben
    sieg = neuer_kampf()
    
    if not sieg:
        print("Du wurdest im Hinterhof ausgeraubt. Die Story endet hier im Dreck.")
        return

    print("\nStark! Der Weg zum Dealer ist frei. Du solltest dich eindecken.")
    besuche_dealer()

   
    print("\n[STATION: Die Parkbank der Schande]")
    print("Auf deiner Stamm-Parkbank sitzt ein Rivale. Zeit für eine Lektion!")
    #spieler1.cracki_aktiv.werte["Leben"] = spieler1.cracki_aktiv.max_leben
    sieg = neuer_kampf()
    
    if sieg:
        print(f"\nRespekt! Du hast die Bank zurückerobert. Dein {spieler1.cracki_aktiv.name} sieht gut aus.")
    
        
    else:
        print("Die Parkbank gehört jetzt dem Gegner. Du ziehst dich zurück.")
        return


    print("\n[FINALE: Der Bahnhofsvorplatz]")
    print("Der Boss der Gegend hat gehört, dass du seine Leute verkloppst.")
    print("Er schickt sein stärkstes Crackimon vor!")
    #spieler1.cracki_aktiv.werte["Leben"] = spieler1.cracki_aktiv.max_leben
    boss_gegner = random.choice(alle_crackimon)
    boss_gegner.max_leben += 500
    boss_gegner.werte["Leben"] = boss_gegner.max_leben
    boss_gegner.werte["Schaden"] += 30
    
    print(f"BOSS-KAMPF: {boss_gegner.name} (Level {boss_gegner.lvl + 2}) fordert dich heraus!")
    
    sieg = kampf_starten(spieler1.cracki_aktiv, boss_gegner)
    
    if sieg:
        print("\n" + 60 * "X")
        print(f"UNGLAUBLICH! {spieler1.name} hat den Boss gestürzt!")
        print(f"Du bist nun der Herrscher über alle Crackpfeifen der Stadt.")
        print("DEIN NAME WIRD IN JEDER ENTZUGSKLINIK GEFÜRCHTET!")
        print(60 * "X")
    else:
        print("\nDer Boss war zu stark. Du endest als kleiner Laufbursche.")
                    


# ERSTER KAMPF
print("Willkommen bei Crackimon!")

name        = input("Bitte gib deinen Spielernamen ein: ")
sex         = input("Sehr gut, gib bitte dein Geschlecht ein: ")
abhängigkeit = input("Nun zur wichtigsten Frage – welche Droge feierst du am meisten? ")

spieler1 = spieler(name, sex, abhängigkeit, inventar, c_tot, c_lebend,0,None)

print(f"Sehr gut! Du bist {spieler1.name}, Geschlecht: {spieler1.sex}, süchtig nach: {spieler1.abhängigkeit}!")
print("Nun bist du an der Reihe, ein Crackimon zu wählen!")


while True:
    auswahl = input("Du hast die Wahl zwischen drei Crackimons! Welchen möchtest du wählen? "
                    "(shitmanda / opiati / walium): ").strip().lower()
    if auswahl == "shitmanda":
        print(f"Du hast {shitmanda.name} gewählt! Element: Süchtiger!")
        c_lebend.append(shitmanda0)
        break
    elif auswahl == "opiati":
        print(f"Du hast {opiati.name} gewählt! Element: Prostituierte!")
        c_lebend.append(opiati0)
        break
    elif auswahl == "walium":
        print(f"Du hast {walium.name} gewählt! Element: Psycho!")
        c_lebend.append(walium0)
        break
    else:
        print("Ungültige Wahl! Wähle shitmanda, opiati oder walium.")

c_lebend.append(cracki0)        


print("Dein erster Kampf beginnt bald – knall dir noch eine Dosis rein, bevor es zu wild wird!")
abfrage = True
while abfrage ==True:
    kampfabfrage = input("Nimmst du Schlapschwanz die Herausforderung an? (ja/nein): ").strip().lower()
    if kampfabfrage == "ja":
        print("Du hast Eier bewiesen, nun nutze sie auch.")
        gegner = random.choice(alle_crackimon)
        spieler1.cracki_aktiv = spieler1.c_lebend[0]
        gewon = kampf_starten( spieler1.cracki_aktiv, gegner)
        

        

        if gewon == True:
            
            while True:
                auswahl2 = input("Wie möchtest du jetzt weiter machen? (Route / Dealer): ").strip().lower()
                if auswahl2 == "route":
                    print("Es geht weiter auf der Route!")
                    abfrage = False
                    break
                    
                elif auswahl2 == "dealer":
                    print("Du gehst zum Dealer...")
                    besuche_dealer()
                    inventar_öffnen(spieler1.inventar)
                    abfrage = False 
                    break
                else:
                    print("Ungültige Auswahl, du Crackhead!")
        else:
            print("Game Over! Geh dir erst mal einen Schuss setzen...")
            break

    elif kampfabfrage == "nein":
        print("Du beschissene Pussy, geh in deine Crackhöhle zurück, du Lelek!")
        gewon = False
        break
    else:
        print("Ja oder Nein, mehr Optionen gibt's hier nicht.")
        

if gewon == True:
    story_modus()
    
    
   