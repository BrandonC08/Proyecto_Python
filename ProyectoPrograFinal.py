#Proyecto Aventuras "Sky Monteverde"
#Estudiantes:
#Brandon Cespedes Morales
#Danny Morales Marenco
#Sebas Acuña Canton
#Yenni Chaves Fernandez

import random

teleferico1 = 6
teleferico2 = 6
teleferico3 = 6
totalEspacios = 18

reservasHorarios = [[0,0,0],[0,0,0],[0,0,0]]

teleferico1Reservado = 0
teleferico2Reservado = 0
teleferico3Reservado = 0
totalEspaciosReservados = teleferico1Reservado + teleferico2Reservado + teleferico3Reservado
numeroId = ""
r1 = ""

def menuPrincipal():
    print("1. Ingresar como cliente.")
    print("2. Ingresar como administrador.")
    print("3. Salir.")
    print("Digite el numero de como desea ingresar:")
    eleccion = int(input())
    while eleccion < 1 or eleccion > 3:
        print("Digite una opcion valida.")
        eleccion = int(input())
    if eleccion == 1:
        pasajero = solicitarUsuarioCli()
        menuCliente(pasajero)
        menuPrincipal()
    elif eleccion == 2:
        solicitarUsuarioAdm()
        menuAdmin()
        menuPrincipal()
    elif eleccion == 3:
        print("Gracias por usar el programa.")

def solicitarUsuarioAdm():
    print("A continuacion se le solicitara un usuario y una contraseña")
    print("Por favor, use el usuario: 'admin' y la contraseña: 321\n")
    user=str
    pwd=str
    while (user != "admin" or pwd != "321"):
            user = input("Usuario: ")
            if user == 'admin':
                pwd = input("\nContraseña: ")
                if pwd != "321":
                    print("No ha introducio credenciales correctas, intente nuevamente.\n")
            else:
                print("No ha introducido un usuario correcto, intente nuevamente\n")
            if user == "admin" and pwd == "321":
                print("\nBienvenido administrador, que desea realizar hoy?\n")
    

def solicitarUsuarioCli():
    print("A continuacion se le solicitara un usuario y una contraseña")
    print("Por favor, use el usuario: cliente y la contraseña: 123\n")
    user=str
    pwd=str
    while (user != 'Cliente' and pwd != "123") or (user != 'cliente' and pwd != "123"):
            user = input("Usuario: ")
            if user == 'cliente':
                    pwd = input("\nContraseña: ")
                    if pwd == "123":
                            print('Bienvenido.\n')
                    else:
                            print("No ha introducio credenciales correctas, intente nuevamente.\n")
            else:
                    print("No ha introducido un usuario correcto, intente nuevamente\n")
    pasajero=str(input("Para empezar con la reserva, por favor, indiquenos su nombre: "))
    while pasajero == "":
        pasajero = str(input("Por favor, indiquenos su nombre: "))
    print("\nBienvenido(a)", pasajero, "a Aventuras Sky Monteverde!\n")
    return pasajero

def menuCliente(pasajero):
    print("1. Realizar alguna reservacion")
    print("2. Ver estado de facturacion")
    print("3. Volver")     
    seleccion = int(input("Ingrese la opcion que desea realizar: "))
    while seleccion < 1 or seleccion > 3:
        print("Digite una opcion valida")
        seleccion = int(input())
    if seleccion == 1:
        if totalEspaciosReservados == totalEspacios:
            print("Lo sentimos, no hay espacios disponibles")
        else:
            reservacion(pasajero)
        menuCliente(pasajero)
    elif seleccion == 2:
        if numeroId == "":
            print("Error -> primero debe realizar una reservacion para poder ver la facturacion")
        else:
            print("Aventuras Sky Monteverde, se complace en indicarle al cliente: ", pasajero, ", cedula :", numeroId, "factura",r1, "que su reservacion a sido creada exitosamente")
        menuCliente(pasajero)
    elif seleccion == 3:
        print("Usted a salido de la opcion de reserva del programa lindo dia")

def reservacion(pasajero):
    print("Nuestro servicio cuenta con 3 telifericos con una capacidad maxima de 6 cada uno por favor tome esto en cuenta cuando realice su reservacion")
    horario = int(input("Seleccione su horario.\n1. 9am\n2. 10am\n3. 11am\nHorario: "))
    while horario < 1 or horario > 3:
        print("Digite una opcion valida.")
        horario = int(input())

    print("Actualmente tenemos", totalEspacios-totalEspaciosReservados, "espacios distribuidos de la siguiente manera:")
    print("Teleferico 1:", teleferico1-reservasHorarios[horario-1][0], "espacios disponibles")
    print("Teleferico 2:", teleferico2-reservasHorarios[horario-1][1], "espacios disponibles")
    print("Teleferico 3:", teleferico3-reservasHorarios[horario-1][2], "espacios disponibles")


    espaciosDisponibles = teleferico1-reservasHorarios[horario-1][0] + teleferico2-reservasHorarios[horario-1][1] + teleferico3-reservasHorarios[horario-1][2]
    cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros: "))
    while cantidadPasajeros < 1 or cantidadPasajeros > espaciosDisponibles:
        print("Digite una cantidad valida")
        cantidadPasajeros = int(input())
    condicionPasajerosNac = int(input("Ingrese la cantidad de adultos (nacionales) en la reserva: "))
    while condicionPasajerosNac < 0 or condicionPasajerosNac > cantidadPasajeros:
        print("Digite una cantidad valida")
        condicionPasajerosNac = int(input())
    if cantidadPasajeros > condicionPasajerosNac:
        condicionPasajerosExt = int(input("Ingrese la cantidad de adultos (extranjeros) en la reserva: "))
        while condicionPasajerosExt < 0 or condicionPasajerosExt + condicionPasajerosNac > cantidadPasajeros:
            print("Digite una cantidad valida")
            condicionPasajerosExt = int(input())
        if condicionPasajerosNac + condicionPasajerosExt < cantidadPasajeros:
            condicionPasajerosNinn = int(input("Ingrese la cantidad de niños en la reserva: "))
            while condicionPasajerosNinn < 0 or condicionPasajerosNinn + condicionPasajerosNac + condicionPasajerosExt > cantidadPasajeros:
                print("Digite una cantidad valida")
                condicionPasajerosNinn = int(input())
            if (condicionPasajerosNac + condicionPasajerosExt + condicionPasajerosNinn) < cantidadPasajeros:
                condicionPasajerosAdulMay = int(input("Ingrese la cantidad de adultos mayores en la reserva: "))                                               
                while condicionPasajerosAdulMay < 0 or condicionPasajerosAdulMay + condicionPasajerosNac + condicionPasajerosExt + condicionPasajerosNinn != cantidadPasajeros:
                    print("Digite una cantidad valida")
                    condicionPasajerosAdulMay = int(input())
                print("Ha seleccionado", condicionPasajerosNac, "nacionales,", condicionPasajerosExt, "extranjeros,", condicionPasajerosNinn," ninos y",condicionPasajerosAdulMay,"adultos mayores de", cantidadPasajeros, " espacios reservados.\n")
            elif (condicionPasajerosNac + condicionPasajerosExt + condicionPasajerosNinn) == cantidadPasajeros:
                print("Ha seleccionado", condicionPasajerosNac, "nacionales,", condicionPasajerosExt, "extranjeros y", condicionPasajerosNinn," ninos de", cantidadPasajeros, " espacios reservados.\n")
            else:
                print("Ha seleccionado una cantidad erronea, por favor, intente nuevamente.")
        elif (condicionPasajerosNac + condicionPasajerosExt) == cantidadPasajeros:
            print("Ha seleccionado", condicionPasajerosNac, "nacionales y", condicionPasajerosExt, "extranjeros de", cantidadPasajeros, " espacios reservados.\n")
        else:
            print("Ha seleccionado una cantidad erronea, por favor, intente nuevamente.")
    elif cantidadPasajeros == condicionPasajerosNac:
        print("Ha seleccionado", condicionPasajerosNac, "de", cantidadPasajeros,"espacios reservados.\n")
    else:
        print("Ha seleccionado", condicionPasajerosNac, "pasajeros nacionales, y excede nuestra capacidad de 18 espacios.\nPor favor reservar los excedentes en otro horario.")                          
    
    reserva = reservar(cantidadPasajeros,reservasHorarios[horario-1])
    if reserva:
        reservasHorarios[horario-1][0] += reserva[0]
        reservasHorarios[horario-1][1] += reserva[1]
        reservasHorarios[horario-1][2] += reserva[2]
        global numeroId, r1
        r1 = random.randint(0,1000)
        numeroId = int(input("Ingrese en formato numerico su numero de cedula: "))
        print("Aventuras Sky Monteverde, se complace en indicarle al cliente: ", pasajero, ", cedula :", numeroId, "factura",r1, "que su reservacion a sido creada exitosamente")
    
    

def reservar(cantidadPasajeros,totalEspacios):
    if cantidadPasajeros <= teleferico1 - totalEspacios[0]:
        print("Su numero de teleferico es 1, los espacios reservados son:", cantidadPasajeros)
        return [cantidadPasajeros,0,0]
    elif cantidadPasajeros >teleferico1 - totalEspacios[0] and cantidadPasajeros <= teleferico1 - totalEspacios[0] + teleferico2 - totalEspacios[1]:
        print ("La cantidad excede la capacidad de 1 teleferico, por lo que seran distribuidos. En el teleferico 1 iran: ", teleferico1-totalEspacios[0], "personas.\nEn el teleferico 2 viajaran: ",cantidadPasajeros- (teleferico1-totalEspacios[0]), "personas.")
        return [teleferico1-totalEspacios[0], cantidadPasajeros- (teleferico1-totalEspacios[0]), 0]
    elif cantidadPasajeros > teleferico1 - totalEspacios[0] + teleferico2 - totalEspacios[1] and cantidadPasajeros <= teleferico1 - totalEspacios[0] + teleferico2 - totalEspacios[1] + teleferico3 -totalEspacios[2]:
        print("La cantidad excede la capacidad de 1 teleferico, por lo que seran distribuidos. En el teleferico 1 iran: ", teleferico1-totalEspacios[0], "personas.\nEn el teleferico 2 viajaran: ", teleferico2 - totalEspacios[1], "personas.\nY en el teleferico 3 viajaran: ", cantidadPasajeros - (teleferico1-totalEspacios[0]) - (teleferico2 - totalEspacios[1]), "personas.")
        return [teleferico1-totalEspacios[0],teleferico2 - totalEspacios[1], cantidadPasajeros - (teleferico1-totalEspacios[0]) - (teleferico2 - totalEspacios[1])]
    else:
        print ("La cantidad de pasajeros excede nuestra capacidad, favor de realizar nuevamente la gestion pero con un tope de ",(teleferico1 - totalEspacios[0]) + (teleferico2 - totalEspacios[1]) +(teleferico3 - totalEspacios[2]), " personas.")
        return False

def menuAdmin():
    
        print("Bienvenido administrador, que desea realizar hoy?")
        print("1. Ver la disponibilidad de los telefericos por horario")
        print("2. Ver la cantidad de reservaciones por dia")
        print("3. Salir")
        seleccion = int(input("Ingrese la opcion que desea realizar: "))
        while seleccion < 1 or seleccion > 5:
            print("Por favor, digite una opcion valida")
            seleccion = int(input())
        if seleccion == 1:
            dinero(condicionPasajeros,condicionPasajerosNac,condicionPasajerosExt,condicionPasajerosAdulMay,condicionPasajerosNinn)
        elif seleccion == 2:
            print("La disponibilidad de los telefericos es de")
            print("\n9am")
            print("teleferico 1: ",teleferico1 - reservasHorarios[0][0], " espacios disponibles")
            print("teleferico 2: ",teleferico2 - reservasHorarios[0][1], " espacios disponibles")
            print("teleferico 3: ",teleferico3 - reservasHorarios[0][2], " espacios disponibles")
            print("\n10am")
            print("teleferico 1: ",teleferico1 - reservasHorarios[1][0], " espacios disponibles")
            print("teleferico 2: ",teleferico2 - reservasHorarios[1][1], " espacios disponibles")
            print("teleferico 3: ",teleferico3 - reservasHorarios[1][2], " espacios disponibles")
            print("\n11am")
            print("teleferico 1: ",teleferico1 - reservasHorarios[2][0], " espacios disponibles")
            print("teleferico 2: ",teleferico2 - reservasHorarios[2][1], " espacios disponibles")
            print("teleferico 3: ",teleferico3 - reservasHorarios[2][2], " espacios disponibles")
        elif seleccion == 3:
            print("La cantidad de reservas por dia es de: ")
            total = 0
            total += reservasHorarios[0][0] + reservasHorarios[0][1] + reservasHorarios[0][2]
            total += reservasHorarios[1][0] + reservasHorarios[1][1] + reservasHorarios[1][2]
            total += reservasHorarios[2][0] + reservasHorarios[2][1] + reservasHorarios[2][2]
            print( total, " reservas en total")
        elif seleccion == 4:
            print("Usted a salido de la opcion de administrador del programa lindo dia")
            return 0


menuPrincipal()
