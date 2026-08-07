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
        id_pedir=int(input(id))
        for i in almacenador_tareas:
            if i.id ==  id_pedir:
                return i
        return None

def buscar_tarea():
    Tarea_encontrada=Auxiliar_buscar_por_id("ingrese el id correspondiente a la tarea que desea buscar: ")
    if Tarea_encontrada is None:
        print("lo sentimos, no hay una tarea registrada con ese id")
    else:
        return id.mostrar_datos()
    
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

def actualizar_tareas():
    tarea_encontrada= Auxiliar_buscar_por_id("ingrese el id correspondiente a la tarea que desea actualizar: ")
    if tarea_encontrada is None:
        print("no hay una tarea con ese id en estos momentos0")
        return

    print("Tarea encontrado")

    datos= int(input("que datos desea actualizar? escriba el numero d la opcion q desea cambiar: \n1. Titulo \n2.Descripcion \n3.Estado \n4.Prioridad"))
    if datos == 1:
        tarea_encontrada.titulo = input("ingrese el nuevo nombre de la tarea: ")
    elif datos == 2:
        tarea_encontrada.descripcion=input("ingrese la nueva descripcion de la tarea: ")
    elif datos == 3:
        tarea_encontrada.estado=input("ingrese el nuevo estado de la tarea: ")
    elif datos == 4:
        tarea_encontrada.prioridad=input("ingrese la nueva prioridad de la tarea: ")
    else:
        print("opcion invalida, ingrese nuevamente")

    guardar_tarea()
    
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

    



