from paquete.autenticacion import iniciar_sesion, registrar_usuario
from paquete.validacion.validaciones import *
from paquete.formato import (
    mostrar_tabla_prolija, 
    gestionar_tablas, 
    ejecutar_estadisticas, 
    separar_por_comas
)
from paquete.estadistica.estadistica import *
from paquete.variables.variables import *

proyectos = {}

continuar_login = True
sistema_activa = False
while continuar_login:
    print("=" * 40)
    print("BIENVENIDO AL SISTEMA ESTADÍSTICO")
    print("=" * 40)
    print("1. Iniciar Sesión\n2. Registrarse\n3. Salir")
    opc = get_int("Ingrese una opcion numeral: ",
                  "Error, ingrese un número entre 1 y 3 ",
                  1, 3)

    match opc:
        case 1:
            if iniciar_sesion():
                sistema_activa = True      
                continuar_login = False    
        case 2:
            registrar_usuario()
        case 3:
            continuar_login = False        
        case _:
            print("Opción inválida.")

proyecto_activo = "Proyecto_Predeterminado"
while sistema_activa:
    print(f"\n[Activo: {proyecto_activo}]\n1) Proyectos\n2) Tablas\n3) Variables\n4) Mostrar\n5) Estadística\n6) Salir")
    opcion = get_int("Ingrese una opcion numeral: ",
                     "Error, ingrese un número entre 1 y 6 ",
                     1, 6)

    match opcion:
        case 1:
            nuevo_p = limpiar_texto(input("Nombre proyecto: "))
            if nuevo_p not in proyectos: 
                proyectos[nuevo_p] = {}
            print("Cambiado a: " + nuevo_p)
            proyecto_activo = nuevo_p

        case 2:
            crear_o_modificar_tabla(proyecto_activo, proyectos)
        case 3:
            modificar_variables(proyecto_activo, proyectos)

        case 4:
            mostrar_tabla(proyecto_activo, proyectos)

        case 5:
            mostrar_estadisticas(proyecto_activo, proyectos)

        case 6:
            print("Saliendo del sistema.")
            sistema_activa = False  

        case _:
            print("Opción inválida.")

