from paquete.validacion.validaciones import *



def elegir_tipo_dato() -> str:        
    """Permite elegir el tipo de dato que tendra una columna.

    Returns:
        str: retorna un texto.
    """

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


def agregar_dato(tipo_dato: str) -> int | str:
    """Permite ingresar un texto según el tipo de dato.

    Args:
        tipo_dato (str): indica el tipo de dato

    Returns:
        int | str: Retorna un texto o un int
    """
    if tipo_dato == "texto":
        dato = get_length("Ingrese un dato tipo texto: ",
                          "Error, no numeros ni caracteres especiales",
                          1, 16)
        dato = transformar_dato(dato)    
    elif tipo_dato == "numerico":
        dato = get_float("Ingresar número entero positivo: ", 
                         "Error, Ingrese número entero positivo: ",
                         0, 100000) 

    return dato

def cargar_fila(tabla: dict) -> list:
    """Carga una fila con datos.

    Args:
        tabla (dict): tabla con datos.

    Returns:
        list: retorna una lista con los datos para la fila.
    """
    fila = []

    if len(tabla['columnas']) == 0:
        print("Lista vacia, ingresara nombres de columnas")
        cantidad_columnas = get_int(
                        "Ingrese la cantidad de columnas que desee: ",
                        "Error, ingrese entero mayor a 0",
                        1, 100)
        for i in range(cantidad_columnas):
            dato = agregar_dato("texto")
            dato = transformar_dato(dato)
            tabla['columnas'].append(dato) 
    else:
        for i in range(len(tabla['columnas'])):
            print(f"Columna [{tabla['columnas'][i]}]") 
            print(f"Tipo esperado de dato: {tabla['tipos'][i]}")    
            dato = agregar_dato(tabla['tipos'][i])
            fila.append(dato)

    return fila





def crear_tabla(columnas: int, filas: int) -> list:
    """Crea una tabla con cierta cantidad de columnas y filas.

    Args:
        columnas (int): cantidad de columnas.
        filas (int): cantidad de filas.

    Returns:
        list: retorna la tabla creada
    """
    matriz_tabla = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila += ""
        matriz_tabla += [fila]

    return matriz_tabla





def agregar_fila(tabla: dict) -> None:
    """Permite agregar una fila a la tabla.

    Args:
        tabla (dict): tabla de datos.
    """
    nueva_fila = []
    for i in range(len(tabla['columnas'])):
        nueva_fila.append(" ")
    
    tabla['matriz'].append(nueva_fila)
    print("---Se agrego una nueva fila---")
    
    

def agregar_columna(tabla: dict) -> None:
    """Permite agregar una columna con nombre a la tabla.

    Args:
        tabla (dict): tabla de datos.
    """
    nombre_columna = input("Ingrese nombre para nueva columna: ")
    nombre_columna = transformar_dato(nombre_columna)
    tabla['columnas'].append(nombre_columna)
    
    print(f"Defina tipo de datos para la nueva columna '{nombre_columna}':")
    tipo_nueva_col = elegir_tipo_dato()
    tabla['tipos'].append(tipo_nueva_col)

    for i in range(len(tabla['matriz'])):
        tabla['matriz'][i].append("")
    
    print("---Se agrego una nueva columna---")
            

def eliminar_fila(tabla: dict) -> None:
    """Elimina una fila de la tabla.

    Args:
        tabla (dict): tabla de datos.
    """


    fila = get_int_simple("Ingrese número de fila a eliminar: ",
                          "Error, no es entero o no es numero")
    fila -= 1

    if 0 < fila < len(tabla['matriz']):

        tabla['matriz'].pop(fila)
        print("---Se elimino la fila---")

    else:
        print("Índice de fila inválido.")
    


def eliminar_columna(tabla: dict) -> None:
    """Elimina una columna, junto a sus datos y tipo de datos.

    Args:
        tabla (dict): tabla de datos.
    """
    nombre_columna = input("Ingrese nombre para eliminar columna: ")
    
    indice_columna = obtener_indice_columna(tabla, nombre_columna)

    if indice_columna != -1:
        tabla['columnas'].pop(indice_columna)
        tabla['tipos'].pop(indice_columna) 
        for fila in tabla['matriz']:
            fila.pop(indice_columna)
            
        print("---Se elimino la columna---")
    else:
        print("La columna no existe.")





#d.1-mostrar tabla completa
def mostrar_tabla_completa(tabla: dict) -> None:
    """Muestra la tabla completa.

    Args:
        tabla (dict): tabla de datos.
    """
    print("|", end="")
    for col in tabla['columnas']:
        print(f" {col:^10} |", end="")
    print()
    print("-" * (13 * len(tabla['columnas'])))         
    
    for fila in tabla['matriz']:
        print("|", end="")
        for dato in fila:
            print(f" {dato:^10} |", end="")
        print()



def obtener_indice_columna(tabla: dict, nombre_columna: str) -> int:
    """Permite obtener el indice de la columna buscandola por el nombre.

    Args:
        tabla (dict): tabla de datos.
        nombre_columna (str): nombre de la columna

    Returns:
        int: retorna el indice de la columna o -1 si no existe.
    """
    indice = -1
    for i in range(len(tabla['columnas'])):
        if tabla['columnas'][i] == nombre_columna:
            indice = i
    return indice


def obtener_columna_por_indice(tabla: dict, numero_columna: int) -> list:   
    """Permite obtener la columna a través de su indice.

    Args:
        tabla (dict): tabla de datos.
        numero_columna (int): numero de columna.

    Returns:
        list: retorna una lista con los datos de la columna encontrada.
    """
    lista_columna = []
    for i in range(len(tabla['matriz'])):
        lista_columna.append(tabla['matriz'][i][numero_columna])
    return lista_columna


def obtener_columna_por_nombre(tabla: dict, columna: str) -> list:   
    """Obtiene una columna por su nombre.

    Args:
        tabla (dict): tabla de datos.
        columna (str): nombre de columna.

    Returns:
        list: retorna una lista de los datos de la columna.
    """
    lista_columna = []
    for i in range(len(tabla['columnas'])):
        if tabla['columnas'][i] == columna:
            lista_columna = obtener_columna_por_indice(tabla, i)
    return lista_columna


def mostrar_columna(tabla: dict, columna_elegida: str) -> bool:
    """Verifica si existe la columna.

    Args:
        tabla (dict): tabla de datos.
        columna_elegida (str): nombre de columna elegida.

    Returns:
        bool: retorna True si existe la columna, False caso contrario.
    """
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
    """Verifica si existe la columna.

    Args:
        tabla (dict): tabla de datos.
        columna_elegida (str): nombre de columna elegida.

    Returns:
        bool: retorna True si existe la columna, False caso contrario.
    """
    
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
    """Pide repetidamente el nombre de una columna existente.

    Args:
        tabla (list): tabla de datos.

    Returns:
        str: retorna el nombre de una columna.
    """
    columna = input("Elija columna: ")
    columna = transformar_dato(columna)
    columna_existente = verificar_columnas(tabla, columna)

    while not columna_existente:
        columna = input("Elija columna: ")
        columna_existente = verificar_columnas(tabla, columna)

    return columna


def seleccionar_columnas_tabla(tabla: dict) -> list:
    """Hace una lista de columnas seleccionadas de la tabla 
        junto a sus nombres.

    Args:
        tabla (dict): tabla de datos.

    Returns:
        list: retorna una lista con los nombres de las columnas elegidas.
    """
    cargar = obtener_respuesta(
                "Quiere seleccionar una columna de datos?(s/n): ",
                "Error, solo ingresar 's' o 'n'", 
                "s", "n")
    nombres_columnas = []
    lista_seleccionadas = [] 

    while cargar == "s":
        columna = retornar_columna(tabla)
        nombres_columnas.append(columna)

        lista_seleccionadas.append(obtener_columna_por_nombre(tabla, 
                                                              columna))

        cargar = obtener_respuesta("Quiere seleccionar otra columna?(s/n): ",
                                   "Error, ingrese 's' o 'n'", 
                                   "s", "n")

    return nombres_columnas, lista_seleccionadas


def mostrar_columnas_seleccionadas(tabla: dict) -> None:
    """Muestra el contenido de las columnas seleccionadas.

    Args:
        tabla (dict): tabla de datos.
    """
    titulos, columnas = seleccionar_columnas_tabla(tabla)
    
    if len(columnas) != 0:
        
        cantidad_filas = len(columnas[0])

        print("|", end="")
        for i in range(len(titulos)):
            print(f" {titulos[i]:^12} |", end="")
        print()
        
        print("-" * (16 * len(columnas)))

        for fila in range(cantidad_filas):
            print("| ", end="")
            for columna in range(len(columnas)):
                print(f"{str(columnas[columna][fila]):^12} | ", end="")
            print()
            
        print("-" * (16 * len(columnas)))
        print()

    else:
        print("No se seleccionó ninguna columna.")


def verificar_filas(tabla: dict) -> int:
    """Pide repetidamente un numero de fila hasta que se
        le pase un numero de fila existente.

    Args:
        tabla (dict): tabla de datos.

    Returns:
        int: retorna el número de fila existente ingresado.
    """
    fila = get_int_simple("Elija un numero de fila: ", 
                          "Error, Ingrese número entero positivo")
    
    fila -= 1

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


def mostrar_fila_tabla(tabla: dict) -> None:
    """Muestra una fila especifica de la tabla.

    Args:
        tabla (dict): tabla de datos.
    """
    fila = verificar_filas(tabla)
    
    for col in tabla['columnas']:
        print(f"{col:<15}", end="")
    print("\n" + "-" * (15 * len(tabla['columnas'])))
    
    for dato in tabla['matriz'][fila]:
        print(f"{dato:<15}", end="")
    print()


def filtrar_columnas(tabla: dict) -> None:
    """Filtra datos a través de columnas.

    Args:
        tabla (dict): tabla de datos.
    """
    columna = retornar_columna(tabla)
    valor_buscado = input("Ingrese el valor a filtrar: ")
    indice_columna = obtener_indice_columna(tabla, columna)

    print("|", end="")
    for col in tabla['columnas']:
        print(f" {col:^10} |", end="")
    print()
    print("-" * (13 * len(tabla['columnas'])))

    for fila in range(len(tabla['matriz'])):
        if str(tabla['matriz'][fila][indice_columna]) == valor_buscado:
            print("|", end="")
            for dato in tabla['matriz'][fila]:
                print(f" {str(dato):^10} |", end="")
            print()

def guardar_tabla(nombre_proyecto: str, proyectos: dict) -> None:
    """Guarda la tabla en un archivo csv.

    Args:
        nombre_proyecto (str): nombre del proyecto actual.
        proyectos (dict): diccionario actual.
    """
    for nom_tabla in proyectos[nombre_proyecto]:
        tabla_actual = proyectos[nombre_proyecto][nom_tabla]

        archivo_csv = open("paquete/archivos/tablas.csv", "a")
        archivo_csv.write(f"Tabla: {nom_tabla}\n")

        linea_columnas = ""
        for i in range(len(tabla_actual['columnas'])):
            linea_columnas = linea_columnas + str(tabla_actual['columnas'][i])
            if i < len(tabla_actual['columnas']) - 1:
                linea_columnas = linea_columnas + ","
        
        linea_columnas = linea_columnas + "\n"
        archivo_csv.write(linea_columnas)

        linea_tipos = ""
        for t in range(len(tabla_actual['tipos'])):
            linea_tipos = linea_tipos + str(tabla_actual['tipos'][t])
            if t < len(tabla_actual['tipos']) - 1:
                linea_tipos = linea_tipos + ","
        
        linea_tipos = linea_tipos + "\n"
        archivo_csv.write(linea_tipos)

        for f in range(len(tabla_actual['matriz'])):
            linea_fila = ""
            for c in range(len(tabla_actual['matriz'][f])):
                linea_fila = linea_fila + str(tabla_actual['matriz'][f][c])
                if c < len(tabla_actual['matriz'][f]) - 1:
                    linea_fila = linea_fila + ","
            
            linea_fila = linea_fila + "\n"
            archivo_csv.write(linea_fila)

    archivo_csv.close()
    print("¡Todas las tablas del proyecto fueron guardadas")


def crear_o_modificar_tabla(nombre_proyecto: str, proyectos: dict) -> dict:    
    """Menu para crear, modificar o guardar una tabla.

    Args:
        nombre_proyecto (str): nombre del proyecto actual.
        proyectos (dict): diccionario actual.

    Returns:
        dict: retorna un diccionario.
    """
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
            nom_tabla = transformar_dato(nom_tabla)
        
            if nom_tabla in proyectos[nombre_proyecto]:
                print("La tabla ya existe en este proyecto.")
            else:
                cant_cols = get_int_simple("Ingrese cantidad Columnas: ",
                                           "Error, ingrese un entero")

                tabla_tipos = []
                columnas = []
                for i in range(cant_cols):
                    col = input("Nombre Columna " + str(i + 1) + ": ")
                    col = limpiar_texto(col)
                    col = transformar_dato(col)        
                    columnas.append(col)
                    print(f"Para la columna '{col}':")
                    tip = elegir_tipo_dato()
                    tabla_tipos.append(tip)
                    
                cant_f = get_int_simple("Ingrese cantidad de Filas: ",
                                           "Error, ingrese un entero")
                
                matriz = []
                for f in range(cant_f):
                    fila = []
                    for c in range(len(columnas)):
                        valor_celda = ""            
                        fila.append(valor_celda)
                    matriz.append(fila)
                    
                proyectos[nombre_proyecto][nom_tabla] = {
                    'columnas': columnas, 
                    'tipos': tabla_tipos, 
                    'matriz': matriz
                }
                print("¡Tabla Creada!")

        elif opcion == 2:
            nom_tabla = input("Ingrese el nombre de tabla a modificar: ")
            nom_tabla = transformar_dato(nom_tabla)
            
            if nom_tabla in proyectos[nombre_proyecto]:
                tabla_elegida = proyectos[nombre_proyecto][nom_tabla]
                
                if len(tabla_elegida['columnas']) != 0:
                    modificar_tabla(tabla_elegida)
                else:
                    print("Error, tabla vacia")
            else:
                print("La tabla especificada no existe en este proyecto.")
        
        elif opcion == 3:
            guardar_tabla(nombre_proyecto, proyectos)
            
        print("\n1-Crear tabla\n2-Modificar tabla\n3-Guardar tabla\n4-Salir")

        opcion = get_int("Ingresar una opcion numerica: ", 
                         "Error, Intente otra vez", 1, 4)
    
    return proyectos


def modificar_tabla(tabla: list):
    """Menu para modificar la tabla actual.

    Args:
        tabla (list): tabla de datos.
    """
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
            seguro = obtener_respuesta(
                        "Seguro quieres eliminar una fila(s/n)?",
                        "Error, ingrese 's' o 'n", "s", "n")
            if seguro == "s":
                eliminar_fila(tabla)
        elif opcion == 3:
            agregar_columna(tabla)
        elif opcion == 4:
            seguro = obtener_respuesta(
                            "Seguro quieres eliminar una columna(s/n)?",
                            "Error, ingrese 's' o 'n'", "s", "n")
            if seguro == "s":
                eliminar_columna(tabla)
                
        
        print("1-Agregar fila")
        print("2-Eliminar fila")
        print("3-Agregar columna")
        print("4-Eliminar columna")
        print("5-Salir de modificar tabla")
        opcion = get_int("Ingresar una opcion numerica: ", 
                         "Error, Intente otra vez", 
                         1, 5)


def mostrar_tabla(nombre_proyecto: str, proyectos: dict) -> None:
    """Menu para mostrar la tabla de diferentes formas y atraves de
       distintos filtros.

    Args:
        nombre_proyecto (str): nombre del proyecto actual.
        proyectos (dict): diccionario actual.
    """
    
    nom_tabla = limpiar_texto(input("Tabla a analizar: "))
    nom_tabla = transformar_dato(nom_tabla)
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
    else:
        print("No existe tabla con ese nombre!")


def cargar_tablas_desde_csv(proyectos, nombre_proyecto):

    """
     Lee el archivo 'tablas.csv' y carga los datos guardados en la memoria.
    
    Busca las líneas que empiezan con 'Tabla: ' para identificar el nombre,
    crea el espacio en el diccionario, y luego guarda la primera línea como
    las columnas y las líneas siguientes como las filas de la matriz.
    
    Parámetros:
    - proyectos: El diccionario principal con los datos en memoria.
    - nombre_proyecto: El nombre del proyecto que se está usando.
    
    Retorna:
    - El diccionario 'proyectos' actualizado con las tablas recuperadas.
    """

    ruta = "paquete/archivos/tablas.csv"
    
    if nombre_proyecto not in proyectos:
        proyectos[nombre_proyecto] = {}
        
    archivo = open(ruta, "r")
    nom_tabla = ""
    
    for linea in archivo:
        
        if len(linea) > 0 and linea[len(linea)-1] == "\n":
            linea = linea[:-1]
            
        if len(linea) > 0:
            
            if len(linea) >= 7 and linea[0:7] == "Tabla: ":
                nom_tabla = linea[7:]
                proyectos[nombre_proyecto][nom_tabla] = {"columnas": [],
                                                            "tipos": [], 
                                                            "matriz": []}
        
            elif nom_tabla != "":
                datos = []
                palabra_actual = ""
                
                for caracter in linea:
                    if caracter == ",":
                        datos.append(palabra_actual)
                        palabra_actual = ""
                    else:
                        palabra_actual = palabra_actual + caracter
                
                
                datos.append(palabra_actual)
 
                if len(proyectos[nombre_proyecto][nom_tabla]["columnas"]) == 0:
                    proyectos[nombre_proyecto][nom_tabla]["columnas"] = datos
                else:
                    es_vacia = True
                    for d in datos:
                        if d != "":
                            es_vacia = False
                    
                    if es_vacia == False:
                        proyectos[nombre_proyecto][nom_tabla]["matriz"].append(datos)
                        
    archivo.close()
    return proyectos