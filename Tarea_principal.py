class Tarea:
    def __init__(self, id, titulo, descripcion, estado, prioridad):
        self.id= id
        self.titulo= titulo
        self.descripcion= descripcion
        self.estado= estado
        self.prioridad= prioridad

    def mostrar_datos(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Descripción:", self.descripcion)
        print("Estado:", self.estado)
        print("Prioridad:", self.prioridad)

    def convertir_tarea_a_diccionario(self):
        diccionario={ 
        "id": self.id,
        "titulo": self.titulo,
        "descripcion": self.descripcion,
        "estado": self.estado,
        "prioridad": self.prioridad
    }
        return diccionario

    