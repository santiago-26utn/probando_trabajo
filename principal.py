from paquete.autenticacion import iniciar_sesion, registrar_usuario
from paquete.formato import mostrar_tabla_prolija
from paquete import estadistica as est
from paquete.validaciones import (
    es_par_recursivo, 
    es_primo_recursivo, 
    es_multiplo_recursivo, 
    leer_entero_validado,
    limpiar_texto
)

proyectos = {}

def separar_por_comas(texto: str) -> list:
    """Función manual alternativa a split() para segmentar columnas a filtrar."""
    lista = []
    acumulador = ""
    for i in range(len(texto)):
        if texto[i] == ",":
            if len(limpiar_texto(acumulador)) > 0:
                lista.append(limpiar_texto(acumulador))
            acumulador = ""
        else:
            acumulador += texto[i]
    if len(limpiar_texto(acumulador)) > 0:
        lista.append(limpiar_texto(acumulador))
    return lista

def gestionar_tablas(nombre_proyecto):
    if nombre_proyecto not in proyectos:
        proyectos[nombre_proyecto] = {}
        
    print("\n--- GESTIÓN DE TABLAR ---")
    print("1. Crear Tabla (Carga secuencial)")
    print("2. Modificar Filas/Columnas de Tabla")
    opc = input("Seleccione: ")
    
    if opc == "1":
        nom_tabla = limpiar_texto(input("Nombre de la nueva tabla: "))
        cant_col = leer_entero_validado("Cantidad de columnas: ")
        
        columnas = []
        for i in range(cant_col):
            col = limpiar_texto(input(f"Nombre de la columna {i+1}: "))
            columnas.append(col)
            
        cant_filas = leer_entero_validado("Cantidad de filas iniciales: ")
        matriz = []
        for f in range(cant_filas):
            fila = []
            print(f"--- Fila {f+1} ---")
            for c in range(cant_col):
                val = input(columnas[c] + ": ")
                fila.append(val)
            matriz.append(fila)
            
        proyectos[nombre_proyecto][nom_tabla] = {
            'columnas': columnas,
            'matriz': matriz
        }
        print("Tabla '" + nom_tabla + "' creada con éxito.")

    elif opc == "2":
        nom_tabla = limpiar_texto(input("Nombre de la tabla a modificar: "))
        if nom_tabla not in proyectos[nombre_proyecto]:
            print("La tabla no existe.")
            return
        
        tabla = proyectos[nombre_proyecto][nom_tabla]
        print("1. Agregar fila distribuida\n2. Modificar celda específica")
        sub_opc = input("Opción: ")
        if sub_opc == "1":
            nueva_fila = []
            for col in tabla['columnas']:
                val = input("Valor para " + col + ": ")
                nueva_fila.append(val)
                tabla['matriz'].append(nueva_fila)
        elif sub_opc == "2":
            f_idx = leer_entero_validado("Índice de fila: ") - 1
            c_idx = leer_entero_validado("Índice de columna: ") - 1
            if 0 <= f_idx < len(tabla['matriz']) and 0 <= c_idx < len(tabla['columnas']):
                nuevo_val = input("Nuevo valor: ")
                tabla['matriz'][f_idx][c_idx] = nuevo_val
            else:
                print("Índices fuera de rango.")

def ejecutar_estadisticas(nombre_proyecto):
    nom_tabla = limpiar_texto(input("Nombre de la tabla a analizar: "))
    if nom_tabla not in proyectos[nombre_proyecto]:
        print("Tabla no encontrada.")
        return
    
    tabla = proyectos[nombre_proyecto][nom_tabla]
    print("\nColumnas disponibles:")
    for i in range(len(tabla['columnas'])):
        print(str(i+1) + ". " + tabla['columnas'][i])
        
    col_idx = leer_entero_validado("Seleccione el número de columna: ") - 1
    if not (0 <= col_idx < len(tabla['columnas'])):
        print("Selección inválida.")
        return
        
    valores = est.obtener_columna_numerica(tabla['matriz'], col_idx)
    if len(valores) == 0:
        print("No se encontraron datos numéricos procesables en esa columna.")
        return
        
    print("\n--- REPORTE ESTADÍSTICO PARA: " + tabla['columnas'][col_idx] + " ---")
    print("Conteo de registros: " + str(len(valores)))
    print("Máximo: " + str(est.calcular_maximo(valores)))
    print("Mínimo: " + str(est.calcular_minimo(valores)))
    print("Promedio Aritmético: " + str(est.calcular_promedio_aritmetico(valores)))
    print("Promedio Geométrico: " + str(est.calcular_promedio_geometrico(valores)))
    print("Varianza: " + str(est.calcular_varianza(valores)))
    print("Desviación Estándar: " + str(est.calcular_desviacion_estandar(valores)))
    
    primer_val = int(valores[0])
    print("\n[Validación del primer valor entero (" + str(primer_val) + ")]:")
    print("¿Es par? " + str(es_par_recursivo(primer_val)))
    print("¿Es primo? " + str(es_primo_recursivo(primer_val)))
    print("¿Es múltiplo de 5? " + str(es_multiplo_recursivo(primer_val, 5)))

def programa_principal():
    autenticado = False
    while not autenticado:
        print("\n=== BIENVENIDO AL SISTEMA ESTADÍSTICO UTN ===")
        print("1. Iniciar Sesión\n2. Registrarse\n3. Salir")
        opc = input("Opción: ")
        if opc == "1":
            autenticado = iniciar_sesion()
        elif opc == "2":
            registrar_usuario()
        elif opc == "3":
            return
            
    proyecto_activo = "Proyecto_Predeterminado"
    
    while True:
        print("\n[Proyecto Activo: " + proyecto_activo + "]")
        print("a) Proyectos (Cambiar/Crear)")
        print("b) Tablas (Crear/Modificar)")
        print("c) Variables")
        print("d) Mostrar Tabla")
        print("e) Estadística")
        print("f) Salir")
        
        opcion = input("Seleccione opción: ").lower()
        
        if opcion == "a":
            proyecto_activo = limpiar_texto(input("Nombre del proyecto: "))
            if proyecto_activo not in proyectos:
                proyectos[proyecto_activo] = {}
            print("Cambiado al proyecto: " + proyecto_activo)
            
        elif opcion == "b" or opcion == "c":
            gestionar_tablas(proyecto_activo)
            
        elif opcion == "d":
            nom_tabla = limpiar_texto(input("Nombre de la tabla a visualizar: "))
            if nom_tabla in proyectos[proyecto_activo]:
                print("¿Desea filtrar columnas? (s/n)")
                if input().lower() == 's':
                    cols_str = input("Ingrese nombres de columnas separadas por coma: ")
                    lista_filtros = separar_por_comas(cols_str)
                    mostrar_tabla_prolija(proyectos[proyecto_activo][nom_tabla], lista_filtros)
                else:
                    mostrar_tabla_prolija(proyectos[proyecto_activo][nom_tabla])
            else:
                print("Tabla no encontrada.")
        elif opcion == "e":
            ejecutar_estadisticas(proyecto_activo)
            
        elif opcion == "f":
            print("Cerrando el sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    programa_principal()
