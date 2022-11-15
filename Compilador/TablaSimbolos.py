class TablaSimbolos:
    NOMBRE = 'Nombre'
    TIPO_DATO = 'Tipo'
    AMBITO = 'Ambito'
    
    def __init__(self):
        self.tabla = {
            self.NOMBRE : [],
            self.TIPO_DATO: [],
            self.AMBITO: []
        }
        
    def dameTabla(self) -> dict:
        return self.tabla
    
    def fijaInfo(self, clave:str, dato) -> bool:
        self.tabla[clave].append(dato)
        return True
    