def es_par_recursivo(n: int) -> bool:
    if n == 0:
        return True
    if n == 1:
        return False
    if n < 0:
        return es_par_recursivo(-n)
    return es_par_recursivo(n - 2)

def es_multiplo_recursivo(a: int, b: int) -> bool:
    if b == 0:
        return False
    if a < 0:
        return es_multiplo_recursivo(-a, abs(b))
    if b < 0:
        return es_multiplo_recursivo(a, -b)
    if a == 0:
        return True
    if a < b:
        return False
    return es_multiplo_recursivo(a - b, b)

def es_primo_recursivo(n: int, divisor: int = None) -> bool:
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if es_multiplo_recursivo(n, divisor):
        return False
    return es_primo_recursivo(n, divisor - 1)

def validar_rango_recursivo(valor: float, minimo: float, maximo: float) -> bool:
    if valor < minimo or valor > maximo:
        return False
    return True

def es_cadena_numerica(entrada: str) -> bool:
    """Verifica si un string representa un entero de forma manual."""
    if len(entrada) == 0:
        return False
    
    inicio = 0
    if entrada[0] == '-':
        if len(entrada) == 1:
            return False
        inicio = 1
        
    for i in range(inicio, len(entrada)):
        if entrada[i] < '0' or entrada[i] > '9':
            return False
    return True

def leer_entero_validado(mensaje: str) -> int:
    """Fuerza al usuario a ingresar un entero usando validación de string manual."""
    entrada = input(mensaje).strip()
    if es_cadena_numerica(entrada):
        return int(entrada)
    print("Error: Debe ingresar un número entero válido.")
    return leer_entero_validado(mensaje)

def limpiar_texto(texto: str) -> str:
        
        if len(texto) == 0:
            return texto
        
        inicio = 0
        fin = len(texto) - 1
    
        while inicio <= fin and (texto[inicio] == " " or texto[inicio] == "\n"):
            inicio += 1
        while fin >= inicio and (texto[fin] == " " or texto[fin] == "\n"):
            fin -= 1
        resultado = ""
        for i in range(inicio, fin + 1):
            resultado += texto[i]
        
        return resultado


def convertir_a_minuscula(texto: str) -> str:
    resultado = ""
    for i in range(len(texto)):
        caracter = texto[i]
        if "A" <= caracter <= "Z":
            resultado += chr(ord(caracter) + 32)
        else:
            resultado += caracter
    return resultado