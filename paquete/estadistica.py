def es_flotante_valido(entrada: str) -> bool:
    """Verifica si un string se puede convertir a float de forma estructurada."""
    if len(entrada) == 0:
        return False
    
    inicio = 0
    if entrada[0] == '-':
        inicio = 1
        
    puntos = 0
    for i in range(inicio, len(entrada)):
        if entrada[i] == '.':
            puntos += 1
            if puntos > 1:
                return False
        elif entrada[i] < '0' or entrada[i] > '9':
            return False
    return True

def obtener_columna_numerica(matriz: list, idx_columna: int) -> list:
    valores = []
    for fila in matriz:
        val_str = str(fila[idx_columna]).strip()
        if es_flotante_valido(val_str):
            valores.append(float(val_str))
    return valores

def calcular_maximo(valores: list) -> float:
    if len(valores) == 0: return 0.0
    maxi = valores[0]
    for v in valores:
        if v > maxi: maxi = v
    return maxi

def calcular_minimo(valores: list) -> float:
    if len(valores) == 0: return 0.0
    mini = valores[0]
    for v in valores:
        if v < mini: mini = v
    return mini

def calcular_promedio_aritmetico(valores: list) -> float:
    if len(valores) == 0: return 0.0
    suma = 0.0
    for v in valores:
        suma += v
    return suma / len(valores)

def calcular_promedio_geometrico(valores: list) -> float:
    if len(valores) == 0: return 0.0
    producto = 1.0
    for v in valores:
        if v <= 0:
            return 0.0
        producto *= v
    return producto ** (1 / len(valores))

def calcular_varianza(valores: list) -> float:
    if len(valores) == 0: return 0.0
    media = calcular_promedio_aritmetico(valores)
    suma_cuadrados = 0.0
    for v in valores:
        suma_cuadrados += (v - media) ** 2
    return suma_cuadrados / len(valores)

def calcular_desviacion_estandar(valores: list) -> float:
    return calcular_varianza(valores) ** 0.5