from paquete.validacion.validaciones import *
from paquete.tabla.tablas import *


def cargar_tabla_secuencial(tabla: dict) -> list:
    """Carga la tabla secuencialmente con datos.

    Args:
        tabla (dict): tabla de datos.

    Returns:
        list: retorna una matriz
    """
    total_filas = len(tabla['matriz'])
    
    if total_filas != 0:

        cargar = obtener_respuesta(
                            "¿Quiere cargar una fila de datos? (s/n): ",
                            "Error, ingresar solo 's' o 'n'",
                            "s", "n")
        
        f = 0 

        while cargar == "s" and f < total_filas:
            print(f"---Cargando datos fila {f + 1}---")
            
            nueva_fila = cargar_fila(tabla)
            
            if len(nueva_fila) > 0:
                tabla['matriz'][f] = nueva_fila
                f += 1 
            
            if f < total_filas:
                cargar = obtener_respuesta(
                                "¿Quiere cargar otra fila de datos? (s/n): ",
                                "Error, ingresar solo 's' o 'n'",
                                "s", "n")
            else:
                print("Se completaron las filas disponibles en la tabla")
    else:
        print("La tabla no tiene filas predefinidas para cargar.")

    return tabla


def modificar_celda_individual(tabla: dict, fila: int, columna: int) -> None:
    """Modifica una celda especifica de la tabla.

    Args:
        tabla (dict): tabla de datos
        fila (int): numero de fila
        columna (int): numero de columna
    """
    print(f"Dato actual en Fila {fila + 1}", 
            "Columna '{tabla['columnas'][columna]}':"
            "{tabla['matriz'][fila][columna]}")
    
    modificar = obtener_respuesta(
                        "¿Quiere modificar este dato específico? (si/no): ",
                        "Error, ingrese 'si' o 'no'", "si", "no")
    if modificar == "si":
        nuevo_dato = input("Ingrese nuevo dato: ")
        tabla['matriz'][fila][columna] = transformar_dato(nuevo_dato)


def modificar_fila(tabla: dict) -> None: 
    """Modifica los datos de una fila especifica.

    Args:
        tabla (dict): tabla de datos.
    """
    for i in range(len(tabla['matriz'])):
        print(f"\nDatos de la fila número {i + 1}: {tabla['matriz'][i]}")
        modificar = obtener_respuesta(
                            "¿Quiere modificar esta fila? (si/no): ",
                            "Error, ingrese 'si' o 'no'", "si", "no")
        if modificar == "si":
            for j in range(len(tabla['columnas'])):
                modificar_celda_individual(tabla, i, j)


def modificar_columna(tabla: dict) -> None:
    """Modifica los datos de una columna especifica.

    Args:
        tabla (dict): tabla de datos.
    """
    for i in range(len(tabla['columnas'])):
        print(f"\nDatos de la columna '{tabla['columnas'][i]}':")
        #mostrar_columna(tabla, tabla['columnas'][i]) 
        
        modificar = obtener_respuesta(
                            "¿Quiere modificar esta columna? (si/no): ",
                            "Error, ingrese 'si' o 'no'", "si", "no")
        if modificar == "si":
            for j in range(len(tabla['matriz'])):
                modificar_celda_individual(tabla, j, i)


def modificar_variable_especifica(tabla: dict, 
                                  fila: int, 
                                  columna: int) -> None:
    """Sobreescribe una variable especifica.

    Args:
        tabla (dict): tabla de datos.
        fila (int): numero de fila
        columna (int): numero de columna
    """
    celda = tabla['columnas'][columna]
    nuevo_valor = input(f"Ingrese nuevo valor para '{celda}': ")
    tabla['matriz'][fila][columna] = transformar_dato(nuevo_valor)


def eliminar_variable(tabla: dict, fila: int, columna: int) -> None:
    """Elimina una variable sobreescribiendola con un "".

    Args:
        tabla (dict): tabla de datos.
        fila (int): numero de fila
        columna (int): numero de columna
    """
    tabla['matriz'][fila][columna] = ""


def elegir_modificacion_de_variable(tabla: dict, 
                                    fila: int, 
                                    columna: int) -> None:
    """Menu de opciones para modificar una variable.

    Args:
        tabla (dict): tabla de datos.
        fila (int): numero de fila
        columna (int): numero de columna
    """
    print("\n1. Eliminar variable (vaciar celda)")
    print("2. Modificar variable (cambiar valor)")

    opcion_modificacion = get_int(
                    "Elija una de las opciones: ",
                    "Error, ingrese un entero válido (1 o 2)",
                    1, 2)
    
    match opcion_modificacion:
        case 1:
            eliminar_variable(tabla, fila, columna)
            print("¡Variable vaciada!")
        case 2:
            modificar_variable_especifica(tabla, fila, columna)
            print("¡Variable modificada!")


def modificar_variables(nombre_proyecto: str, 
                        proyectos: dict) -> None:
    """Menu de opciones para modificar variables.

    Args:
        nombre_proyecto (str): nombre del proyecto actual.
        proyectos (dict): diccionario actual.
    """

    nom_tabla = limpiar_texto(input("Tabla a analizar: "))
    if nom_tabla in proyectos[nombre_proyecto]:
        tabla = proyectos[nombre_proyecto][nom_tabla]

        print("1-Cargar tabla secuencial")
        print("2-Modificar fila completa")
        print("3-Modificar columna completa")
        print("4-Modificar una variable/celda específica")
        print("5-Salir de modificar variables")

        opcion = get_int("Ingresar una opcion numerica: ", 
                        "Error, Intente otra vez", 
                        1, 5)

        while opcion != 5:
            match opcion:
                case 1:
                    cargar_tabla_secuencial(tabla)
                case 2:
                    modificar_fila(tabla)
                case 3:
                    modificar_columna(tabla)
                case 4:
                    if len(tabla['matriz']) != 0:
                        fila = verificar_filas(tabla) 
                        col_nombre = retornar_columna(tabla) 
                        col = obtener_indice_columna(tabla, col_nombre)
                        
                        elegir_modificacion_de_variable(tabla, fila, col)
                    else:
                        print("La tabla no tiene filas de datos.")
                        
            print("1-Cargar tabla secuencial")
            print("2-Modificar fila completa")
            print("3-Modificar columna completa")
            print("4-Modificar una variable/celda específica")
            print("5-Salir de modificar variables")

            opcion = get_int("Ingresar una opcion numerica: ", 
                            "Error, Intente otra vez", 
                            1, 5)
    else:
        print("No existe tabla con ese nombre!")
            