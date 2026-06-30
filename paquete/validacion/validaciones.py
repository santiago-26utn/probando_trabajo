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









def obtener_respuesta(mensaje: str, 
                      mensaje_error: str, 
                      respuesta_positiva: str,
                      respuesta_negativa: str):
    ""
    respuesta_aceptada = False

    while True:
        respuesta = input(mensaje)

        if respuesta == respuesta_positiva or respuesta == respuesta_negativa:
            return respuesta
        print(mensaje_error)


def validar_rango(valor: any, minimo: int, maximo: int) -> bool:
    """Valida si una cadena representa un número entero dentro de un rango
       específico.

    Args:
        valor (any): El valor ingresado por el usuario.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Returns:
        bool: True si el valor es válido, False en caso contrario.
    """
    return minimo <= valor <= maximo

def get_int_simple(mensaje: str, mensaje_error: str) -> int:
    ""

    while True:
        dato = input(mensaje)
        n = len(dato)
        es_numero = True

        for i in dato:
            if i not in "0123456789":
                es_numero = False

        if es_numero and n > 0 and dato != "0":
            numero = 0
            for i in dato:
                numero = numero * 10 + (ord(i) - ord("0"))
            return numero
        
        print(mensaje_error)


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    ""

    while True:
        numero = get_int_simple(mensaje, mensaje_error)
        
        if validar_rango(numero, minimo, maximo) == True:
            return numero
        
        print(mensaje_error)



def calcular_raiz(numero: float, indice: int) -> float|int:  
    aproximacion = numero

    for _ in range(8):
        aproximacion = ((indice - 1) * aproximacion + numero / (aproximacion ** (indice - 1))) / indice

    return aproximacion


def ordenar_array(array_numeros: list, descendente: bool=False) -> list:
    """ordena un array por default en forma ascendente, o descendente
       si se le pasa un True de parametro


    Args:
        array_numeros (list): array de numeros enteros.
        descendente (bool, optional): Si esta en False ordena de forma 
                                      ascendente, si esta en True ordena 
                                      descendente. Defaults to False.

    Returns:
        list: retorna la lista ordenada segun el parametro "descendente".
    """
    n = len(array_numeros)

    for i in range(n):

        limite_superior = n - i - 1

        for j in range(0, limite_superior):

            if (not descendente and array_numeros[j] > array_numeros[j + 1]) or \
               (descendente and array_numeros[j] < array_numeros[j + 1]):

                menor = array_numeros[j + 1]
                array_numeros[j + 1] = array_numeros[j]
                array_numeros[j] = menor

    return array_numeros


def verificar_paridad_con_booleano(numero: int) -> bool:
    """Verifica si el número ingresado es par o no.

    Returns:
        bool: retorna "False" si el número es impar y "True" en caso 
              contrario.
    """

    paridad = False

    if numero == 0:
        paridad = True
    elif numero > 1:
        paridad = verificar_paridad_con_booleano(numero - 2)

    return paridad



def hacer_mayuscula(caracter: str) -> str:
    ""

    codigo = ord(caracter)

    return chr(codigo - 32)

def verificar_mayuscula(dato_ingresado: str) -> str:
    ""

    letra_verificada = ""

    if ord(dato_ingresado[0]) > 64 and ord(dato_ingresado[0]) < 91:
        letra_verificada += dato_ingresado[0]
    else:
        letra_verificada += hacer_mayuscula(dato_ingresado[0])

    return letra_verificada


def hacer_minuscula(caracter: str) -> str:
    ""

    codigo = ord(caracter)

    return chr(codigo + 32)

def verificar_minuscula(dato_ingresado: str, posicion_letra: int) -> str:
    ""

    letra_verificada = ""

    if ord(dato_ingresado[posicion_letra]) > 96 and ord(dato_ingresado[posicion_letra]) < 123:
        letra_verificada += dato_ingresado[posicion_letra]
    else:
        letra_verificada += hacer_minuscula(dato_ingresado[posicion_letra])

    return letra_verificada

def transformar_dato(dato_ingresado: any) -> str|float:
    ""
    dato_numerico = 0
    dato_transformado = ""

    if type(dato_ingresado) == int or dato_ingresado in "0123456789":       #arreglar esto que no acepta los numeros float
        dato_numerico += int(dato_ingresado)
    else:
        for i in range(len(dato_ingresado)):
            if i == 0:
                dato_transformado += verificar_mayuscula(dato_ingresado)
            else:
                dato_transformado += verificar_minuscula(dato_ingresado, i)

    if type(dato_ingresado) == int:
        dato_retornar = dato_numerico
    else:
        dato_retornar = dato_transformado

    return dato_retornar