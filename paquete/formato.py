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
    lista, acumulador = [], ""
    for i in range(len(texto)):
        if texto[i] == ",":
            if len(limpiar_texto(acumulador)) > 0: lista.append(limpiar_texto(acumulador))
            acumulador = ""
        else: acumulador += texto[i]
    if len(limpiar_texto(acumulador)) > 0: lista.append(limpiar_texto(acumulador))
    return lista

def gestionar_tablas(nombre_proyecto: str, proyectos: dict):
    if nombre_proyecto not in proyectos: 
        proyectos[nombre_proyecto] = {}

    print("\n1. Crear Tabla\n2. Guardar tabla\n3. Modificar Tabla")
    opc = input("Opción: ")
    
    if opc == "1":
        nom_tabla = limpiar_texto(input("Nombre tabla: "))
        
        if nom_tabla in proyectos[nombre_proyecto]:
            print("La tabla ya existe en este proyecto.")
        else:
            cant_cols = leer_entero_validado("Columnas: ")
        
            columnas = []
            for i in range (cant_cols):
                col = limpiar_texto(input("Nombre Columna " + str(i + 1) + ": "))
                columnas.append(col)
            
            cant_f = leer_entero_validado("Filas: ")
        
            matriz = []
            for f in range(cant_f):
                fila = []
                for c in range(len(columnas)):
                    valor_celda = input(f"{columnas[c]}: ") #antes: columnas[c] + ": "
                    valor_celda = es_numero(valor_celda)            #nuevo
                    fila.append(valor_celda)
                matriz.append(fila)
            
            proyectos[nombre_proyecto][nom_tabla] = {'columnas': columnas, 'matriz': matriz}
            print("¡Creada!")
    
    elif opc == "2":
        archivo_csv = open("paquete/archivos/tablas.csv", "w")

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

    elif opc == "3":
        nom_tabla = limpiar_texto(input("Nombre tabla a modificar: "))
        if nom_tabla in proyectos[nombre_proyecto]:
            tabla = proyectos[nombre_proyecto][nom_tabla]
            print("1. Agregar fila\n2. Modificar celda")
            sub_opc = input("Opción: ")
            
            if sub_opc == "1":
                nueva_fila = []
                for c in range(len(tabla['columnas'])):
                    valor_col = input(tabla['columnas'][c] + ": ")
                    nueva_fila.append(valor_col)
                tabla['matriz'].append(nueva_fila)
            else:
                f = leer_entero_validado("Fila: ") - 1
                c = leer_entero_validado("Col: ") - 1
                if 0 <= f < len(tabla['matriz']) and 0 <= c < len(tabla['columnas']):
                    tabla['matriz'][f][c] = input("Nuevo valor: ")
                else: 
                    print("Fuera de rango.")
        else: 
            print("No existe.")
        
        

    elif opc == 3:
        print("Salir")


def ejecutar_estadisticas(nombre_proyecto: str, proyectos: dict):
    nom_tabla = limpiar_texto(input("Tabla a analizar: "))
    if nom_tabla in proyectos[nombre_proyecto]:
        tabla = proyectos[nombre_proyecto][nom_tabla]
        
        for i in range(len(tabla['columnas'])): 
            print(str(i + 1) + ". " + tabla['columnas'][i])
            
        col_idx = leer_entero_validado("Seleccione columna: ") - 1
        
        if 0 <= col_idx < len(tabla['columnas']):
            valores = estadistica.obtener_columna_numerica(tabla['matriz'], col_idx)
            if len(valores) > 0:
                print("\n--- REPORTE: " + tabla['columnas'][col_idx] + " ---")
                print("Cant: " + str(len(valores)) + " | Máx: " + str(estadistica.calcular_maximo(valores)) + " | Mín: " + str(estadistica.calcular_minimo(valores)))
                print("P.Arit: " + str(estadistica.calcular_promedio_aritmetico(valores)) + " | P.Geom: " + str(estadistica.calcular_promedio_geometrico(valores)))
                print("Var: " + str(estadistica.calcular_varianza(valores)) + " | Desv: " + str(estadistica.calcular_desviacion_estandar(valores)))
                
                p_val = int(valores[0])
                print("Primer valor (" + str(p_val) + ") -> Par: " + str(es_par_recursivo(p_val)) + " | Primo: " + str(es_primo_recursivo(p_val)) + " | Mult 5: " + str(es_multiplo_recursivo(p_val, 5)))
            else: 
                print("Sin datos numéricos.")
        else: 
            print("Selección inválida.")
    else: 
        print("No encontrada.")