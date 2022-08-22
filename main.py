from Compilador.AnalizadorLexico import AnalizadorLexico
from Ventana.Ventana import Ventana

def __main__():
    ventana = Ventana("Compilador V2")
    analizadorLexico = AnalizadorLexico(ventana)
    
    ventana.mostrarte()
    cadTokens =  ventana.leerEntrada("Ingrese sus tokens separados por espacios")
    
    # analizadorLexico.analizarSencillamente(cadTokens)
    analizadorLexico.analizar(cadTokens)
    
__main__()