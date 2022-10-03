from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.Interfaces.Reducciones import Reducciones
from Compilador.Interfaces.TipoSimbolo import TipoSimbolo
from Compilador.NoTerminal import NoTerminal
from EstructuraDatos.ArbolSintatico import ArbolSintatico
from Compilador.Nodo import Nodo
from EstructuraDatos.Pila import Pila
from Ventana.Ventana import Ventana

import csv

class AnalizaroSintatico(TipoSimbolo, Reducciones):
    ARCHIVO_GRAMATICA = './GramaticaCompilador/compilador.csv'
    REDUCCION = 'r'
    DESPLAZAMIENTO = 'd'
    ERROR_GRAMATICAL = 1
    GRAMATICA_OK = 0
    
    def __init__(self, ventana:Ventana, analizadorLexico:AnalizadorLexico):
        self.ventana = ventana
        self.analizadorLexico = analizadorLexico
        self.gramatica = []
        self.pila = Pila()
        self.arbolSintatico = ArbolSintatico()
        
        self.inicializarGramatica()
        
    def inicializarGramatica(self):
        cuentaLineas = 0
        lineaAIgnorar = 1
        with open(self.ARCHIVO_GRAMATICA, newline='') as GramaticaExcel:  
            reader = csv.reader(GramaticaExcel)
            for fila in reader:
                if(cuentaLineas >= lineaAIgnorar):
                    self.gramatica.append([ dato for dato in fila[1:] ])
                else: cuentaLineas += 1
    
    def mostrarInfoActual(self, simbolo:Nodo, accion):
        self.ventana.imprime('simbolo: '+simbolo.dameSimbolo())
        self.ventana.imprime('accion: '+accion)
        self.ventana.imprime(self.pila.showYourself())
        self.ventana.imprimeSeparacion()
    
    def crearRama(self, nodo:NoTerminal, nodosPops:list):
        if(len(nodosPops) == 0):
            nodo.fijaSimbolo('\e')
        else:
            for n in nodosPops:
                if(type(n) == NoTerminal): nodo.fijaNodoHijo(nodo)
                elif(type(n) == Nodo):
                    token = n.dameTokenID()
                    if(token == self.PUNTO_COMA or token == self.COMA or token == self.PARENTESIS_DER or
                    token == self.PARENTESIS_IZQ or token == self.LLAVE_DER or token == self.LLAVE_IZQ):
                        continue
                    else: nodo.fijaSimbolo(n.dameSimbolo())
                else: continue
        
        act = self.arbolSintatico.dameNodoActual()
        print('inicio')
        if(act != None): 
            act.fijaPadre(nodo)
        self.arbolSintatico.fijaNodoActual(nodo)
    
    def reduccir(self, reduccion) -> Nodo:
        nodosPops = []
        cuentaPops = 0
        reduccionID = (-1 * int(reduccion[1:]))
        totalReducciones = self.POPS[reduccionID] * 2
        while(cuentaPops < totalReducciones):
            cuentaPops += 1
            nodosPops.append(self.pila.pop())
        nodo = NoTerminal(self.REDUCCIONES_ID[reduccionID], self.REDUCCIONES[reduccionID])
        self.crearRama(nodo, nodosPops)
        return nodo
    
    def analizar(self):
        self.pila.push(Nodo(self.PESOS, self.SIMBOLOS[self.PESOS]))
        self.pila.push(0)
        
        self.ventana.imprime(self.pila.showYourself())
        while(not self.analizadorLexico.terminado()): # fil = al tope de la pila y col = al token ID del simbolo etregado por el analizador lexico
            simbolo = self.analizadorLexico.sigSimbolo()
            
            while(True):
                accion = self.gramatica[self.pila.top()][simbolo.dameTokenID()]
                accionTemp = accion
                
                if(accion != ''):
                    accionCad = accion[0:1]
                    
                    if(self.REDUCCION == accionCad): #Se sacarán elementos de la pila
                        if(accion == self.R0):
                            self.arbolSintatico.fijaRaiz(self.arbolSintatico.dameNodoActual())
                            return self.GRAMATICA_OK
                        else:
                            simboloR = self.reduccir(accion)
                            accion = self.gramatica[self.pila.top()][simboloR.dameTokenID()]
                            self.pila.push(simboloR)
                            self.pila.push(int(accion))
                            self.mostrarInfoActual(simbolo, accionTemp)
                        
                    elif(self.DESPLAZAMIENTO == accionCad): #Se agregaran elementos
                        self.pila.push(simbolo)
                        self.pila.push(int(accion[1:]))
                        self.mostrarInfoActual(simbolo, accionTemp)
                        if(self.analizadorLexico.terminado()): simbolo = self.analizadorLexico.sigSimbolo()
                        else: break
                else:
                    self.ventana.imprime(f"Error de sintaxis en: {simbolo.dameSimbolo()}")
                    return self.ERROR_GRAMATICAL
            