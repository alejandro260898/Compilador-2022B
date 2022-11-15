from Compilador.NoTerminal import NoTerminal
from Ventana.Ventana import Ventana

class ArbolSintatico:
    def __init__(self, ventana:Ventana, raiz:NoTerminal = None):
        self.ventana = ventana
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
        self.ventana.imprime(tabs+nodoInicio.dameSimbolo(), tabulaciones)
        
        tabulaciones += 1
        for simbolo in reversed(nodoInicio.dameSimbolos()): 
            tabs = ''
            for i in range(tabulaciones):
                if(i == tabulaciones - 1): tabs += 'L '
                else: tabs += ' '
            self.ventana.imprime(tabs+simbolo.dameSimbolo(), tabulaciones)
        for hijoNodo in reversed(nodoInicio.dameNodosHijos()): self.recorrer(hijoNodo, tabulaciones)