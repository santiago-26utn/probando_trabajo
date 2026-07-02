def limpiar_texto(texto: str) -> str:
    """Devuelve 'texto' tras eliminar espacios en blanco y caracteres 
       especiales.

    Args:
        texto (str): cadena de texto.

    Returns:
        str: Retorna una cadena de texto tras 'limpiarla'
    """
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
    """Convierte el texto a minuscula.

    Args:
        texto (str): cadena de texto.

    Returns:
        str: retorna el texto convertido en minusculas.
    """
    resultado_str = ""
    for i in range(len(texto)):
        caracter = texto[i]
        if "A" <= caracter <= "Z":
            resultado_str += chr(ord(caracter) + 32)
        else:
            resultado_str += caracter

    return resultado_str


def validar_rango_recursivo(valor: float, minimo: float, maximo: float) -> bool:
    """Valida el rango de forma recursiva

    Args:
        valor (float): valor ingresado.
        minimo (float): valor minimo.
        maximo (float): valor maximo.

    Returns:
        bool: retorna True si el valor es aceptado dentro del rango, 
                caso contrario False.
    """
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
    """verifica si la cadena es un entero.

    Args:
        mensaje (str): mensaje

    Returns:
        int: retorna un entero.
    """
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
                      respuesta_negativa: str) -> str:
    """Pide una respuesta a una pregunta de si o no.

    Args:
        mensaje (str): mensaje pregunta.
        mensaje_error (str): mensaje error.
        respuesta_positiva (str): respuesta positiva.
        respuesta_negativa (str): respuesta negativa.

    Returns:
        str: retorna un texto igual a 'respuesta positiva' o 
             igual a 'respuesta negativa'.
    """
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
    """Pide repetidamente al usuario un numero entero, 
       deja de pedir cuando el dato es correctamente ingresado.

    Args:
        mensaje (str): mensaje.
        mensaje_error (str): mensaje error.

    Returns:
        int: retorna el numero elegido.
    """

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


def get_int(mensaje: str, 
            mensaje_error: str, 
            minimo: int, 
            maximo: int) -> int:
    """Pide repetidamente al usuario un numero entero entre cierto rango, 
       deja de pedir cuando el dato es correctamente ingresado.

    Args:
        mensaje (str): mensaje.
        mensaje_error (str): mensaje error.
        minimo (int): rango minimo.
        maximo (int): rango maximo.

    Returns:
        int: retorna el numero elegido dentro del rango.
    """

    while True:
        numero = get_int_simple(mensaje, mensaje_error)
        
        if validar_rango(numero, minimo, maximo) == True:
            return numero
        
        print(mensaje_error)



def calcular_raiz(numero: float, indice: int) -> float|int:  
    """Calcula una raiz de forma recursiva.

    Args:
        numero (float): numero a calcular raiz.
        indice (int): indice de la raiz.

    Returns:
        float|int: Retorna un int o float dependiendo del calculo.
    """
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
    """convierte a mayuscula el caracter pasado como parametro.

    Args:
        caracter (str): caracter.

    Returns:
        str: retorna el caracter transformado.
    """

    codigo = ord(caracter)

    return chr(codigo - 32)

def verificar_mayuscula(dato_ingresado: str) -> str:
    """Verifica si el dato ingresado tiene mayusculas.

    Args:
        dato_ingresado (str): cadena de texto.

    Returns:
        str: retorna la cadena de texto transformada.
    """

    letra_verificada = ""

    if ord(dato_ingresado[0]) > 64 and ord(dato_ingresado[0]) < 91:
        letra_verificada += dato_ingresado[0]
    else:
        letra_verificada += hacer_mayuscula(dato_ingresado[0])

    return letra_verificada


def hacer_minuscula(caracter: str) -> str:
    """convierte a minuscula el caracter pasado como parametro.

    Args:
        caracter (str): caracter.

    Returns:
        str: retorna el caracter transformado.
    """

    codigo = ord(caracter)

    return chr(codigo + 32)

def verificar_minuscula(dato_ingresado: str, posicion_letra: int) -> str:
    """Verifica si el dato ingresado tiene minusculas.

    Args:
        dato_ingresado (str): cadena de texto.

    Returns:
        str: retorna la cadena de texto transformada.
    """

    letra_verificada = ""

    if ord(dato_ingresado[posicion_letra]) > 96 and ord(dato_ingresado[posicion_letra]) < 123:
        letra_verificada += dato_ingresado[posicion_letra]
    else:
        letra_verificada += hacer_minuscula(dato_ingresado[posicion_letra])

    return letra_verificada

def transformar_dato(dato_ingresado: any) -> str|int:
    """Transforma el dato pasado para que sea legible.

    Args:
        dato_ingresado (any): cadena de texto o numero

    Returns:
        str|int: retorna una cadena de texto o un entero.
    """
    dato_numerico = 0
    dato_transformado = ""

    if type(dato_ingresado) == int or dato_ingresado in "0123456789":
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


def es_numero(posible_numero: str) -> int | str:
    """Si 'posible_numero' es un numero lo convierte en int,
       caso contrario lo deja como str.

    Args:
        posible_numero (str): una cadena de texto.

    Returns:
        int | str: Retorna int si 'posible_numero' es un número, caso
                   contrario retorna el dato original sin cambios.
    """
    es_numero = True
    dato = posible_numero
    n = len(dato)

    if n == 0:
        es_numero = False

    for i in dato:
        if i < "0" or i > "9":
            es_numero = False

    if es_numero:
        numero = 0
        for i in dato:
            numero = numero * 10 + (ord(i) - ord("0"))
        dato = numero

    return dato