
class Ventana:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrarte(self):
        print(f"********** {self.titulo} **********\n")
        
    def leerEntrada(self, mensaje):
        return input(f"{mensaje} : ")
    
    def imprime(self, mensaje:str, char = "-"):
        return print(f"[{char}] {mensaje}")
    
    def imprimeSeparacion(self, char = "-", maxCol = 20):
        separacion = ""
        for i in range(maxCol):
            separacion += char
        print(separacion)
        
    def imprimeTitulo(self, char = "+", titulo:str = "", maxCol = 20):
        tituloDecorado = "\n"
        for i in range(int(maxCol/2)):
            tituloDecorado += char
        tituloDecorado += titulo.upper()
        for i in range(int(maxCol/2)):
            tituloDecorado += char
        print(tituloDecorado)
    
    def imprimirTabla(self, area = None, tabla = None):
        print("\n")
        print(tabla)