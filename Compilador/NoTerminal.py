from Compilador.Nodo import Nodo

class NoTerminal(Nodo):
    def __init__(self, id, nombre):
        self.padre = None
        self.simbolos = []
        self.nodosHijos = []
        Nodo.__init__(self, id, nombre)
        
    def fijaPadre(self, nodo):
        self.padre = nodo
        
    def fijaSimbolo(self, simbolo:str):
        self.simbolos.append(simbolo)
        
    def fijaNodoHijo(self, nodo):
        self.nodosHijos.append(nodo)
        
    def damePadre(self):
        return self.padre
        
    def dameNodosHijos(self) -> list:
        return self.nodosHijos
    
    def dameSimbolos(self) -> list:
        return self.simbolos
    
    
        
    