
class Ventana:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrarte(self):
        print(f"********** {self.titulo} **********")
        
    def leerEntrada(self, mensaje):
        return input(f"{mensaje} : ")
    
    def imprime(self, mensaje):
        return print(f"[-] {mensaje}.")
    
    def imprimirTabla(self, area = None, tabla = None):
        print("\n")
        print(tabla)