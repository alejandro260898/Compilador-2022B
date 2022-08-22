import re
from tkinter import SEPARATOR
from Compilador.Interfaces.ConstantesAnalizadorLexico import ConstantesAnalizadorexico

from Ventana.Componentes.Tabla import Tabla

class AnalizadorLexico(ConstantesAnalizadorexico):
    SEPARATOR_TOKEN = " "
    EXPRESION_ID = "^[a-zA-Z][a-zA-Z0-9]*$"
    EXPRESION_NUM_REAL = "^[0-9]+[.][0-9]+$"
    EXPRESION_NUM_ENTERO = "^[0-9]+[0-9]*$"
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.tabla = None
    
    def analizar(self, cadTokens):
        identificadores = []
        numReales = []
        numEnteros = []
        errores = []
        
        tokens = re.split(self.SEPARATOR_TOKEN, cadTokens)
        for token in tokens:
            if(re.search(self.EXPRESION_ID, token) == None):
                if(re.search(self.EXPRESION_NUM_REAL, token) == None):
                    if(re.search(self.EXPRESION_NUM_ENTERO, token) == None): errores.append(token)
                    else: numEnteros.append(token)
                else: numReales.append(token)
            else: identificadores.append(token)
        
        self.tabla = Tabla()
        self.tabla.fijaColumna(self.NOM_IDENTIDICADORES)
        self.tabla.fijaColumna(self.NOM_NUM_REALES)
        self.tabla.fijaColumna(self.NOM_NUM_ENTEROS)
        self.tabla.fijaColumna(self.NOM_ERRORES)
        self.tabla.fijaDatos(self.NOM_IDENTIDICADORES, identificadores)
        self.tabla.fijaDatos(self.NOM_NUM_REALES, numReales)
        self.tabla.fijaDatos(self.NOM_NUM_ENTEROS, numEnteros)
        self.tabla.fijaDatos(self.NOM_ERRORES, errores)
        
        self.ventana.imprimirTabla(None, self.tabla.dameTabla())