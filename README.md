# Gestor de tareas

Aplicación de consola en Python para registrar y administrar tareas. Permite crear, consultar, actualizar y eliminar tareas, y conserva la información en un archivo JSON para recuperarla al volver a iniciar el programa.

## Características

- Crear tareas con ID, título, descripción, estado y prioridad.
- Validar que los ID sean números positivos y no estén repetidos.
- Consultar una tarea por su ID o listar todas las tareas registradas.
- Actualizar el título, descripción, estado o prioridad de una tarea.
- Eliminar tareas con confirmación previa.
- Guardar los cambios en `tareas.json` y cargarlos automáticamente al iniciar.

## Tecnologías

- Python 3
- Biblioteca estándar: `json` y `os`

No requiere instalar dependencias externas.

## Cómo ejecutar el proyecto

1. Abre una terminal en esta carpeta:

   ```powershell
   cd Gestor_de_tareas
   ```

2. Ejecuta el menú principal:

   ```powershell
   python menu.py
   ```

3. Selecciona una opción del 1 al 6 y sigue las instrucciones que aparecen en pantalla.

## Estados y prioridades permitidos

| Campo | Valores disponibles |
| --- | --- |
| Estado | `pendiente`, `en progreso`, `completada` |
| Prioridad | `baja`, `media`, `alta` |

## Estructura del proyecto

```text
Gestor_de_tareas/
├── menu.py                 # Punto de entrada y menú interactivo
├── logica_principal.py     # Validaciones y operaciones CRUD
├── Tarea_principal.py      # Clase Tarea
├── tareas.json             # Datos persistentes de las tareas
└── README.md
```

## Ejemplo de una tarea almacenada

```json
{
  "id": 1,
  "titulo": "Estudiar para el examen",
  "descripcion": "estudiar para el examen de matematicas",
  "estado": "en progreso",
  "prioridad": "alta"
}
```
## Autoría
Proyecto desarrollado en Python utilizando programación orientada a objetos, validación de datos, operaciones CRUD y persistencia de información mediante archivos JSON.

Paula Machacon
