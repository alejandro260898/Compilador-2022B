from Compilador.NoTerminal import NoTerminal

class ArbolSintatico:
    def __init__(self, raiz:NoTerminal = None):
        self.raiz = raiz
        self.act = None
        
    def fijaRaiz(self, raiz:NoTerminal):
        self.raiz = raiz
        
    def dameRaiz(self) -> NoTerminal:
        return self.raiz
    
    def fijaNodoActual(self, nodo:NoTerminal):
        self.act = nodo
        
    def dameNodoActual(self) -> NoTerminal|None:
        return self.act