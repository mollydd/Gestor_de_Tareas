from Tarea_principal import Tarea
import json

almacenador_tareas=[]

def pedir_opcion(opcion):
    try:
        opcion=int(input(opcion))
        if 1<= opcion <= 6:
            return  opcion
        else:
            print("solo se admiten numeros del 1 al 6 como metodo d respuesta, por favor intentelo de nuevo")
    except ValueError:
        print("Error, solo se admiten numeros")

def agregar_tarea():
    id=int(input("ingrese el codigo: "))
    titulo=input("ingrese el titulo de la tarea: ")
    descripcion=input("ingrese la descripcion: ")
    estado=input("ingrese el estado de la tarea: ")
    prioridad=input("ingrese la prioridad de la tarea: ")
    tarea= Tarea(id, titulo, descripcion, estado, prioridad)
    almacenador_tareas.append(tarea)

def Auxiliar_buscar_por_id(id):
    while True:
        id_pedir=int(input(id))
        for i in almacenador_tareas:
            if i.id ==  id_pedir:
                return i.titulo
        return None

def mostrar_tareas():
    if not almacenador_tareas:
        print("lo sentimos, no hay tareas guardadas en este momento")
    else:
        for tarea in almacenador_tareas:
            tarea.mostrar_datos()

def guardar_tarea():
    datos=[]
    for tarea in almacenador_tareas:
        datos.append(tarea.convertir_tarea_a_diccionario())
    with open("tareas.json" , "w") as archivo:
        json.dump(datos,archivo)

"este sirve para cargar los datos"
def cargar_tareas():
    with open("tareas.json" , "r") as archivo:
        datos= json.load(archivo)

    for i in datos:
        objeto_sacado= Tarea( i["id"],              
                              i["titulo"],          
                              i["descripcion"],    
                              i["estado"],
                              i["prioridad"])
        almacenador_tareas.append(objeto_sacado)

    



