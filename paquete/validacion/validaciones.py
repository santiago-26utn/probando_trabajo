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
        init = 0
        fin = len(texto) - 1

        while init <= fin and (texto[init] == " " or texto[init] == "\n"):
            init += 1

        while fin >= init and (texto[fin] == " " or texto[fin] == "\n"):
            fin -= 1

        acumulador = ""

        for i in range(init, fin + 1):
            caracter = texto[i]

            if (caracter >= "a" and caracter <= "z") or \
               (caracter >= "A" and caracter <= "Z") or \
               caracter == " " or caracter == "\n":

                acumulador += caracter

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


def validar_rango_recursivo(valor: float, 
                            minimo: float, 
                            maximo: float) -> bool:
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


def get_float(mensaje: str, 
              mensaje_error: str, 
              minimo: int, 
              maximo: int) -> float:
    """Pide repetidamente al usuario un numero flotante entre cierto rango, 
       deja de pedir cuando el dato es correctamente ingresado.

    Args:
        mensaje (str): mensaje.
        mensaje_error (str): mensaje error.
        minimo (int): rango minimo.
        maximo (int): rango maximo.

    Returns:
        float: retorna el numero elegido dentro del rango.
    """

    numero = 0

    while True:
        dato = input(mensaje)

        es_numero = True
        puntos = 0
        decimal = False
        decimales = 0

        entero = 0
        part_dec = 0
        divisor = 1

        if len(dato) == 0:
            es_numero = False

        for caracter in dato:

            if caracter == ".":
                puntos += 1

                if puntos > 1:
                    es_numero = False

                decimal = True

            elif caracter >= "0" and caracter <= "9":

                if not decimal:
                    entero = entero * 10 + (ord(caracter) - ord("0"))
                else:
                    decimales += 1

                    if decimales > 2:
                        es_numero = False
                    else:
                        part_dec = part_dec * 10 + (ord(caracter) - ord("0"))
                        divisor *= 10

            else:
                es_numero = False

        if es_numero:
            numero = entero + part_dec / divisor
            if validar_rango(numero, minimo, maximo) == True:
                return numero
            else:
                print(mensaje_error)
        print(mensaje_error)


def get_length(mensaje: str, 
               mensaje_error: str,
               minimo: int, 
               maximo: int) -> str:
    """Pide repetidamente al usuario una cadena de texto entre cierto rango,
       deja de pedir cuando el dato es correctamente ingresado.

    Args:
        mensaje (str): mensaje.
        mensaje_error (str): mensaje error.
        minimo (int): rango minimo.
        maximo (int): rango maximo.

    Returns:
        int: retorna la cadena de texto elegida dentro del rango.
    """

    cadena = ""

    while True:
        dato = input(mensaje)
        n = len(dato)

        es_texto = True
        tiene_letras = False

        if len(dato) == 0:
            es_texto = False

        for caracter in dato:

            if (caracter >= "A" and caracter <= "Z") or \
               (caracter >= "a" and caracter <= "z") or \
               caracter == " ":

                if caracter != " ":
                    tiene_letras = True
            else:
                es_texto = False

        if es_texto and tiene_letras:
            cadena = dato

        if es_texto:
            if validar_rango(n, minimo, maximo):
                return cadena
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)




def es_numero_flotante(posible_numero: str) -> bool:
    """Determina si una cadena representa un número flotante válido.

    Args:
        posible_numero (str): cadena a validar.

    Returns:
        bool: True si es un número flotante, False en caso contrario.
    """

    es_flotante = True
    puntos = 0
    decimales = 0
    decimal = False

    if len(posible_numero) < 3:       
        es_flotante = False

    for caracter in posible_numero:

        if caracter == ".":
            puntos += 1

            if puntos > 1:
                es_flotante = False

            decimal = True

        elif caracter >= "0" and caracter <= "9":

            if decimal:
                decimales += 1

                if decimales > 2:
                    es_flotante = False

        else:
            es_flotante = False

    if puntos != 1:
        es_flotante = False

    return es_flotante


def es_numero(posible_numero: str) -> bool:
    """Verifica si 'posible_numero' es un numero, ya sea entero o decimal.

    Args:
        posible_numero (str): una cadena de texto.

    Returns:
        bool: Retorna True si es entero o flotante o False
                           caso contrario.
    """
    es_numero = True

    if es_numero_flotante(posible_numero):
        es_numero = True

    if len(posible_numero) == 0:
        es_numero = False

    for caracter in posible_numero:
        if caracter < "0" or caracter > "9":
            es_numero = False

    return es_numero


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
        aproximacion = ((indice - 1) * aproximacion + numero / 
                        (aproximacion ** (indice - 1))) / indice

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

def verificar_mayuscula(caracter_ingresado: str) -> str:
    """Verifica si el caracter ingresado tiene mayusculas.

    Args:
        dato_ingresado (str): cadena de texto.

    Returns:
        str: retorna la cadena de texto transformada.
    """

    letra_verificada = ""

    if ord(caracter_ingresado) > 64 and ord(caracter_ingresado) < 91:
        letra_verificada += caracter_ingresado
    else:
        letra_verificada += hacer_mayuscula(caracter_ingresado)

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

def verificar_minuscula(caracter_ingresado: str) -> str:
    """Verifica si el caracter ingresado tiene minusculas.

    Args:
        dato (str): cadena de texto.

    Returns:
        str: retorna el caracter de texto transformado.
    """

    letra_verificada = ""

    if ord(caracter_ingresado) > 96 and ord(caracter_ingresado) < 123:
        letra_verificada += caracter_ingresado
    else:
        letra_verificada += hacer_minuscula(caracter_ingresado)

    return letra_verificada

def transformar_texto(texto_ingresado: str) -> str:
    """Limpia el texto y lo convierte todo a minuscula,
        exceptuando la primera letra que es mayuscula.

    Args:
        texto_ingresado (str): cadena de texto

    Returns:
        str: retorna la cadena de texto transformada.
    """
    texto_limpio = limpiar_texto(texto_ingresado)
    texto_transformado = ""

    for i in range(len(texto_limpio)):
        caracter = texto_limpio[i]
        if i == 0:
            texto_transformado += verificar_mayuscula(caracter)
        elif caracter == " ":
            texto_transformado += caracter
        else:
            texto_transformado += verificar_minuscula(caracter)

    return texto_transformado
        

def transformar_dato(dato_ingresado: any) -> str | int | float:
    """Transforma el dato pasado para que sea legible y acorde a 
        su contenido.

    Args:
        dato_ingresado (any): cadena de texto o numero.

    Returns:
        str|int|float: retorna una cadena de texto o un entero o un decimal.
    """
    dato_numerico = 0
    dato_transformado = ""
    tipo_dato = es_numero(dato_ingresado)

    if tipo_dato:
        if es_numero_flotante(dato_ingresado):
            dato_numerico = float(dato_ingresado)
        else:
            dato_numerico = int(dato_ingresado)
    else:
        dato_transformado += transformar_texto(dato_ingresado)

    if tipo_dato:
        dato_retornar = dato_numerico
    else:
        dato_retornar = dato_transformado

    return dato_retornar



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