
class Ventana:
    NOM_ARCHIVO_LOG = "./resumen.txt"
    
    def __init__(self, titulo):
        self.archivo = open(self.NOM_ARCHIVO_LOG, "w")
        self.titulo = titulo
    
    def mostrarte(self):
        self.archivo.write(f"********** {self.titulo} **********\n")
        
    # def leerEntrada(self, mensaje):
    #     return input(f"{mensaje} : ")
    
    def leerEntrada(self, ruta):
        codigo = ""
        with open(ruta) as archivo:
            for linea in archivo:
                codigo += linea
        return codigo
    
    def imprime(self, mensaje:str, char = "-"):
        self.archivo.write(f"[{char}] {mensaje}\n")
    
    def imprimeSeparacion(self, char = "-", maxCol = 20):
        separacion = ""
        for i in range(maxCol):
            separacion += char
        separacion += "\n"
            
        self.archivo.write(separacion)
        
    def imprimeTitulo(self, char = "+", titulo:str = "", maxCol = 20):
        tituloDecorado = "\n"
        for i in range(int(maxCol/2)):
            tituloDecorado += char
        tituloDecorado += titulo.upper()
        for i in range(int(maxCol/2)):
            tituloDecorado += char
        tituloDecorado += "\n"
            
        self.archivo.write(tituloDecorado)
    
    def imprimirTabla(self, area = None, tabla = None):
        # print("\n")
        self.archivo.write(tabla)
        
    def cerrar(self):
        self.archivo.close()