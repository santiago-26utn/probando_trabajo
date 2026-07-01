from paquete.validacion.validaciones import *



def elegir_tipo_dato() -> str:        
    ""  


    print("1-Dato tipo texto")
    print("2-Dato tipo numerico")

    opcion = get_int("Ingrese una de las opciones: ",
                     "Error, ingrese una opcion numerica ",
                     1,2)
    
    if opcion == 1:
        tipo_dato = "texto"
    elif opcion == 2:
        tipo_dato = "numerico"

    return tipo_dato

#esto va en variables!
def agregar_dato(tipo_dato: str) -> any:
    ""
    if tipo_dato == "texto":
        dato = input("Agregar dato: ")      #hacer un transformar dato
    elif tipo_dato == "vacio":
        dato = " "
    elif tipo_dato == "numerico":
        dato = get_int_simple("Ingresar número entero positivo", 
                              "Error, Ingrese número entero positivo") 

    return dato

#esto no se si va en variables o modificar tabla o crear tabla
def cargar_fila(tabla: dict) -> list:
    ""
    fila = []

    if len(tabla['columnas']) == 0:
        print("Lista vacia, ingresara nombres de columnas")
        cantidad_columnas = get_int("Ingrese la cantidad de columnas que desee: ",
                                    "Error, ingrese entero mayor a 0",
                                    1, 100)
        for i in range(cantidad_columnas):
            dato = agregar_dato("texto")
            dato = transformar_dato(dato)
            tabla['columnas'].append(dato) 
    else:
        for i in range(len(tabla['columnas'])):
            print(f"Columna [{tabla['columnas'][i]}] (Tipo esperado: {tabla['tipos'][i]})")
            dato = agregar_dato(tabla['tipos'][i])
            fila.append(dato)

    return fila





def crear_tabla(columnas: int, filas: int) -> list:
    ""
    matriz_tabla = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila += [None]
        matriz_tabla += [fila]

    return matriz_tabla





def agregar_fila(tabla: dict) -> None:
    """Modificado: Revisa la longitud de 'columnas' y añade a 'filas'."""
    nueva_fila = []
    for i in range(len(tabla['columnas'])):
        nueva_fila.append(None)
    
    tabla['matriz'].append(nueva_fila)
    

def agregar_columna(tabla: dict) -> None:
    """Modificado: Añade la columna y registra su tipo correspondiente."""
    nombre_columna = input("Ingrese nombre para nueva columna: ")
    tabla['columnas'].append(nombre_columna)
    
    # Registramos qué tipo de datos va a aceptar esta nueva columna
    print(f"Defina el tipo de datos para la nueva columna '{nombre_columna}':")
    tipo_nueva_col = elegir_tipo_dato()
    tabla['tipos'].append(tipo_nueva_col)

    for i in range(len(tabla['matriz'])):
        tabla['matriz'][i].append(None)
            

def eliminar_fila(tabla: dict) -> None:
    """Modificado: Remueve una fila interna de la lista tabla['matriz']."""

    fila = int(input("Ingrese número de fila a eliminar: "))

    # ANTES: tabla.remove(tabla[fila])

    if 0 <= fila < len(tabla['matriz']):

        tabla['matriz'].pop(fila)

    else:

        print("Índice de fila inválido.")


def eliminar_columna(tabla: dict) -> None:
    """Modificado: Elimina la columna de los metadatos, de los tipos y de la matriz."""
    nombre_columna = input("Ingrese nombre para eliminar columna: ")
    
    indice_columna = obtener_indice_columna(tabla, nombre_columna)

    if indice_columna != -1:
        tabla['columnas'].pop(indice_columna)
        tabla['tipos'].pop(indice_columna) # CORREGIDO: Mantiene la paridad eliminando el tipo
        for fila in tabla['matriz']:
            fila.pop(indice_columna)
    else:
        print("La columna no existe.")





#d.1-mostrar tabla completa
def mostrar_tabla_completa(tabla: dict) -> None:
    """Modificado: Imprime por separado la cabecera ('columnas') y el cuerpo ('matriz')."""
    # 1. Imprimir títulos de columnas
    print("|", end="")
    for col in tabla['columnas']:
        print(f" {col:^10} |", end="")
    print()
    print("-" * (13 * len(tabla['columnas'])))          #ver cual queda mejor, esta funcion o la de santi
    
    # 2. Imprimir las filas de datos
    for fila in tabla['matriz']:
        print("|", end="")
        for dato in fila:
            print(f" {dato:^10} |", end="")
        print()

#d.2-mostrar tabla por columna/columnas


def obtener_indice_columna(tabla: dict, nombre_columna: str) -> int:
    """Retorna el índice de la columna dentro del dict. Si no existe, devuelve -1."""
    indice = -1
    for i in range(len(tabla['columnas'])):
        if tabla['columnas'][i] == nombre_columna:
            indice = i
    return indice



def obtener_columna_por_indice(tabla: dict, numero_columna: int) -> list:   
    """Modificado: Recorre las filas puras guardando el valor de la columna."""
    lista_columna = []
    # ANTES: recorría toda la 'tabla' trayendo también el nombre de la columna. 
    # Si preferís mantener el nombre como primer elemento, agregás tabla['columnas'][numero_columna] primero.
    for i in range(len(tabla['matriz'])):
        lista_columna.append(tabla['matriz'][i][numero_columna])
    return lista_columna

def obtener_columna_por_nombre(tabla: dict, columna: str) -> list:   
    """Modificado: Revisa las claves correspondientes."""
    lista_columna = []
    for i in range(len(tabla['columnas'])):
        if tabla['columnas'][i] == columna:
            lista_columna = obtener_columna_por_indice(tabla, i)
    return lista_columna

def mostrar_columna(tabla: dict, columna_elegida: str):
    """Modificado: Busca en la lista de metadatos 'columnas'."""
    total_columnas = len(tabla['columnas']) 
    posicion_columna = 0
    columna_encontrada = False
    
    while total_columnas > posicion_columna and columna_encontrada == False:
        if tabla['columnas'][posicion_columna] == columna_elegida: 
            columna_encontrada = True
        posicion_columna += 1

    if columna_encontrada == False:
        print("El dato ingresado no es un titulo de columna")
    return columna_encontrada


def verificar_columnas(tabla: dict, columna_elegida: str) -> bool:
    """Modificado: Busca en la lista de metadatos 'columnas'."""
    total_columnas = len(tabla['columnas'])
    posicion_columna = 0
    columna_encontrada = False

    while total_columnas > posicion_columna and not columna_encontrada:
        if tabla['columnas'][posicion_columna] == columna_elegida:
            columna_encontrada = True
        posicion_columna += 1

    if not columna_encontrada:
        print("El dato ingresado no es un titulo de columna")

    return columna_encontrada



def retornar_columna(tabla: list) -> str:   
    ""
    columna = input("Elija columna: ")
    columna_existente = verificar_columnas(tabla, columna)

    while not columna_existente:
        columna = input("Elija columna: ")
        columna_existente = verificar_columnas(tabla, columna)

    return columna

def seleccionar_columnas_tabla(tabla: dict) -> list:
    """Modificado: Ahora extrae las columnas seleccionadas como sublistas puras."""
    cargar = obtener_respuesta("Quiere seleccionar una columna de datos?(si/no): ", 
                               "Error, solo ingresar 'si' o 'no'", 
                               "si", "no")
    lista_seleccionadas = [] 

    while cargar == "si":
        columna = retornar_columna(tabla)
        # Guardamos la columna obtenida de la tabla
        lista_seleccionadas.append(obtener_columna_por_nombre(tabla, columna))

        cargar = obtener_respuesta("Quiere seleccionar otra columna?(s/n): ",
                                   "Error, ingrese 'si' o 'no'", 
                                   "si", "no")

    return lista_seleccionadas

def mostrar_columnas_seleccionadas(tabla: dict) -> None:
    """Modificado: Muestra las columnas elegidas alineadas horizontalmente."""
    columnas = seleccionar_columnas_tabla(tabla)
    
    # Si el usuario no eligió ninguna columna, evitamos que rompa
    if len(columnas) == 0:
        print("No se seleccionó ninguna columna.")
        return
        
    cantidad_filas = len(columnas[0])

    print("\n--- COLUMNAS SELECCIONADAS ---")
    for fila in range(cantidad_filas):
        for columna in range(len(columnas)):
            print(f"{str(columnas[columna][fila]):<15}", end="")
        print()
    print()


#d.3-mostrar fila
def verificar_filas(tabla: dict) -> int:
    """Modificado: El rango válido ahora va desde 0 hasta la cantidad de 'filas' - 1."""
    fila = get_int_simple("Elija una fila (por índice numérico): ", "Error, Ingrese número entero positivo")

    total_filas = len(tabla['matriz']) - 1
    
    if total_filas < 0:
        print("La tabla no contiene filas de datos actualmente.")
        return -1

    fila_existente = validar_rango(fila, 0, total_filas)

    while fila_existente == False:
        print("No existe ese número de fila")
        fila = get_int_simple("Elija una fila: ", "Error, Ingrese número entero positivo")
        fila_existente = validar_rango(fila, 0, total_filas)

    return fila


def obtener_fila_tabla(tabla: dict) -> int:
    """
    Modificado: Corregido el error de tu código base. 
    Esta función debe retornar el ÍNDICE validado de la fila elegida.
    """
    fila_idx = verificar_filas(tabla)
    return fila_idx


def mostrar_fila_tabla0(tabla: list) -> None:
    ""

    fila = obtener_fila_tabla(tabla)

    for dato in tabla[fila]:
        print(f"{dato:<15}", end="")
    print()

###################

def mostrar_fila_tabla(tabla: dict) -> None:
    """Modificado: Corrige la lógica para mostrar los títulos y la fila seleccionada."""
    fila_idx = verificar_filas(tabla)
    
    # Imprimir columnas primero para referencia limpia
    for col in tabla['columnas']:
        print(f"{col:<15}", end="")
    print("\n" + "-" * (15 * len(tabla['columnas'])))
    
    # Imprimir los datos de la fila elegida
    for dato in tabla['matriz'][fila_idx]:
        print(f"{dato:<15}", end="")
    print()


def filtrar_columnas(tabla: dict) -> None:
    """Modificado: Filtra directo sobre la clave 'matriz' manteniendo el diseño visual."""
    columna = retornar_columna(tabla)
    valor_buscado = input("Ingrese el valor a filtrar: ")
    indice_columna = obtener_indice_columna(tabla, columna)

    # 1. Imprimir títulos de columnas (Formato idéntico a mostrar_tabla_completa)
    print("|", end="")
    for col in tabla['columnas']:
        print(f" {col:^10} |", end="")
    print()
    print("-" * (13 * len(tabla['columnas'])))

    # 2. Filtrar e imprimir las filas que coincidan usando el mismo formato de celdas
    for fila in range(len(tabla['matriz'])):
        if str(tabla['matriz'][fila][indice_columna]) == valor_buscado:
            print("|", end="")
            for dato in tabla['matriz'][fila]:
                # Usamos el mismo formateo centrado ':^10' para mantener la alineación de la tabla
                print(f" {str(dato):^10} |", end="")
            print()


################
#d.4 filtrar_columnas
def obtener_indice_columna0(tabla: list, columna: str) -> int:
    ""
    indice = -1

    for i in range(len(tabla[0])):
        if tabla[0][i] == columna:
            indice = i

    return indice

def filtrar_columnas0(tabla: list) -> None:
    ""
    columna = retornar_columna(tabla)

    valor_buscado = input("Ingrese el valor a filtrar: ")

    indice_columna = obtener_indice_columna(tabla, columna)

    mostrar_tabla_completa([tabla[0]])

    for fila in range(1, len(tabla)):
        if str(tabla[fila][indice_columna]) == valor_buscado:

                for dato in tabla[fila]:
                    print(f"{dato:<15}", end="")

                print()





def crear_o_modificar_tabla(nombre_proyecto: str, proyectos: dict) -> dict:    

    if nombre_proyecto not in proyectos: 
        proyectos[nombre_proyecto] = {}

    print("1-Crear tabla")
    print("2-Modificar tabla")
    print("3-Guardar tabla")
    print("4-Salir de crear tabla")

    opcion = get_int("Ingresar una opcion numerica: ", 
                     "Error, Intente otra vez", 
                     1, 4)

    while opcion != 4:
        if opcion == 1:
            nom_tabla = limpiar_texto(input("Nombre tabla: "))
        
            if nom_tabla in proyectos[nombre_proyecto]:
                print("La tabla ya existe en este proyecto.")
            else:
                cant_cols = leer_entero_validado("Ingrese cantidad Columnas: ")

                tabla_tipos = []
                columnas = []
                for i in range(cant_cols):
                    col = limpiar_texto(input("Nombre Columna " + str(i + 1) + ": "))
                    columnas.append(col)
                    print(f"Para la columna '{col}':")
                    tip = elegir_tipo_dato()
                    tabla_tipos.append(tip)
                    
                cant_f = leer_entero_validado("Ingrese cantidad Filas: ")
                
                matriz = []
                for f in range(cant_f):
                    fila = []
                    for c in range(len(columnas)):
                        valor_celda = None            
                        fila.append(valor_celda)
                    matriz.append(fila)
                    
                proyectos[nombre_proyecto][nom_tabla] = {
                    'columnas': columnas, 
                    'tipos': tabla_tipos, 
                    'matriz': matriz
                }
                print("¡Tabla Creada!")

        elif opcion == 2:
            nom_tabla = limpiar_texto(input("Ingrese el nombre de la tabla a modificar: "))
            
            if nom_tabla in proyectos[nombre_proyecto]:
                tabla_elegida = proyectos[nombre_proyecto][nom_tabla]
                
                if len(tabla_elegida['columnas']) != 0:
                    modificar_tabla(tabla_elegida)
                else:
                    print("Error, tabla vacia")
            else:
                print("La tabla especificada no existe en este proyecto.")
        
        elif opcion == 3:
            archivo_csv = open("probando_trabajo/paquete/archivos/tablas.csv", "w")

            # Recorremos todas las tablas que pertenezcan a el proyecto
            for nom_tabla in proyectos[nombre_proyecto]:
                tabla_actual = proyectos[nombre_proyecto][nom_tabla]
                
                # Escribimos los encabezados de la tabla
                linea_columnas = ""
                for i in range(len(tabla_actual['columnas'])):
                    linea_columnas = linea_columnas + str(tabla_actual['columnas'][i])
                    if i < len(tabla_actual['columnas']) - 1:
                        linea_columnas = linea_columnas + ","
                
                linea_columnas = linea_columnas + "\n"
                archivo_csv.write(linea_columnas)

                # Escribimos el tipo de datos de la tabla:
                linea_tipos = ""
                for t in range(len(tabla_actual['tipos'])):
                    linea_tipos = linea_tipos + str(tabla_actual['tipos'][t])
                    if t < len(tabla_actual['tipos']) - 1:
                        linea_tipos = linea_tipos + ","
                
                linea_tipos = linea_tipos + "\n"
                archivo_csv.write(linea_tipos)

                # Escribimos las filas de la matriz 
                for f in range(len(tabla_actual['matriz'])):
                    linea_fila = ""
                    for c in range(len(tabla_actual['matriz'][f])):
                        linea_fila = linea_fila + str(tabla_actual['matriz'][f][c])
                        if c < len(tabla_actual['matriz'][f]) - 1:
                            linea_fila = linea_fila + ","
                    
                    linea_fila = linea_fila + "\n"
                    archivo_csv.write(linea_fila)

            archivo_csv.close()
            print("¡Todas las tablas del proyecto fueron guardadas en archivos/tablas.csv!")
                
        print("\n1-Crear tabla\n2-Modificar tabla\n3-Guardar tabla\n4-Salir")

        opcion = get_int("Ingresar una opcion numerica: ", 
                         "Error, Intente otra vez", 1, 4)
    
    return proyectos


def modificar_tabla(tabla: list):
    print("1-Agregar fila")
    print("2-Eliminar fila")
    print("3-Agregar columna")
    print("4-Eliminar columna")
    print("5-Salir de modificar tabla")

    opcion = get_int("Ingresar una opcion numerica: ", 
                     "Error, Intente otra vez", 
                     1, 5)

    while opcion != 5:
        if opcion == 1:
            agregar_fila(tabla)
        elif opcion == 2:
            seguro = obtener_respuesta("Seguro quieres eliminar una fila(si/no)?",
                                       "Error, ingrese 'si' o 'no'", "si", "no")
            if seguro == "si":
                eliminar_fila(tabla)
        elif opcion == 3:
            agregar_columna(tabla)
        elif opcion == 4:
            seguro = obtener_respuesta("Seguro quieres eliminar una columna(si/no)?",
                                       "Error, ingrese 'si' o 'no'", "si", "no")
            if seguro == "si":
                eliminar_columna(tabla)     #problema, no acepta titulos de columna
                
        print("\n1-Agregar fila\n2-Eliminar fila\n3-Agregar columna\n4-Eliminar columna\n5-Salir")
        opcion = get_int("Ingresar una opcion numerica: ", "Error, Intente otra vez", 1, 5)


def mostrar_tabla(nombre_proyecto: str, proyectos: dict) -> None:
    """Modificado: Controla el submenú de visualización leyendo las propiedades del dict."""
    
    nom_tabla = limpiar_texto(input("Tabla a analizar: "))
    if nom_tabla in proyectos[nombre_proyecto]:
        tabla = proyectos[nombre_proyecto][nom_tabla]

    if len(tabla['columnas']) != 0: 
        print("1-Mostrar tabla completa")
        print("2-Mostrar fila")
        print("3-Seleccionar columnas")
        print("4-Filtrar")
        print("5-Salir de mostrar tabla")

        opcion = get_int("Ingresar una opcion numerica: ", 
                         "Error, Intente otra vez", 
                         1, 5)

        while opcion != 5:
            if opcion == 1:
                mostrar_tabla_completa(tabla)
            elif opcion == 2:
                mostrar_fila_tabla(tabla)
            elif opcion == 3:
                mostrar_columnas_seleccionadas(tabla)
            elif opcion == 4:
                filtrar_columnas(tabla)
            
            print("1-Mostrar tabla completa")
            print("2-Mostrar fila")
            print("3-Seleccionar columnas")
            print("4-Filtrar")
            print("5-Salir de mostrar tabla")

            opcion = get_int("Ingresar una opcion numerica: ", 
                            "Error, Intente otra vez", 
                            1, 5)
    else:
        print("¡Tabla vacía!")