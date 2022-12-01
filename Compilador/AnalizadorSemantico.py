from EstructuraDatos.ArbolSintatico import ArbolSintatico
from Compilador.TablaSimbolos import TablaSimbolos
from Compilador.NoTerminal import NoTerminal
from Ventana.Componentes.Tabla import Tabla
from Compilador.Interfaces.Reducciones import Reducciones
from Compilador.Interfaces.TipoDato import TipoDato
from Ventana.Ventana import Ventana

class AnalizadorSemantico:
    GLOBAL = "$global"
    
    def __init__(self, ventana:Ventana):
        self.ventana = ventana
        self.tablaSimbolos = TablaSimbolos()
        self.tablaFunciones = TablaSimbolos()
        
    def verifica(self, nodoInicio:NoTerminal = None, ambito:str = "", tipoDato:str = "", accion:str = "") -> None:
        simbolo = nodoInicio.dameSimbolo()
        
        if(simbolo == Reducciones.REDUCCIONES[Reducciones.R6] or accion == Reducciones.REDUCCIONES[Reducciones.R6]):
            accion = Reducciones.REDUCCIONES[Reducciones.R6]
            for simbolo in reversed(nodoInicio.dameSimbolos()):
                if(
                    simbolo.dameTokenID() == TipoDato.INT or simbolo.dameTokenID() == TipoDato.FLOAT or
                    simbolo.dameTokenID() == TipoDato.CHAR or simbolo.dameTokenID() == TipoDato.STRING
                ):
                    tipoDato = simbolo.dameSimbolo()
                elif(simbolo.dameSimbolo() != '\e'):
                    self.tablaSimbolos.fijaInfo(TablaSimbolos.NOMBRE, simbolo.dameSimbolo())
                    self.tablaSimbolos.fijaInfo(TablaSimbolos.TIPO_DATO, tipoDato)
                    self.tablaSimbolos.fijaInfo(TablaSimbolos.AMBITO, ambito)
        elif(simbolo == Reducciones.REDUCCIONES[Reducciones.R9] or accion == Reducciones.REDUCCIONES[Reducciones.R9]):
            for simbolo in reversed(nodoInicio.dameSimbolos()):
                if(
                    simbolo.dameTokenID() == TipoDato.INT or simbolo.dameTokenID() == TipoDato.FLOAT or
                    simbolo.dameTokenID() == TipoDato.CHAR or simbolo.dameTokenID() == TipoDato.STRING
                ):
                    tipoDato = simbolo.dameSimbolo()
                elif(simbolo.dameSimbolo() != '\e'):
                    ambito = f"${simbolo.dameSimbolo()}"
                    self.tablaFunciones.fijaInfo(TablaSimbolos.NOMBRE, simbolo.dameSimbolo())
                    self.tablaFunciones.fijaInfo(TablaSimbolos.TIPO_DATO, tipoDato)
                    self.tablaFunciones.fijaInfo(TablaSimbolos.AMBITO, "$global")
        elif(simbolo == Reducciones.REDUCCIONES[Reducciones.R10] or accion == Reducciones.REDUCCIONES[Reducciones.R10]):
            accion = Reducciones.REDUCCIONES[Reducciones.R10]
            for simbolo in reversed(nodoInicio.dameSimbolos()):
                if(
                    simbolo.dameTokenID() == TipoDato.INT or simbolo.dameTokenID() == TipoDato.FLOAT or
                    simbolo.dameTokenID() == TipoDato.CHAR or simbolo.dameTokenID() == TipoDato.STRING
                ):
                    tipoDato = simbolo.dameSimbolo()
                elif(simbolo.dameSimbolo() != '\e'):
                    self.tablaSimbolos.fijaInfo(TablaSimbolos.NOMBRE, simbolo.dameSimbolo())
                    self.tablaSimbolos.fijaInfo(TablaSimbolos.TIPO_DATO, tipoDato)
                    self.tablaSimbolos.fijaInfo(TablaSimbolos.AMBITO, ambito)
                
        for hijoNodo in reversed(nodoInicio.dameNodosHijos()): 
            self.verifica(hijoNodo, ambito, tipoDato, accion)
        
    def analizar(self, arbolSintatico:ArbolSintatico) -> None:
        self.verifica(arbolSintatico.dameRaiz(), self.GLOBAL, "", "")
        
        tabla = Tabla()
        self.ventana.imprimeTitulo(titulo="Tabla Simbolos (Variables)")
        for key, datos in self.tablaSimbolos.dameTabla().items():
            tabla.fijaColumna(key)
            tabla.fijaDatos(key, datos)
        self.ventana.imprimirTabla(None, tabla.dameTabla())
        
        tabla = Tabla()
        self.ventana.imprimeTitulo(titulo="Tabla Simbolos (Funciones)")
        for key, datos in self.tablaFunciones.dameTabla().items():
            tabla.fijaColumna(key)
            tabla.fijaDatos(key, datos)
        self.ventana.imprimirTabla(None, tabla.dameTabla())