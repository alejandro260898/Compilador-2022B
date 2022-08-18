
class Ventana:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrarte(self):
        print(f"********** {self.titulo} **********")
        
    def leerEntrada(self, mensaje):
        return input(f"{mensaje} : ")
    
    def imprimirTabla(self, area = None, titulo = "", datos = []):
        print("\n")
        print(f"{titulo}")
        for dato in datos:
            print(dato)