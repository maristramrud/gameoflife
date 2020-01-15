## GAME OF LIFE
# HOVEDPROGRAM

# Importerer spillebrettet
from spillebrett import Spillebrett
from celle import Celle

def main():
    # Bruker oppgir dimensjonene til spillebrettet
    rader = int(input("Oppgi antall rader: "))
    kolonner = int(input("Oppgi antall kolonner: "))
    # Oppretter den nullte versjonen av spillebrettet med dimensjonene
    # som bruker oppga
    spill = Spillebrett(rader, kolonner)
    spill.tegnBrett()
    print("Generasjon:", spill._generasjon, " - Antall levende celler:", spill.finnAntallLevende())
    # Oppretter en menylokke for brukeren
    while True:
        valg = input("Trykk enter for aa fortsette. Trykk q for aa avslutte: ")
        if valg == "":
            spill.oppdatering()
            spill.tegnBrett()
            # Printer ut generasjon og antall levende celler
            print("Generasjon:", spill._generasjon, "- Antall levende celler:", spill.finnAntallLevende())
        else:
            break

# Starter hovedprogrammet
main()
