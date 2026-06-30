from paquete.validacion.validaciones import limpiar_texto

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
            f.close() # ¡IMPORTANTE! Cerramos antes de salir con return
            return 

    f.close() # Cerramos si terminó el bucle y no encontró al usuario

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
    print("\n--- INICIO DE SESIÓN ---")
    
    usuario = limpiar_texto(input("Usuario: "))
    contrasenia = limpiar_texto(input("Contraseña: "))
    
    creador = open("paquete/archivos/usuarios.csv", "a")
    creador.close()
        
    f = open("paquete/archivos/usuarios.csv", "r")
    for linea in f:
        linea_limpia = limpiar_texto(linea)
        u, c = separar_linea(linea_limpia, ",")
        if u == usuario and c == contrasenia:
            print("¡Bienvenido, " + usuario + "!")
            f.close() # ¡IMPORTANTE! Cerramos antes de salir con True
            return True 
                
    f.close() # Cerramos si terminó de buscar en todo el archivo y no lo encontró
    print("Usuario o contraseña incorrectos.")
    return False
