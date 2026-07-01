from paquete.validacion.validaciones import *
from paquete.tabla.tablas import *

def contar_valor_columna(lista: list, valor: int) -> int:
    """Muestra cuanto se repite un valor en especifico en una columna.

    Args:
        lista (list): lista de valores.
        valor (int): valor numeral.

    Returns:
        int: retorna el valor y el numero de veces que se repite.
    """
    total_valor = 0

    for i in range(len(lista)):
        if lista[i] == valor:
            total_valor += 1

    return valor, total_valor

def listar_valores_repetidos(lista: list) -> list:
    """lista los valores y cuantas veces se repitieron.

    Args:
        lista (list): lista de valores.

    Returns:
        list: lista de valores y su numero de repeticiones.
    """
    lista_valores = []
    if len(lista) > 0:
        lista_valores.append(lista[0])

    for i in range(1, len(lista)):
        # ANTES: if i not in lista_valores:
        if lista[i] not in lista_valores:
            lista_valores.append(lista[i])

    return lista_valores


def contar_valores_columna(lista: list) -> None:
    """Muestra valores y el numero de veces que se repitieron en una lista.

    Args:
        lista (list): lista de valores
    """
    lista_valores = listar_valores_repetidos(lista)

    for valor in lista_valores:
        print(contar_valor_columna(lista, valor))


def mostrar_maximo_y_minimo(lista: list) -> None:
    """En una lista muestra el maximo y el minimo valor.

    Args:
        lista (list): lista de valores.
    """
    print(f"El minimo es: {lista[0]}")
    print(f"El maximo es: {lista[-1]}")


def mostrar_moda(lista: list) -> None:
    """Muestra la moda de una lista de valores.

    Args:
        lista (list): lista de valores.
    """
    lista_valores = listar_valores_repetidos(lista)
    
    if len(lista_valores) == 0:
        print("No hay datos para calcular la moda.")
        return

    moda = lista_valores[0]
    max_frecuencia = contar_valor_columna(lista, moda)[1]              

    for i in range(1, len(lista_valores)):
        frec_actual = contar_valor_columna(lista, lista_valores[i])[1]
        if frec_actual > max_frecuencia:
            max_frecuencia = frec_actual
            moda = lista_valores[i]

    if max_frecuencia > 1:
        print(f"La moda de la columna es: {moda} (Se repite {max_frecuencia} veces)")
    else:
        print(f"No hay moda, todos los valores se repiten una vez")



def mostrar_rango(lista: list) -> None:
    """Muestra el rango restando el minimo al maximo.

    Args:
        lista (list): lista de valores.
    """
    rango = lista[-1] - lista[0]
    print(f" El rango es de: {rango}")




def verificar_columna_con_numeros(tabla: dict, columna_elegida: str) -> bool:
    """Verifica si todas las celdas de la columna seleccionada contienen 
       números.
    Args:
        tabla (dict): tabla de valores.
        columna_elegida (str): nombre de columna.

    Returns:
        bool: retorna True si todas las celdas tienen numero o False caso 
              contrario.
    """
    indice_columna = obtener_indice_columna(tabla, columna_elegida)
    
    if indice_columna == -1:
        return False
        
    columna_numeros = True
    for i in range(len(tabla['matriz'])):
        posible_numero = tabla['matriz'][i][indice_columna]
        if type(posible_numero) != int and type(posible_numero) != float:
            columna_numeros = False
            
    return columna_numeros


def obtener_columna_con_numeros(tabla: dict) -> str:
    """Pide una columna por consola hasta que el usuario ingrese una que sea
       numérica y la retorna.
    Args:
        tabla (dict): tabla de valores.

    Returns:
        str: retorna la columna si solo contiene numeros.
    """
    columna = retornar_columna(tabla)
    columna_numeros = verificar_columna_con_numeros(tabla, columna)         #ver si se puede evitar repeticion de codigo

    while columna_numeros == False:
        print(" Esa columna no es numérica o contiene texto. Elija otra.")
        columna = retornar_columna(tabla)
        columna_numeros = verificar_columna_con_numeros(tabla, columna)
    
    return columna


def crear_lista_numeros_de_columna(tabla: dict) -> list:
    """Extrae los datos numéricos puros de la columna elegida para 
       enviárselos a las estadísticas.
    Args:
        tabla (dict): tabla de valores.

    Returns:
        list: retorna una lista con los valores de la columna elegida.
    """
    columna = obtener_columna_con_numeros(tabla)
    columna_indice = obtener_indice_columna(tabla, columna)
    lista_columna = []

    for i in range(len(tabla['matriz'])):
        lista_columna.append(tabla['matriz'][i][columna_indice])
    
    return lista_columna




def calcular_promedio_aritmetico(lista: list) -> float:    
    """Calcula el promedio aritmetico de la lista pasada.

    Args:
        lista (list): lista de numeros

    Returns:
        float: Retorna un float como promedio aritmetico.
    """
    total_columna = 0
    total_elementos_columna = len(lista)

    for i in range(len(lista)):
        total_columna += lista[i]

    promedio_aritmetico = total_columna / total_elementos_columna

    return promedio_aritmetico


    
def calcular_promedio_geometrico(lista: list) -> float:        
    """Calcula el promedio geometrico de la lista pasada.

    Args:
        lista (list): lista de numeros

    Returns:
        float: Retorna un float como promedio geometrico.
    """
    indice_columna = 3
    total_columna = 1
    total_elementos_columna = len(lista)


    for i in range(len(lista)):
        total_columna *= lista[i]

    promedio_geometrico = calcular_raiz(total_columna, total_elementos_columna)

    return promedio_geometrico



def mostrar_mediana(lista_columna: list) -> None:
    """Calcula y muestra la mediana de una lista.

    Args:
        lista_columna (list): lista de numeros.
    """
    cantidad_numeros = len(lista_columna)

    if verificar_paridad_con_booleano(cantidad_numeros):
        indice_1 = cantidad_numeros // 2 - 1
        indice_2 = cantidad_numeros // 2

        numero_mediano = (lista_columna[indice_1] +
                          lista_columna[indice_2]) / 2

    else:
        indice = cantidad_numeros // 2
        numero_mediano = lista_columna[indice]

    print(f"La mediana es: {numero_mediano}")


def retornar_varianza(lista_columna: list) -> int:
    """Calcula la varianza de una lista.

    Args:
        lista_columna (list): lista de numeros.

    Returns:
        int: retorna la varianza calculada como int
    """
    cantidad_numeros = len(lista_columna)
    media = calcular_promedio_aritmetico(lista_columna)
    suma_cuadrados = 0

    for i in range(len(lista_columna)):
        numero_actual = lista_columna[i] - media
        numero_elevado_a_2 = numero_actual * numero_actual
        suma_cuadrados += numero_elevado_a_2
    
    varianza = suma_cuadrados / cantidad_numeros
    return varianza

def retornar_desviacion_estandar(lista_columna: list) -> float|int:
    """Devuelve la desviacion estandar calculada.

    Args:
        lista_columna (list): lista de numeros.

    Returns:
        float|int: retorna la desviacion como float o int.
    """
    varianza = retornar_varianza(lista_columna)
    desviacion_estandar = calcular_raiz(varianza, 2)

    return desviacion_estandar


def mostrar_coeficiente_de_variacion(lista_columna: list) -> None:
    """Calcula el coeficiente de variacion y lo muestra.

    Args:
        lista_columna (list): lista de numeros.
    """
    desviacion = retornar_desviacion_estandar(lista_columna)
    media = calcular_promedio_aritmetico(lista_columna)
    coeficiente = (desviacion / media) * 100

    print(f"El coeficiente de varianza es de: {coeficiente}")


def mostrar_promedios(lista: list) -> None:
    """Muestra el promedio aritmetico y geometrico.

    Args:
        lista (list): lista de numeros.
    """
    promedio_aritmetico = calcular_promedio_aritmetico(lista)
    promedio_geometrico = calcular_promedio_geometrico(lista)

    print(f"El promedio aritmetico es: {promedio_aritmetico}")
    print(f"El promedio aritmetico es: {promedio_geometrico}")


def mostrar_cuartil(lista: list, medida: int):
    n = len(lista)
    pos = int(medida * (n + 1) / 4)
    print("Q", medida, "=", lista[pos - 1])


def mostrar_decil(lista: list, medida: int):
    n = len(lista)
    pos = int(medida * (n + 1) / 10)
    print("D", medida, "=", lista[pos - 1])

    
def mostrar_medida_tendencia(lista_ordenada: list):
    ""
    medida_quartil = get_int("Ingrese una medida entre 1 y 3",
                             "Error, ingrese un entero entre 1 y 3",
                             1, 3)
    medida_decil = get_int("Ingrese una medida entre 1 y 10",
                             "Error, ingrese un entero entre 1 y 10",
                             1, 10)

    mostrar_cuartil(lista_ordenada, medida_quartil)
    mostrar_decil(lista_ordenada, medida_decil)




def mostrar_estadisticas(nombre_proyecto: str, proyectos: dict) -> None:
    """Muestra las estadisticas de un diccionario de un proyecto.

    Args:
        nombre_proyecto (str): nombre de un proyecto.
        proyectos (dict): diccionario con valores.
    """
    nom_tabla = limpiar_texto(input("Tabla a analizar: "))
    if nom_tabla in proyectos[nombre_proyecto]:
        tabla = proyectos[nombre_proyecto][nom_tabla]

    lista_datos = crear_lista_numeros_de_columna(tabla)
    lista_ordenada = ordenar_array(lista_datos)

    print("1.Contar valores de columna\n",
          "2.Mostrar maximo y minimo\n",
          "3.Mostrar promedios\n",
          "4.Mostrar mediana\n",
          "5.Mostrar moda\n",
          "6.Mostrar medidas de tendencia\n",
          "7.Mostrar rango\n",
          "8.Mostrar varianza\n",
          "9.Mostrar desviación estandar\n",
          "10.Mostrar coeficiente de varianza\n",
          "11.Salir de mostrar estadisticas\n")
    
    opcion_elegida = 0

    while opcion_elegida != 11:
            
        opcion_elegida = get_int("Ingrese una opción: ", 
                                "La opcion debe ser número entero(1 a 11)", 
                                1, 11)
        
        match opcion_elegida:
            case 1:
                contar_valores_columna(lista_ordenada)
            case 2:
                mostrar_maximo_y_minimo(lista_ordenada)
            case 3:
                mostrar_promedios(lista_ordenada)
            case 4:
                mostrar_mediana(lista_ordenada)
            case 5:
                mostrar_moda(lista_ordenada)
            case 6:
                mostrar_medida_tendencia(lista_ordenada)
            case 7:
                mostrar_rango(lista_ordenada)
            case 8:
                print(f"La varianza es: {retornar_varianza(lista_ordenada)}")
            case 9:
                print(f"La desviacion estandar es: "
                    f"{retornar_desviacion_estandar(lista_ordenada)}")
            case 10:
                mostrar_coeficiente_de_variacion(lista_ordenada)
            case 11:
                break
            case _:
                opcion_elegida = get_int("Ingrese una opción", 
                                "La opcion debe ser número entero(1 a 10)", 
                                1, 11)