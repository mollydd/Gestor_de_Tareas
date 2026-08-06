import logica_principal
logica_principal.cargar_tareas()
opcion = 0

while opcion != 6:
    print("===== GESTOR DE TAREAS =====")
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Buscar tarea")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

    opcion = logica_principal.pedir_opcion("Ingrese una opción: ")

    if opcion == 1:
        logica_principal.agregar_tarea()
        logica_principal.guardar_tarea()
    elif opcion == 2:
        logica_principal.mostrar_tareas()
    elif opcion == 3:
        logica_principal.buscar_tarea()
    elif opcion == 4:
        logica_principal.actualizar_tarea()
    elif opcion == 5:
        logica_principal.eliminar_tarea()
    elif opcion == 6:
        print("--------- Saliendo del programa, ¡hasta luego! ---------")
 