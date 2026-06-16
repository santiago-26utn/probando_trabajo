from paquete.autenticacion import iniciar_sesion, registrar_usuario
from paquete.validaciones import limpiar_texto, convertir_a_minuscula
from paquete.formato import (
    mostrar_tabla_prolija, 
    gestionar_tablas, 
    ejecutar_estadisticas, 
    separar_por_comas
)

proyectos = {}

def programa_principal():
    continuar_login = True
    sistema_activa = False
    while continuar_login:
        print("=" * 40)
        print("BIENVENIDO AL SISTEMA ESTADÍSTICO")
        print("=" * 40)
        print("1. Iniciar Sesión\n2. Registrarse\n3. Salir")
        opc = input("Opción: ")

        match opc:
            case "1":
                if iniciar_sesion():
                    sistema_activa = True      
                    continuar_login = False    
            case "2":
                registrar_usuario()
            case "3":
                continuar_login = False        
            case _:
                print("Opción inválida.")

    proyecto_activo = "Proyecto_Predeterminado"
    while sistema_activa:
        print(f"\n[Activo: {proyecto_activo}]\na) Proyectos\nb) Tablas\nc) Variables\nd) Mostrar\ne) Estadística\nf) Salir")
        opcion = convertir_a_minuscula(input("Opción: "))

        match opcion:
            case "a":
                nuevo_p = limpiar_texto(input("Nombre proyecto: "))
                if nuevo_p not in proyectos: 
                    proyectos[nuevo_p] = {}
                print("Cambiado a: " + nuevo_p)
                proyecto_activo = nuevo_p

            case "b" | "c":  
                gestionar_tablas(proyecto_activo, proyectos)

            case "d":
                nom_tabla = limpiar_texto(input("Tabla a visualizar: "))
                if nom_tabla in proyectos[proyecto_activo]:
                    print("¿Filtrar? (s/n)")
                    if convertir_a_minuscula(input()) == 's':
                        mostrar_tabla_prolija(proyectos[proyecto_activo][nom_tabla], separar_por_comas(input("Columnas: ")))
                    else: 
                        mostrar_tabla_prolija(proyectos[proyecto_activo][nom_tabla])
                else: 
                    print("No encontrada.")

            case "e":
                ejecutar_estadisticas(proyecto_activo, proyectos)

            case "f":
                print("Saliendo del sistema.")
                sistema_activa = False  

            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    programa_principal()