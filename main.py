from Compilador.AnalizadorLexico import AnalizadorLexico
from Compilador.AnalizadorSemantico import AnalizadorSemantico
from Compilador.AnalizadorSintatico import AnalizaroSintatico
from Ventana.Ventana import Ventana
import os

RUTA_ARCHIVO = "./main.c" #Este arhivo es de ejemplo para futuras mejoras

def __main__():
    ventana = Ventana("Compilador V10")
    ventana.mostrarte()
    cadSimbolos = ventana.leerEntrada(RUTA_ARCHIVO)

    analizadorLexico = AnalizadorLexico(ventana, cadSimbolos)
    analizadorSintatico = AnalizaroSintatico(ventana, analizadorLexico)
    analizadorSemantico = AnalizadorSemantico(ventana)
    if(analizadorSintatico.analizar()): print("Compilación con errores") 
    else: 
        analizadorSemantico.analizar(analizadorSintatico.dameArbolSintatico())
        os.system('nasm -f elf -o main-elf.o main.asm')
        os.system('ld -m elf_i386 -o main --entry=main main-elf.o')
        print("Compilación OK")
        print("Revise el archivo resumen.txt para revisar los resultados de la compilación")
        
    ventana.cerrar()
    
__main__()