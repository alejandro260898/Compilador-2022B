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
    
    def recorrer(self, nodoInicio:NoTerminal = None, tabulaciones = 0):
        if(nodoInicio == None): nodoInicio = self.raiz
        
        tabs = ''
        for i in range(tabulaciones):
            if(i == tabulaciones - 1): tabs += 'L '
            else: tabs += ' '
        print(tabs+nodoInicio.dameSimbolo())
        
        for hijoNodo in nodoInicio.dameNodosHijos(): self.recorrer(hijoNodo, tabulaciones + 1)
        tabulaciones += 1
        for simbolo in nodoInicio.dameSimbolos(): 
            tabs = ''
            for i in range(tabulaciones):
                if(i == tabulaciones - 1): tabs += 'L '
                else: tabs += ' '
            print(tabs+simbolo)