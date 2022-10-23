from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.AnalizadorSintatico import AnalizaroSintatico
from Ventana.Ventana import Ventana


def __main__():
    ventana = Ventana("Compilador V7")
    ventana.mostrarte()
    cadSimbolos = ventana.leerEntrada("Ingrese sus simbolos")
    
    analizadorLexico = AnalizadorLexico(cadSimbolos, ventana)
    analizadorSintatico = AnalizaroSintatico(ventana, analizadorLexico)
    if(analizadorSintatico.analizar()): print("Compilación con errores") 
    else: print("\nCompilación OK")
    
__main__()