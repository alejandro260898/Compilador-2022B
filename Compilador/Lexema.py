class Lexema:
    def __init__(self, id = 0, simbolo = ""):
        self.id = id
        self.simbolo = simbolo
        
    def fijaTokenID(self, id):
        self.id = id
        
    def fijaSimbolo(self, simbolo):
        self.simbolo = simbolo
        
    def dameTokenID(self):
        return self.id
        
    def dameSimbolo(self):
        return self.simbolo