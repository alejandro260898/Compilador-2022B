from Compilador.AnalizadorLexico import AnalizadorLexico
from Ventana.Ventana import Ventana

def __main__():
    ventana = Ventana("Compilador V1")
    analizadorLexico = AnalizadorLexico(ventana)
    
    ventana.mostrarte()
    cadTokens =  ventana.leerEntrada("Ingrese sus tokens separados por espacios")
    
    analizadorLexico.analizar(cadTokens)
    
__main__()