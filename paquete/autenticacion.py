from paquete.validacion.validaciones import limpiar_texto

def separar_linea(cadena: str, separador: str) -> tuple:
    """_summary_

    Args:
        cadena (str): _description_
        separador (str): _description_

    Returns:
        tuple: _description_
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
    """Registra a un usuario.
    """
    # 1. Aseguramos que el archivo exista en la carpeta 'archivos'
    creador = open("probando_trabajo/paquete/archivos/usuarios.csv", "a")
    creador.close()
    usuario = limpiar_texto(input("Ingrese el usuario a registrar: "))
    f = open("probando_trabajo/paquete/archivos/usuarios.csv", "r")



    # 2. Leemos para verificar si el usuario ya existe
    f = open("probando_trabajo/paquete/archivos/usuarios.csv", "r")
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
    f = open("probando_trabajo/paquete/archivos/usuarios.csv", "a")
    f.write(usuario + "," + contrasenia + "\n")
    f.close()
        
    print("¡Usuario registrado con éxito!")


def iniciar_sesion() -> bool:
    """Permite iniciar sesion si ingresa un usuario existente.

    Returns:
        bool: Si se ingresa un usuario existente retorna True,
            caso contrario False.
    """
    print("\n--- INICIO DE SESIÓN ---")
    
    usuario = limpiar_texto(input("Usuario: "))
    contrasenia = limpiar_texto(input("Contraseña: "))

    creador = open("probando_trabajo/paquete/archivos/usuarios.csv", "a")
    creador.close()
        
    f = open("probando_trabajo/paquete/archivos/usuarios.csv", "r")
    for linea in f:
        linea_limpia = limpiar_texto(linea)
        u, c = separar_linea(linea_limpia, ",")
        if u == usuario and c == contrasenia:
            print("¡Bienvenido, " + usuario + "!")
            f.close() 
            return True 
                
    f.close() 
    print("Usuario o contraseña incorrectos.")
    return False
