def mostrar_tabla_prolija(tabla_dict: dict, columnas_filtradas: list = None):
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
            # Buscamos si la columna actual está en los filtros
            encontrado = False
            for col_filtro in columnas_filtradas:
                if columnas[i] == col_filtro:
                    encontrado = True
            if encontrado:
                indices_a_mostrar.append(i)

    if len(indices_a_mostrar) == 0:
        print("No hay columnas seleccionadas para visualizar.")
        return

    # Calcular anchos fijos manualmente
    anchos = []
    for i in range(len(columnas)):
        max_ancho = len(columnas[i])
        for fila in matriz:
            largo_val = len(str(fila[i]))
            if largo_val > max_ancho:
                max_ancho = largo_val
        anchos.append(max_ancho + 2)

    # Imprimir Encabezado
    linea_encabezado = ""
    for idx in indices_a_mostrar:
        # Relleno manual de espacios a la derecha (ljust casero)
        texto = str(columnas[idx])
        espacios = anchos[idx] - len(texto)
        linea_encabezado += texto + (" " * espacios) + "|"
        
    print("\n" + "-" * len(linea_encabezado))
    print(linea_encabezado)
    print("-" * len(linea_encabezado))

    # Imprimir Filas
    for fila in matriz:
        linea_fila = ""
        for idx in indices_a_mostrar:
            texto = str(fila[idx])
            espacios = anchos[idx] - len(texto)
            linea_fila += texto + (" " * espacios) + "|"
        print(linea_fila)
    print("-" * len(linea_encabezado))