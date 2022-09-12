import re
from Compilador.Interfaces.TipoSimbolo import TipoSimbolo
from Compilador.Interfaces.Patrones import Patrones
from Compilador.Nodo import Nodo
from Ventana.Componentes.Tabla import Tabla
from Ventana.Ventana import Ventana

class AnalizadorLexico(TipoSimbolo, Patrones):
    SEPARATOR_LEXEMA = " "
    
    def __init__(self, ventana:Ventana):
        self.ventana = ventana
        self.tabla = None
        self.lexemas = {}
        self.simbolos = []
        self.cuentaSimbolos = 0

    
    def inicializarTablaLexemas(self):
        for token in self.TOKENS.keys():
            self.lexemas[token] = []
        self.lexemas[self.ERROR] = []
            
    def encontrarToken(self, lexema = ""):
        if(lexema == ""): return self.ERROR
        else:
            if(re.search(self.PATRON_TIPO, lexema) != None): return self.TIPO_DATO
            elif(re.search(self.PATRON_IF, lexema) != None): return self.IF
            elif(re.search(self.PATRON_ELSE, lexema) != None): return self.ELSE
            elif(re.search(self.PATRON_WHILE, lexema) != None): return self.WHILE
            elif(re.search(self.PATRON_RETURN, lexema) != None): return self.RETURN
            elif(re.search(self.PATRON_ID, lexema) != None): return self.IDENTIFICADOR
            elif(re.search(self.PATRON_CADENA, lexema) != None): return self.CADENA
            elif(re.search(self.PATRON_NUM_REAL, lexema) != None): return self.REAL
            elif(re.search(self.PATRON_NUM_ENTERO, lexema) != None): return self.ENTERO
            elif(re.search(self.PATRON_OP_ADICION, lexema) != None): return self.OP_SUMA
            elif(re.search(self.PATRON_OP_MULTIPLICACION, lexema) != None): return self.OP_MULTIPLICACION
            elif(re.search(self.PATRON_OP_ASIGNACION, lexema) != None): return self.SIGNO_IGUAL
            elif(re.search(self.PATRON_OP_IGUALDAD, lexema) != None): return self.OP_IGUALDAD
            elif(re.search(self.PATRON_OP_RELACIONAL, lexema) != None): return self.OP_RELACIONAL
            elif(re.search(self.PATRON_OP_AND, lexema) != None): return self.OP_AND
            elif(re.search(self.PATRON_OP_OR, lexema) != None): return self.OP_OR
            elif(re.search(self.PATRON_OP_NOT, lexema) != None): return self.OP_NOT
            elif(re.search(self.PATRON_PARENTESIS_INICIO, lexema) != None): return self.SIGNO_PARRENTESIS_INICIO
            elif(re.search(self.PATRON_PARENTESIS_FIN, lexema) != None): return self.SIGNO_PARRENTESIS_FIN
            elif(re.search(self.PATRON_LLAVES_INICIO, lexema) != None): return self.SIGNO_LLAVES_INICIO
            elif(re.search(self.PATRON_LLAVES_FIN, lexema) != None): return self.SIGNO_LLAVES_FIN
            elif(re.search(self.PATRON_PUNTO_COMA, lexema) != None): return self.SIGNO_PUNTO_COMA
            elif(re.search(self.PATRON_COMA, lexema) != None): return self.SIGNO_COMA
            elif(re.search(self.PATRON_PESOS, lexema) != None): return self.SIGNO_PESOS
            else: return self.ERROR
    
    def analizarSencillamente(self, cadLexemas = ""):
        lexemas = {
            self.NOM_IDENTIDICADORES: [],
            self.NOM_NUM_REALES: [],
            self.NOM_NUM_ENTEROS: [],
            self.NOM_ERRORES: []
        }
        
        for lexema in re.split(self.SEPARATOR_LEXEMA, cadLexemas):
            if(re.search(self.PATRON_ID, lexema) == None):
                if(re.search(self.PATRON_NUM_REAL, lexema) == None):
                    if(re.search(self.PATRON_NUM_ENTERO, lexema) == None): 
                        lexemas[self.NOM_ERRORES].append(lexema)
                    else: lexemas[self.NOM_NUM_ENTEROS].append(lexema)
                else: lexemas[self.NOM_NUM_REALES].append(lexema)
            else: lexemas[self.NOM_IDENTIDICADORES].append(lexema)
        
        self.tabla = Tabla()
        for col, datos in lexemas.items():
            self.tabla.fijaColumna(col)
            self.tabla.fijaDatos(col, datos)
        self.ventana.imprimirTabla(None, self.tabla.dameTabla())
        
    def analizarConTabla(self, cadLexemas = ""):
        self.inicializarTablaLexemas()
        for lexema in re.split(self.SEPARATOR_LEXEMA, cadLexemas):
            tokenID = self.encontrarToken(lexema)
            if(tokenID != self.ERROR): self.lexemas[tokenID].append(lexema)
            else: self.lexemas[self.ERROR].append(lexema)
            
        columnasAMostrar = 5
        cuentaColumnas = 0
        self.tabla = Tabla()
        for tokenID, datos in self.lexemas.items():
            col = self.TOKENS[tokenID] if(tokenID != self.ERROR) else "error"
            if(cuentaColumnas < columnasAMostrar):
                cuentaColumnas += 1
            else:    
                self.ventana.imprimirTabla(None, self.tabla.dameTabla())
                cuentaColumnas = 0
                self.tabla = Tabla()
            self.tabla.fijaColumna(col)
            self.tabla.fijaDatos(col, datos)
        if(cuentaColumnas > 0): self.ventana.imprimirTabla(None, self.tabla.dameTabla())
        
    def analizar(self, cadLexemas = ""):
        for lexema in re.split(self.SEPARATOR_LEXEMA, cadLexemas):
            tokenID = self.encontrarToken(lexema)
            if(tokenID != self.ERROR): self.simbolos.insert(0, Nodo(tokenID, lexema))
            else:
                self.ventana.imprime(f"Simbolo desconocido: {lexema}")
                break
        self.inicializarCuentaSimbolos()
        
    def inicializarCuentaSimbolos(self):
        self.cuentaSimbolos = len(self.simbolos) - 1
        
    def terminado(self):
        return self.cuentaSimbolos < 0
    
    def sigSimbolo(self) -> Nodo:
        if(self.terminado()): lexema = Nodo(self.SIGNO_PESOS, self.TOKENS[self.SIGNO_PESOS])
        else:
            lexema = self.simbolos[self.cuentaSimbolos]
            self.cuentaSimbolos -= 1
        return lexema