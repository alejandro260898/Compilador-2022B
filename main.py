from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.AnalizadorSemantico import AnalizadorSemantico
from Compilador.AnalizadorSintatico import AnalizaroSintatico
from Ventana.Ventana import Ventana

RUTA_ARCHIVO = "./main.txt"

def __main__():
    ventana = Ventana("Compilador V9")
    ventana.mostrarte()
    cadSimbolos = ventana.leerEntrada(RUTA_ARCHIVO)

    analizadorLexico = AnalizadorLexico(ventana, cadSimbolos)
    analizadorSintatico = AnalizaroSintatico(ventana, analizadorLexico)
    analizadorSemantico = AnalizadorSemantico(ventana)
    if(analizadorSintatico.analizar()): print("Compilación con errores") 
    else: 
        analizadorSemantico.analizar(analizadorSintatico.dameArbolSintatico())
        print("\nCompilación OK")
    
__main__()