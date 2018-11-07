# coding: utf-8

# Lager klassen
class Cell:

# Instansvariabel lages og status til klassen er i utgangspunktet død
    def __init__(self):
        self._status = "dead"

# Lager metode som kan sette status til død
    def set_dead(self):
        self._status = "dead"

# Lager metode som kan sette status til levende
    def set_alive(self):
        self._status = "alive"

# Lager metode som returnerer True hvis cellen lever, og False hvis død
    def is_alive(self):
        if self._status == "alive":
            return True
        return False

# Lager metode som returnerer O hvis levende og . hvis død
    def get_cell_status(self):
        if self._status == "alive":
            return "O"
        return "."