from Compilador.Interfaces.TipoDato import TipoDato
from Compilador.TablaSimbolos import TablaSimbolos

class Nodo(TipoDato):
    def __init__(self, id = 0, simbolo = "", tablaSimbolos:TablaSimbolos = None):
        self.id = id
        self.simbolo = simbolo
        self.tipoDato = self.INDEFINIDO
        self.ambito = ""
        self.tablaSimbolos = tablaSimbolos
        
    def fijaTokenID(self, id):
        self.id = id
        
    def fijaSimbolo(self, simbolo):
        self.simbolo = simbolo
        
    def dameTokenID(self):
        return self.id
        
    def dameSimbolo(self):
        return self.simbolo
    
    def validarTipo(self):
        return 0