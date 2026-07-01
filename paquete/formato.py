from paquete.validacion.validaciones import limpiar_texto, leer_entero_validado, convertir_a_minuscula
from paquete.estadistica import estadistica
from paquete.validacion.validaciones import *


def mostrar_tabla_prolija(tabla_dict: dict, 
                          columnas_filtradas: list = None):
    """Muestra la tabla ordenada.

    Args:
        tabla_dict (dict): diccionario
        columnas_filtradas (list, opcional): opcion para filtrar tablas,
                                             por defecto None.
    """
    columnas = tabla_dict['columnas']
    matriz = tabla_dict['matriz']
    
    if len(matriz) == 0:
        print("La tabla está vacía.")
        return

    indices_a_mostrar = []
    for i in range(len(columnas)):
        if columnas_filtradas is None:
            indices_a_mostrar.append(i)
        else:
            encontrado = False
            for col_filtro in columnas_filtradas:
                if columnas[i] == col_filtro:
                    encontrado = True
            if encontrado:
                indices_a_mostrar.append(i)

    if len(indices_a_mostrar) == 0:
        print("No hay columnas seleccionadas para visualizar.")
        return
    
    anchos = []
    for i in range(len(columnas)):
        max_ancho = len(str(columnas[i]))
        for fila in matriz:
            largo_val = len(str(fila[i]))
            if largo_val > max_ancho:
                max_ancho = largo_val
        anchos.append(max_ancho + 2)

    linea_encabezado = ""
    for idx in indices_a_mostrar:
        texto = str(columnas[idx])
        espacios = anchos[idx] - len(texto)
        linea_encabezado += texto + (" " * espacios) + "|"
        
    print("\n" + "-" * len(linea_encabezado))
    print(linea_encabezado)
    print("-" * len(linea_encabezado))

    for fila in matriz:
        linea_fila = ""
        for idx in indices_a_mostrar:
            texto = str(fila[idx])
            espacios = anchos[idx] - len(texto)
            linea_fila += texto + (" " * espacios) + "|"
        print(linea_fila)
    print("-" * len(linea_encabezado))


from paquete.validacion.validaciones import (
    limpiar_texto, 
    leer_entero_validado, 
    convertir_a_minuscula,
    es_par_recursivo, 
    es_primo_recursivo, 
    es_multiplo_recursivo
)
from paquete.estadistica import estadistica

def separar_por_comas(texto: str) -> list:
    """Separa un texto por comas.

    Args:
        texto (str): cadena de texto

    Returns:
        list: retorna .
    """
    lista, acumulador = [], ""
    for i in range(len(texto)):
        if texto[i] == ",":
            if len(limpiar_texto(acumulador)) > 0: lista.append(limpiar_texto(acumulador))
            acumulador = ""
        else: acumulador += texto[i]
    if len(limpiar_texto(acumulador)) > 0: lista.append(limpiar_texto(acumulador))
    return lista
