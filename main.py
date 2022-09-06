from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.AnalizadorSintatico import AnalizaroSintatico
from Ventana.Ventana import Ventana

def __main__():
    ventana = Ventana("Compilador V4")
    analizadorLexico = AnalizadorLexico(ventana)
    analizadorSintatico = AnalizaroSintatico(ventana)
    
    ventana.mostrarte()
    cadTokens =  ventana.leerEntrada("Ingrese sus tokens separados por espacios")
    
    # analizadorLexico.analizarSencillamente(cadTokens)
    # analizadorLexico.analizarConTabla(cadTokens)
    analizadorLexico.analizar(cadTokens)
    analizadorSintatico.analizar(analizadorLexico)
    
__main__()