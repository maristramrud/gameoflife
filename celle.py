## GAME OF LIFE

# Oppretter klassen Celle
class Celle:
    # Konstruktor
    def __init__(self):
        self._celle = "dod"

    def __str__(self):
        penStreng = self.hentStatusTegn()
        return penStreng

    # Endre status
    def settDoed(self):
        self._celle = "dod"

    def settLevende(self):
        self._celle = "levende"

    # Hente status
    def erLevende(self):
        return self._celle == "levende"

    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        return "."
