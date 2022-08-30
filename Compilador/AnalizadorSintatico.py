from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.Interfaces.Reducciones import Reducciones
from Compilador.Interfaces.TipoSimbolo import TipoSimbolo
from EstructuraDatos.Pila import Pila
from Ventana.Ventana import Ventana

class AnalizaroSintatico(TipoSimbolo, Reducciones):
    def __init__(self, ventana:Ventana):
        self.ventana = ventana
        self.gramatica = {}
        self.pila = Pila()
        
    def inicializarGramatica(self):
        self.gramatica = {
            self.E:             [1,  0,  0,  0,  0],
            self.SIGNO_PESOS:   [0, -1,  0,  0, -2],
            self.OP_SUMA:       [0,  0,  3,  0,  0],
            self.IDENTIFICADOR: [2,  0,  0,  4,  0],
            # self.E:             [1,  0,  0,  4,  0],
            # self.SIGNO_PESOS:   [0, -1, -3,  0, -2],
            # self.OP_SUMA:       [0,  0,  3,  0,  0],
            # self.IDENTIFICADOR: [2,  0,  0,  2,  0],
        }
        
    def analizar(self, lexico:AnalizadorLexico):
        self.inicializarGramatica()
        self.pila.push(self.TOKENS[self.SIGNO_PESOS])
        self.pila.push(0)
        while(lexico.terminado()):
            lexema = lexico.sigSimbolo()
            # fil = al tope de la pila y col = al token ID del simbolo etregado por el lexema
            accion = self.gramatica[lexema.dameTokenID()][self.pila.top()]
            
            self.ventana.imprime(self.pila.showYourself())
            self.ventana.imprime(lexema.dameSimbolo())
            self.ventana.imprime(accion)
            self.ventana.imprimeSeparacion()
            
            self.pila.push(lexema.dameSimbolo())
            self.pila.push(accion)
        
        accion = self.gramatica[self.SIGNO_PESOS][self.pila.top()]
        self.ventana.imprime(self.pila.showYourself())
        self.ventana.imprime(self.TOKENS[self.SIGNO_PESOS])
        self.ventana.imprime(f"Reducción {self.REDUCCIONES[accion]}")
        self.ventana.imprimeSeparacion()
        
        self.pila.push(self.TOKENS[self.E])
        self.pila.push(self.REDUCCIONES[accion])