from paquete.validaciones import limpiar_texto

def separar_linea(cadena: str, separador: str) -> tuple:

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
    print("\n--- REGISTRO DE USUARIO ---")

    usuario = limpiar_texto(input("Ingrese nuevo nombre de usuario: "))
    if len(usuario) == 0:
        print("El usuario no puede estar vacío.")
        return
    creador = open("usuarios.csv", "a")
    creador.close()

    f = open("usuarios.csv", "r")
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

    f = open("usuarios.csv", "a")
    f.write(usuario + "," + contrasenia + "\n")
    f.close()
    print("¡Usuario registrado con éxito!")

def iniciar_sesion() -> bool:
    print("\n--- INICIO DE SESIÓN ---")

    usuario = limpiar_texto(input("Usuario: "))
    contrasenia = limpiar_texto(input("Contraseña: "))

    creador = open("usuarios.csv", "a")
    creador.close()

    f = open("usuarios.csv", "r")
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