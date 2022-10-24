from Compilador.TablaSimbolos import TablaSimbolos
from EstructuraDatos.ArbolSintatico import ArbolSintatico
from Ventana.Ventana import Ventana

class AnalizadorSemantico:
    def __init__(self, ventana:Ventana,  tablaSimbolos:TablaSimbolos = None):
        self.ventana = ventana
        self.tablaSimbolos = tablaSimbolos
        
    def analizar(self, arbolSintatico:ArbolSintatico):
        return 0
        