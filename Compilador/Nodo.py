from Compilador.Interfaces.TipoDato import TipoDato

class Nodo(TipoDato):
    def __init__(self, id = 0, simbolo = ""):
        self.id = id
        self.simbolo = simbolo
        self.tipoDato = self.INDEFINIDO
        self.ambito = ""
        
    def fijaTokenID(self, id):
        self.id = id
        
    def fijaSimbolo(self, simbolo):
        self.simbolo = simbolo
        
    def dameTokenID(self):
        return self.id
        
    def dameSimbolo(self):
        return self.simbolo