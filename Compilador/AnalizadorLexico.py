import re
from Compilador.Interfaces.TipoSimbolo import TipoSimbolo
from Compilador.Interfaces.Patrones import Patrones
from Compilador.Nodo import Nodo
from Ventana.Componentes.Tabla import Tabla
from Ventana.Ventana import Ventana

class AnalizadorLexico(TipoSimbolo, Patrones):
    SEPARATOR_LEXEMA = " "
    
    def __init__(self, ventana:Ventana, cadSimbolos:str):
        self.posInicialCadSimbolos = 0
        self.cuentaSimbolos = 0
        self.cadSimbolos = cadSimbolos
        self.ventana = ventana
        self.seguimientoSimbolos = {} #Fines demostrativos
        
        self.inicializarTablaLexemas()
    
    def inicializarTablaLexemas(self):
        for simbolo in self.SIMBOLOS.keys():
            self.seguimientoSimbolos[simbolo] = []
            
    def encontrarSimbolo(self, lexema = ""):
        if(re.search(self.PATRON_TIPO, lexema) != None): return self.TIPO
        elif(re.search(self.PATRON_IF, lexema) != None): return self.IF
        elif(re.search(self.PATRON_ELSE, lexema) != None): return self.ELSE
        elif(re.search(self.PATRON_WHILE, lexema) != None): return self.WHILE
        elif(re.search(self.PATRON_RETURN, lexema) != None): return self.RETURN
        elif(re.search(self.PATRON_IDENTIFICADOR, lexema) != None): return self.IDENTIFICADOR
        elif(re.search(self.PATRON_CADENA, lexema) != None): return self.CADENA
        elif(re.search(self.PATRON_REAL, lexema) != None): return self.REAL
        elif(re.search(self.PATRON_ENTERO, lexema) != None): return self.ENTERO
        elif(re.search(self.PATRON_OP_SUM, lexema) != None): return self.OP_SUM
        elif(re.search(self.PATRON_OP_MUL, lexema) != None): return self.OP_MUL
        elif(re.search(self.PATRON_IGUAL, lexema) != None): return self.IGUAL
        elif(re.search(self.PATRON_OP_IGUALDAD, lexema) != None): return self.OP_IGUALDAD
        elif(re.search(self.PATRON_OP_RELAC, lexema) != None): return self.OP_RELAC
        elif(re.search(self.PATRON_OP_AND, lexema) != None): return self.OP_AND
        elif(re.search(self.PATRON_OP_OR, lexema) != None): return self.OP_OR
        elif(re.search(self.PATRON_OP_NOT, lexema) != None): return self.OP_NOT
        elif(re.search(self.PATRON_PARENTESIS_DER, lexema) != None): return self.PARENTESIS_DER
        elif(re.search(self.PATRON_PARENTESIS_IZQ, lexema) != None): return self.PARENTESIS_IZQ
        elif(re.search(self.PATRON_LLAVE_DER, lexema) != None): return self.LLAVE_DER
        elif(re.search(self.PATRON_LLAVE_IZQ, lexema) != None): return self.LLAVE_IZQ
        elif(re.search(self.PATRON_PUNTO_COMA, lexema) != None): return self.PUNTO_COMA
        elif(re.search(self.PATRON_COMA, lexema) != None): return self.COMA
        elif(re.search(self.PATRON_PESOS, lexema) != None): return self.PESOS
        else: return self.ERROR
    
    def analizarSencillamente(self, cadSimbolos = ""):
        simbolos = {
            self.NOM_IDENTIDICADORES: [],
            self.NOM_NUM_REALES: [],
            self.NOM_NUM_ENTEROS: [],
            self.NOM_ERRORES: []
        }
        
        for simbolo in re.split(self.SEPARATOR_LEXEMA, cadSimbolos):
            if(re.search(self.PATRON_IDENTIFICADOR, simbolo) == None):
                if(re.search(self.PATRON_REAL, simbolo) == None):
                    if(re.search(self.PATRON_ENTERO, simbolo) == None): 
                        simbolos[self.NOM_ERRORES].append(simbolo)
                    else: simbolos[self.NOM_NUM_ENTEROS].append(simbolo)
                else: simbolos[self.NOM_NUM_REALES].append(simbolo)
            else: simbolos[self.NOM_IDENTIDICADORES].append(simbolo)
        
        tabla = Tabla()
        for col, datos in simbolos.items():
            self.tabla.fijaColumna(col)
            self.tabla.fijaDatos(col, datos)
        self.ventana.imprimirTabla(None, tabla.dameTabla())
        
    def analizarConTabla(self, cadSimbolos = ""):
        for simbolo in re.split(self.SEPARATOR_LEXEMA, cadSimbolos):
            simboloID = self.encontrarSimbolo(simbolo)
            if(simboloID != self.ERROR): self.seguimientoSimbolos[simboloID].append(simbolo)
            else: self.seguimientoSimbolos[self.ERROR].append(simbolo)
            
        columnasAMostrar = 5
        cuentaColumnas = 0
        tabla = Tabla()
        for simboloID, datos in self.seguimientoSimbolos.items():
            col = self.SIMBOLOS[simboloID] if(simboloID != self.ERROR) else  self.SIMBOLOS[self.ERROR]
            if(cuentaColumnas < columnasAMostrar):
                cuentaColumnas += 1
            else:    
                self.ventana.imprimirTabla(None, tabla.dameTabla())
                cuentaColumnas = 0
                tabla = Tabla()
            tabla.fijaColumna(col)
            tabla.fijaDatos(col, datos)
        if(cuentaColumnas > 0): self.ventana.imprimirTabla(None, tabla.dameTabla())
    
    def terminado(self):
        return self.posInicialCadSimbolos == len(self.cadSimbolos)
    
    def sigSimbolo(self) -> Nodo:
        if(self.posInicialCadSimbolos == len(self.cadSimbolos)):
            return Nodo(self.PESOS, self.SIMBOLOS[self.PESOS])
        else:
            for patronID in self.PATRONES.keys():
                concurrencia = re.search(
                    self.PATRONES[patronID], 
                    self.cadSimbolos[self.posInicialCadSimbolos:]
                )
                if(concurrencia != None):
                    posInicialAnterior = self.posInicialCadSimbolos
                    self.posInicialCadSimbolos = self.posInicialCadSimbolos + concurrencia.end()
                    if(self.PATRONES[patronID] == self.PATRON_BLANCOS): continue
                    else: 
                        self.cuentaSimbolos += 1
                        return Nodo(
                            patronID, 
                            self.cadSimbolos[posInicialAnterior:self.posInicialCadSimbolos]
                        )
            raise ValueError('Simbolo no correspondiente: '+self.cadSimbolos[self.posInicialCadSimbolos:])