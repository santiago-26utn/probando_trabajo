def separar_linea(linea: str, delimitador: str):
    """Separa usuario y clave manualmente recorriendo el string."""
    for i in range(len(linea)):
        if linea[i] == delimitador:
            return linea[:i], linea[i+1:]
    return linea, ""

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    usuario = input("Ingrese nuevo nombre de usuario: ").strip()
    if len(usuario) == 0:
        print("El usuario no puede estar vacío.")
        return

    
    archivo_creador = open("usuarios.csv", "a")
    archivo_creador.close()

    # Ahora leemos con seguridad
    f = open("usuarios.csv", "r")
    for linea in f:
        u, _ = separar_linea(linea.strip(), ",")
        if u == usuario:
            print("El usuario ya existe en la base de datos.")
            f.close()
            return
    f.close()

    contrasenia = input("Ingrese su contraseña: ").strip()
    if len(contrasenia) < 4:
        print("La contraseña debe tener al menos 4 caracteres.")
        return

    f = open("usuarios.csv", "a")
    f.write(usuario + "," + contrasenia + "\n")
    f.close()
    print("¡Usuario registrado con éxito!")

def iniciar_sesion() -> bool:
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Usuario: ").strip()
    contrasenia = input("Contraseña: ").strip()

    archivo_creador = open("usuarios.csv", "a")
    archivo_creador.close()

    f = open("usuarios.csv", "r")
    for linea in f:
        u, c = separar_linea(linea.strip(), ",")
        if u == usuario and c == contrasenia:
            print("¡Bienvenido, " + usuario + "!")
            f.close()
            return True
    f.close()

    print("Usuario o contraseña incorrectos.")
    return False