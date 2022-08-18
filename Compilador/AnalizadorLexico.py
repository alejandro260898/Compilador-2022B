import re
from tkinter import SEPARATOR

class AnalizadorLexico:
    SEPARATOR_TOKEN = " "
    EXPRESION_ID = "^[a-zA-Z][a-zA-Z0-9]*"
    EXPRESION_NUM_REAL = "^[0-9][.]+[0-9]+"
    EXPRESION_NUM_ENTERO = "^[0-9]+"
    
    def __init__(self, ventana):
        self.ventana = ventana
    
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
        
        self.ventana.imprimirTabla(None, "IDENTIFICADORES", identificadores)
        self.ventana.imprimirTabla(None, "NÚMEROS REALES", numReales)
        self.ventana.imprimirTabla(None, "NÚMEROS ENTEROS", numEnteros)
        self.ventana.imprimirTabla(None, "ERRORES", errores)