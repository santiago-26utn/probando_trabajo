def limpiar_texto(texto: str) -> str:
    resultado_str = texto
    if len(texto) > 0:
        inicio = 0
        fin = len(texto) - 1

        while inicio <= fin and (texto[inicio] == " " or texto[inicio] == "\n"):
            inicio += 1

        while fin >= inicio and (texto[fin] == " " or texto[fin] == "\n"):
            fin -= 1

        acumulador = ""
        for i in range(inicio, fin + 1):
            acumulador += texto[i]
        resultado_str = acumulador

    return resultado_str

def convertir_a_minuscula(texto: str) -> str:

    resultado_str = ""
    for i in range(len(texto)):
        caracter = texto[i]
        if "A" <= caracter <= "Z":
            resultado_str += chr(ord(caracter) + 32)
        else:
            resultado_str += caracter
    return resultado_str

def es_par_recursivo(n: int) -> bool:
    res = False

    if n == 0:
        res = True
    elif n == 1:
        res = False
    elif n < 0:
        res = es_par_recursivo(-n)
    else:
        res = es_par_recursivo(n - 2)

    return res

def es_multiplo_recursivo(a: int, b: int) -> bool:
    res = False

    if b == 0:
        res = False
    elif a < 0:
        res = es_multiplo_recursivo(-a, b if b > 0 else -b)
    elif b < 0:
        res = es_multiplo_recursivo(a, -b)
    elif a == 0:
        res = True
    elif a < b:
        res = False
    else:
        res = es_multiplo_recursivo(a - b, b)

    return res

def es_primo_recursivo(n: int, divisor: int = None) -> bool:
    res = False

    if n <= 1:
        res = False
    else:
        div_actual = divisor
        if div_actual is None:
            div_actual = n - 1

        if div_actual == 1:
            res = True
        elif es_multiplo_recursivo(n, div_actual):
            res = False
        else:
            res = es_primo_recursivo(n, div_actual - 1)

    return res

def validar_rango_recursivo(valor: float, minimo: float, maximo: float) -> bool:
    res = True
    if valor < minimo or valor > maximo:
        res = False
    return res

def es_cadena_numerica(entrada: str) -> bool:
    res = True
    if len(entrada) == 0:
        res = False
    else:
        inicio = 0
        if entrada[0] == '-':
            if len(entrada) == 1:
                res = False
            inicio = 1
        if res:
            for i in range(inicio, len(entrada)):
                if entrada[i] < '0' or entrada[i] > '9':
                    res = False

    return res

def leer_entero_validado(mensaje: str) -> int:
    entrada = limpiar_texto(input(mensaje))
    res_entero = 0

    if es_cadena_numerica(entrada):
        res_entero = int(entrada)
    else:
        print("Error: Debe ingresar un número entero válido.")
        res_entero = leer_entero_validado(mensaje)

    return res_entero