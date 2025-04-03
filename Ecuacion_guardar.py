class Ecuacion_guardar:
    def __init__(self,nombre_archivo="ecuacion.txt"):
        self.nombre_archivo=nombre_archivo
        
    def guardar_ecuacion(self,ecuaciom):
        with open(self.nombre_archivo, "w") as archivo:
            archivo.write(ecuaciom)