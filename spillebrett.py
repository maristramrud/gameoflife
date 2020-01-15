## GAME OF LIFE
# SPILLEBRETT

# Importerer random og klassen Celle
from random import randint
from celle import Celle

# Oppretter klassen Spillebrett
class Spillebrett:

    # Oppretter en konstruktor med instansvariabler for rader og kolonner
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjon = 0
        # Oppretter et rutenett som en tom liste
        self._rutenett = []
        for i in range(self._rader):
            self._rutenett.append([])
            for j in range(self._kolonner):
                self._rutenett[i].append(Celle())
        # Genererer nullte versjon av spillebrettet
        self._generer()

    # Oppretter en metode som genererer den nullte versjonen av spillebrettet
    def _generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                tilfeldig = randint(0, 2)
                if tilfeldig == 2:
                    self._rutenett[i][j].settLevende()

    # Oppretter en metode som tegner spillebrettet ved aa bruke __str__
    def tegnBrett(self):
        # Lager et lite mellomrom mellom utskriften av hvert spillebrett
        for i in range(5):
            print()
        print(self)

    # Oppretter en __str__ - metode som lager en strengrepresentasjon
    # av spillebrettet.
    def __str__(self):
        penStreng = ""
        # Bruker en for-loop til aa gaa gjennom rutenettet, og gjore om
        # hvert celleobjekt til en streng.
        for rad in self._rutenett:
            for celle in rad:
                penStreng += str(celle) + " "
            penStreng += "\n"
        return penStreng

    # Oppretter en metode som finner nabocellene, og returnerer en
    # liste med disse
    # Deler av denne metoden ble gjennomgaatt i gruppe 1
    def finnNabo(self, rad, kolonne):
        naboListe = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Hindrer at elementet blir sin egen nabo
                naboRad = rad + i
                naboKolonne = kolonne + j
                gyldig = True
                # Bruker if-tester for aa sjekke naboene til cellen,
                # og bruker 0 som referansepunkt.
                if 0 > naboRad or naboRad >= self._rader:
                    gyldig = False
                elif 0 > naboKolonne or naboKolonne >= self._kolonner:
                    gyldig = False
                elif naboRad == rad and naboKolonne == kolonne:
                    gyldig = False
                if gyldig:
                    naboListe.append(self._rutenett[naboRad][naboKolonne])
        # Returnerer en liste med alle cellens naboer
        return naboListe

    # Oppretter en metode som beregner neste generasjon av celler
    def oppdatering(self):
        endreTilLevende = [] # celler som skal bli levende
        endreTilDod = []  # celler som skal bli dode
        # Gaar gjennom rutenettet ved hjelp av en nostet for-loop
        for i in range(self._rader):
            for j in range(self._kolonner):
                # Sjekker cellens status ved aa kalle paa metoden hentStatusTegn
                # fra klassen Celle, og bruker finnNabo-metoden for aa sjekke
                # antall levende naboer.
                naboer = self.finnNabo(i,j)
                levendeNaboer = []
                for nabo in naboer:
                    if nabo.erLevende():
                        levendeNaboer.append(nabo)
                # Gaar inn i if dersom cellen har status levende.
                # Sjekker om den levende cellen har mindre enn 2 eller mer
                # enn 3 levende naboer slik at den ikke skal
                # fortsette aa leve videre
                if self._rutenett[i][j].erLevende():
                    if len(levendeNaboer) < 2 or len(levendeNaboer) > 3:
                        endreTilDod.append(self._rutenett[i][j])
                # Gaar inn i else hvis cellen har status dod og sjekker om
                # antall levende naboer er lik 3
                elif len(levendeNaboer) == 3:
                    endreTilLevende.append(self._rutenett[i][j])

        # Endrer status paa de riktige cellene ved hjelp av for-loops og
        # metodene settLevende og settDoed fra klassen Celle.
        for celle in endreTilLevende:
            celle.settLevende()
        for celle in endreTilDod:
            celle.settDoed()
        # Oppdaterer generasjonsnummer
        self._generasjon += 1

    # Oppretter en metode som skal beregne antall levende celler
    # paa spillebrettet.
    def finnAntallLevende(self):
        antallLevendeCeller = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende():
                    antallLevendeCeller += 1
                else:
                    antallLevendeCeller = antallLevendeCeller
        return antallLevendeCeller
