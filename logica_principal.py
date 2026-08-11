from Tarea_principal import Tarea
import json
import os 
carpeta=os.path.dirname(__file__)
unir=os.path.join(carpeta , "tareas.json")

almacenador_tareas=[]
def pedir_mensaje(mensaje):
    while True:
        texto=input(mensaje)
        limpiado= texto.strip()
        if limpiado == "":
            print("debe escribir un valor, ingrese nuevamente")
        else:
            return limpiado
        
def confirmar_eliminacion(mensaje):
    while True:
        opcion=input(mensaje)
        limpiado= opcion.strip().lower()
        if limpiado == "":
            print("debe escribir un valor, intentelo de nuevo")
        elif limpiado == "y":
            return limpiado
        elif limpiado == "n":
            print("opcion cancelada")
            return
        
def pedir_opcion(opcion):
    while True:
        try:
            opcion=int(input(opcion))
            if 1<= opcion <= 6:
                return  opcion
            else:
                print("solo se admiten numeros del 1 al 6 como metodo d respuesta, por favor intentelo de nuevo")
        except ValueError:
            print("Error, solo se admiten numeros")

def pedir_dato_actualizar(opcion):
    while True:
        try:
           opcion=int(input(opcion))
           if 1<= opcion <= 4:
                return opcion
           else:
                print("incorrecto, solo se permiten numeros del 1 al 4")
        except ValueError:
            print("invalido, solo se admiten numeros, intente nuevamente")

def opcion_prioridad(mensaje, opciones):
    while True:
        texto=pedir_mensaje(mensaje).lower()
        if texto in opciones:
            return texto
        else:
            print("debe ingresar opciones validas ")

def agregar_tarea():
    while True:
        try:
            id=int(input("ingrese el codigo: "))
            id_existente = False
        
            if id <= 0:
                print("error, debe ingresar numeros enteros mayores que cero")
            elif id > 0:
                for i in almacenador_tareas:
                    if i.id == id:
                        id_existente = True
                        break
                if id_existente:
                    print("ese ID ya existe")
                    continue
                break
        except ValueError:
            print("valor invalido, debe ingresar unicamente numeros, intentelo de nuevo")

    titulo=pedir_mensaje("ingrese el titulo de la tarea: ")
    descripcion=pedir_mensaje("ingrese la descripcion: ")
    estado=opcion_prioridad("ingrese el estado de la tarea(pendiente, en progreso, completada): " , ["pendiente", "en progreso", "completada"])
    prioridad=opcion_prioridad("ingrese la prioridad de la tarea(baja, media, alta): ",  ["baja", "media", "alta"])
    tarea= Tarea(id, titulo, descripcion, estado, prioridad)
    almacenador_tareas.append(tarea)

def Auxiliar_buscar_por_id(id):
        while True:
            try:
                id_pedir=int(input(id))
                
                if id_pedir <= 0:
                    print("invalido, ingrese solo numeros enteros mayores que 0")
                elif id_pedir > 0:
                    break
            except ValueError:
                print("valor invalido, debe ingresar unicamente numeros, intentelo de nuevo")

        for i in almacenador_tareas:
            if i.id ==  id_pedir:
                return i
        return None

def buscar_tarea():
    Tarea_encontrada=Auxiliar_buscar_por_id("ingrese el id correspondiente a la tarea que desea buscar: ")
    if Tarea_encontrada is None:
        print("lo sentimos, no hay una tarea registrada con ese id")
    else:
        Tarea_encontrada.mostrar_datos()
    
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
    with open(unir , "w") as archivo:
        json.dump(datos,archivo)

def actualizar_tareas():
    tarea_encontrada= Auxiliar_buscar_por_id("ingrese el id correspondiente a la tarea que desea actualizar: ")
    if tarea_encontrada is None:
        print("no hay una tarea con ese id en estos momentos")
        return

    print("Tarea encontrada")

    datos= pedir_dato_actualizar("que datos desea actualizar? escriba el numero d la opcion q desea cambiar: \n1. Titulo \n2.Descripcion \n3.Estado \n4.Prioridad : ")
    if datos == 1:
        tarea_encontrada.titulo = pedir_mensaje("ingrese el nuevo nombre de la tarea: ")
    elif datos == 2:
        tarea_encontrada.descripcion=pedir_mensaje("ingrese la nueva descripcion de la tarea: ")
    elif datos == 3:
        tarea_encontrada.estado=opcion_prioridad("ingrese el nuevo estado de la tarea: ",  ["pendiente", "en progreso", "completada"])
    elif datos == 4:
        tarea_encontrada.prioridad=opcion_prioridad("ingrese la nueva prioridad de la tarea: " , ["baja", "media", "alta"])
    else:
        print("opcion invalida, ingrese nuevamente")

    guardar_tarea()

"este sirve para cargar los datos"
def cargar_tareas():
    if not os.path.exists(unir):
        return
    
    if os.path.getsize(unir) == 0:
        return
    
    with open(unir , "r") as archivo:
        datos= json.load(archivo)

    for i in datos:
        objeto_sacado= Tarea( i["id"],              
                              i["titulo"],          
                              i["descripcion"],    
                              i["estado"],
                              i["prioridad"])
        almacenador_tareas.append(objeto_sacado)

def eliminar_tarea():
    pedir_id= Auxiliar_buscar_por_id("ingrese el id de la tarea a eliminar")
    if pedir_id is None:
        print("no existe una tarea asignada con ese id")
        return

    print("tarea encontrada")
    eliminar=confirmar_eliminacion("esta seguror de que desea eliminar esta tarea? tenga en cuenta que esta opcion es irreversible(y/n): ")
    if eliminar == "y":
        almacenador_tareas.remove(pedir_id)
        guardar_tarea()
        print("tarea eliminada con exito")
    else:
        print("opcion de eliminar cancelada")


   
    
    


