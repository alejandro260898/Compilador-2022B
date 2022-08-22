class Tabla:
    SALTO_LINEA = "\n"
    SEPARADOR_COLUMNA = "|"
    SEPARADOR_FILA = "-"
    
    def __init__(self):
        self.tabla = {}
        self.tamDatosMasLargo = 0
        
    def obtenerTamPalabraMasLarga(self):
        tamPalabraMasLarga = 0
        
        for col in self.tabla.keys():
            tamPalabra = len(col)
            if(tamPalabra > tamPalabraMasLarga): tamPalabraMasLarga = tamPalabra
                
        for datos in self.tabla.values():
            if(len(datos) > self.tamDatosMasLargo): self.tamDatosMasLargo = len(datos) 
            for fil in datos:
                tamPalabra = len(fil)
                if(tamPalabra > tamPalabraMasLarga): tamPalabraMasLarga = tamPalabra
            
        return tamPalabraMasLarga
    
    def obtenerSeparacionVertical(self, tam):
        separacion = ""
        totalColumnas = len(self.tabla.keys())
        for i in range(round((totalColumnas * tam) + (totalColumnas + 1))):
            separacion += self.SEPARADOR_FILA
        separacion += self.SALTO_LINEA
        
        return separacion
    
    def obtenerPalabraArreglada(self, palabra, tamMaximo):
        tamRestante = tamMaximo - len(palabra)
        palabraArreglada = palabra
        for i in range(tamRestante):
            palabraArreglada += " "
        palabraArreglada += self.SEPARADOR_COLUMNA
        
        return palabraArreglada
            
    def fijaColumna(self, nomColumna = ""):
        if(len(nomColumna) > 0):
            self.tabla[nomColumna] = []
            return True
        else: return False
        
    def fijaDatos(self, nomColumna = "", datos = []):
        if(len(nomColumna) > 0 and len(datos) > 0):
            self.tabla[nomColumna] = datos
            return True
        else: return False
    
    def dameTabla(self):
        tabla = ""
        tamPalabraMasLarga = self.obtenerTamPalabraMasLarga()
        separacion = self.obtenerSeparacionVertical(tamPalabraMasLarga)
        
        #Mostramos las columnas
        tabla = separacion
        tabla += self.SEPARADOR_COLUMNA
        for col in self.tabla.keys():
            tabla += self.obtenerPalabraArreglada(col, tamPalabraMasLarga)
        tabla += self.SALTO_LINEA
        tabla += separacion
        
        #Mostramos las filas
        for i in range(self.tamDatosMasLargo):
            tabla += self.SEPARADOR_COLUMNA
            for col in self.tabla.keys():
                try:
                    tabla += self.obtenerPalabraArreglada(self.tabla[col][i], tamPalabraMasLarga)
                except: tabla += self.obtenerPalabraArreglada(" ", tamPalabraMasLarga)
            tabla += self.SALTO_LINEA
            tabla += separacion
            
        return tabla