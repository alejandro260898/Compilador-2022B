from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.AnalizadorSemantico import AnalizadorSemantico
from Compilador.AnalizadorSintatico import AnalizaroSintatico
from Compilador.TablaSimbolos import TablaSimbolos
from Ventana.Ventana import Ventana


def __main__():
    ventana = Ventana("Compilador V7")
    ventana.mostrarte()
    cadSimbolos = ventana.leerEntrada("Ingrese sus simbolos")

    tablaSimbolos = TablaSimbolos()
    analizadorLexico = AnalizadorLexico(cadSimbolos, ventana, tablaSimbolos)
    analizadorSintatico = AnalizaroSintatico(ventana, analizadorLexico)
    analizadorSemantico = AnalizadorSemantico(ventana, tablaSimbolos)
    if(analizadorSintatico.analizar()): print("Compilación con errores") 
    else: 
        analizadorSemantico.analizar(analizadorSintatico.dameArbolSintatico())
        print("\nCompilación OK")
    
__main__()