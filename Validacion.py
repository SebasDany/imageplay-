class validacion():
 nombre_imagen=""
 descripcion_imagen=""
 def __init__(self):
        print("Instanciando clase")

 def set_nombre_imagen(self,nombre):
        self.nombre_imagen=nombre



 def set_descripcion_imagen(self, descripcion):
    self.descripcion_imagen=descripcion


 def get_descripcion_imagen(self):
    print(self.descripcion_imagen)
    return self.descripcion_imagen


 def return_tamanio_de_palabra(self):

     return len(self.nombre_imagen)
 def return_letras(self):
    return self.nombre_imagen[0]+"/"+self.nombre_imagen[len(self.nombre_imagen)-1]