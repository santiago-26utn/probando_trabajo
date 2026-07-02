from paquete.validacion.validaciones import limpiar_texto

def separar_linea(cadena: str, separador: str) -> tuple:
    """Separa una cadena en dos partes (usuario y contraseña)

    Recorre la cadena carácter por carácter: todo lo que aparece antes
    del separador se acumula como usuario, y todo lo que aparece
    después se acumula como contraseña. El separador en sí no se
    incluye en ninguna de las dos partes.

    Args:
        cadena (str): La línea de texto a separar (por ejemplo,
            "juan,1234").
        separador (str): El carácter que divide ambas partes (por
            ejemplo, ",").

    Returns:
        tuple: Una tupla (usuario, contrasenia) con ambos valores ya
            limpios mediante limpiar_texto.
    """
    usuario = ""
    contrasenia = ""
    encontro_separador = False

    for i in range(len(cadena)):
        if cadena[i] == separador and not encontro_separador:
            encontro_separador = True
        else:
            if not encontro_separador:
                usuario += cadena[i]
            else:
                contrasenia += cadena[i]

    return limpiar_texto(usuario), limpiar_texto(contrasenia)


def registrar_usuario():
    """Registra un nuevo usuario en el archivo usuarios.csv.

    Solicita un nombre de usuario y verifica que no exista ya en el
    archivo. Si no existe, solicita una contraseña de al menos 4
    caracteres y guarda el nuevo usuario en el archivo con el formato
    "usuario,contrasenia".

    Si el usuario ya existe, o si la contraseña no cumple con el
    largo mínimo, se informa por consola y la función termina sin
    registrar nada.

    Returns:
        None
    """
    # 1. Aseguramos que el archivo exista en la carpeta 'archivos'
    creador = open("paquete/archivos/usuarios.csv", "a")
    creador.close()
    usuario = limpiar_texto(input("Ingrese el usuario a registrar: "))
    f = open("paquete/archivos/usuarios.csv", "r")

    # 2. Leemos para verificar si el usuario ya existe
    f = open("paquete/archivos/usuarios.csv", "r")
    for linea in f:
        linea_limpia = limpiar_texto(linea)
        u, _ = separar_linea(linea_limpia, ",")
        if u == usuario:
            print("El usuario ya existe en la base de datos.")
            f.close() 
            return 

    f.close() 

    contrasenia = limpiar_texto(input("Ingrese su contraseña: "))
    if len(contrasenia) < 4:
        print("La contraseña debe tener al menos 4 caracteres.")
        return

    # 3. Guardamos el nuevo usuario en la carpeta 'archivos'
    f = open("paquete/archivos/usuarios.csv", "a")
    f.write(usuario + "," + contrasenia + "\n")
    f.close()

    print("¡Usuario registrado con éxito!")


def iniciar_sesion() -> bool:
    """Permite iniciar sesión si ingresa un usuario existente.

    Solicita usuario y contraseña por teclado, y los compara contra
    los registros guardados en usuarios.csv. Si encuentra una línea
    donde ambos coinciden, informa que el inicio de sesión fue
    exitoso; en caso contrario, informa que los datos son
    incorrectos.

    Returns:
        bool: Si se ingresa un usuario existente retorna True,
            caso contrario False.
    """
    print("\n--- INICIO DE SESIÓN ---")

    usuario = limpiar_texto(input("Usuario: "))
    contrasenia = limpiar_texto(input("Contraseña: "))
    verificado = False

    creador = open("paquete/archivos/usuarios.csv", "a")
    creador.close()

    f = open("paquete/archivos/usuarios.csv", "r")
    for linea in f:
        linea_limpia = limpiar_texto(linea)
        u, c = separar_linea(linea_limpia, ",")

        if u == usuario and c == contrasenia:
            print("¡Bienvenido, " + usuario + "!")
            verificado = True

    f.close()

    if verificado == False:
        print("Usuario o contraseña incorrectos.")

    return verificado
