from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.Interfaces.Reducciones import Reducciones
from Compilador.Interfaces.TipoSimbolo import TipoSimbolo
from Compilador.Lexema import Lexema
from EstructuraDatos.Pila import Pila
from Ventana.Ventana import Ventana

class AnalizaroSintatico(TipoSimbolo, Reducciones):
    def __init__(self, ventana:Ventana):
        self.ventana = ventana
        self.gramatica = {}
        self.pila = Pila()
        
    def inicializarGramatica(self):
        self.gramatica = {
            # self.E:             [1,  0,  0,  0,  0],
            # self.SIGNO_PESOS:   [0, -1,  0,  0, -2],
            # self.OP_SUMA:       [0,  0,  3,  0,  0],
            # self.IDENTIFICADOR: [2,  0,  0,  4,  0],
            self.E:             [1,  0,  0,  4,  0],
            self.SIGNO_PESOS:   [0, -1, -3,  0, -2],
            self.OP_SUMA:       [0,  0,  3,  0,  0],
            self.IDENTIFICADOR: [2,  0,  0,  2,  0],
        }
        
    def limpiarPila(self, totalReducciones, accion):
        for i in range(totalReducciones):
            self.pila.pop()
        self.pila.push(Lexema(self.E, self.TOKENS[self.E]))
        self.pila.push(self.REDUCCIONES[accion])
        
    def analizar(self, lexico:AnalizadorLexico):
        self.inicializarGramatica()
        self.pila.push(Lexema(self.SIGNO_PESOS, self.TOKENS[self.SIGNO_PESOS]))
        self.pila.push(0)
        while(not lexico.terminado()):
            lexema = lexico.sigSimbolo()
            # fil = al tope de la pila y col = al token ID del simbolo etregado por el lexema
            accion = self.gramatica[lexema.dameTokenID()][self.pila.top()]
            
            if(accion != 0):
                self.ventana.imprime(self.pila.showYourself())
                self.ventana.imprime(lexema.dameSimbolo())
                self.ventana.imprime(accion)
                self.ventana.imprimeSeparacion()
                
                self.pila.push(lexema)
                self.pila.push(accion)
            else:
               self.ventana.imprime(f"Error de sintaxis en: {lexema.dameSimbolo()}")
               return 1
        
        lexema = lexico.sigSimbolo()
        while(lexema.dameTokenID() == self.SIGNO_PESOS):
            accion = self.gramatica[lexema.dameTokenID()][self.pila.top()]
            if(accion == self.R0):
                self.ventana.imprime(self.pila.showYourself())
                self.ventana.imprime(lexema.dameSimbolo())
                self.ventana.imprime(f"Reducción {self.REDUCCIONES[self.R0]}, aceptación")
                break
            else:
                self.ventana.imprime(self.pila.showYourself())
                self.ventana.imprime(lexema.dameSimbolo())
                self.ventana.imprime(f"Reducción {self.REDUCCIONES[accion]}")
                self.ventana.imprimeSeparacion()
                self.limpiarPila(self.POPS[accion], accion)
        return 0
            