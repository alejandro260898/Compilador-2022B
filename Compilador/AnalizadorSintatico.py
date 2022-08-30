from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.Interfaces.ConstantesAnalizadorLexico import ConstantesAnalizadorexico
from EstructuraDatos.Pila import Pila
from Ventana.Ventana import Ventana

class AnalizaroSintatico(ConstantesAnalizadorexico):
    def __init__(self, ventana:Ventana):
        self.ventana = ventana
        self.tabla = []
        self.pila = Pila()
        
    def analizar(self, lexico:AnalizadorLexico):
        self.pila.push(self.TOKENS[self.SIGNO_PESOS])
        self.pila.push(0)
        while(lexico.terminado()):
            lexema = lexico.sigSimbolo()
        return 0