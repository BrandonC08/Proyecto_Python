#Proyecto Aventuras "Sky Monteverde"
#Estudiantes:
#Brandon Cespedes Morales
#Danny Morales Marenco
#Sebas Acuña Canton
#Yenni Chaves Fernandez

teleferico1 = 6
teleferico2 = 6
teleferico3 = 6
totalEspacios = 18
numeroId = ""
r1 = ""

def menuPrincipal():
        print("1. Ingresar como cliente")
        print("2. Ingresar como Admin")
        print("3. Salir")
        print("Digite el numero de como desea ingresar")

def menuSecundario():
        print("A continuacion se le solicitara un usuario y una contraseña")
        print("Por favor, use el usuario: Cliente y la contraseña: 123\n")               

def menuCliente():
        print("1. Realizar alguna reservacion")
        print("2. Ver estado de facturacion")
        print("3. Salir")

def menuAdmin():
        print("Bienvenido administrador, que desea realizar hoy?")
        print("1. Ver las reservaciones de la semana y el dia con menos reserva")
        print("2. Ver La cantidad monetaria generada en la semana y el dia con menor ganancia")
        print("3. Salir")

while True:
        menuPrincipal()
        eleccion = int(input())
        while eleccion == 1:
                menuSecundario()
                user=str
                pwd=str
                while (user != 'Cliente' and pwd != "123") or (user != 'cliente' and pwd != "123"):
                        user = input("Usuario: ")
                        if user == 'cliente':
                                pwd = input("\nContraseña: ")
                                if user == "cliente" and pwd == "123":
                                        print('Bienvenido.\n')
                                else:
                                        print("No ha introducio credenciales correctas, intente nuevamente.\n")
                        else:
                                print("No ha introducido un usuario correcto, intente nuevamente\n")

                pasajero=str(input("Para empezar con la reserva, por favor, indiquenos su nombre: "))
                def saludar(pasajero):
                        print("\nBienvenido(a)", pasajero, "a Aventuras Sky Monteverde!\n")
                while True:
                        saludar(pasajero)
                        menuCliente()
                        seleccion = int(input("Ingrese la opcion que desea realizar: "))
#Modulo de reserva
                        if seleccion == 1:
                                print("Nuestro servicio cuenta con 3 telifericos con una capacidad maxima de 6 cada uno por favor tome esto en cuenta cuando realice su reservacion")
                                cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros: "))

                                
                                if cantidadPasajeros <=18:
                                        condicionPasajerosNac = int(input("Ingrese la cantidad de adultos (nacionales) en la reserva: "))
                                        if cantidadPasajeros > condicionPasajerosNac:
                                                condicionPasajerosExt = int(input("Ingrese la cantidad de adultos (extranjeros) en la reserva: "))
                                                if (condicionPasajerosNac + condicionPasajerosExt) < cantidadPasajeros:
                                                        condicionPasajerosNinn = int(input("Ingrese la cantidad de niños en la reserva: "))
                                                        if (condicionPasajerosNac + condicionPasajerosExt + condicionPasajerosNinn) < cantidadPasajeros:
                                                                condicionPasajerosAdulMay = int(input("Ingrese la cantidad de adultos mayores en la reserva: "))
                                                                if (condicionPasajerosNac + condicionPasajerosExt + condicionPasajerosNinn + condicionPasajerosAdulMay) == cantidadPasajeros:
                                                                        print("Ha seleccionado", condicionPasajerosNac, "nacionales,", condicionPasajerosExt, "extranjeros,", condicionPasajerosNinn," ninos y",condicionPasajerosAdulMay,"adultos mayores de", cantidadPasajeros, " espacios reservados.\n")
                                                                else:
                                                                        print("Ha seleccionado una cantidad erronea, por favor, intente nuevamente.")
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
                                else:
                                        print("Ha introducido una cantidad mayor a la permitida. Por favor, realizar nuevamente la reserva pero dividiendo los clientes.")

                                
                                horario = int(input("Seleccione su horario teniendo en cuenta que: 9am = 1, 10am = 2 y 11am = 3"))

                                
                                def reserva(cantidadPasajeros,totalEspacios):
                                    if cantidadPasajeros <= 0:
                                        print ("La cantidad de pasajeros no es un valor valido, favor de introducir un valor valido. ")
                                    elif totalEspacios >= cantidadPasajeros and cantidadPasajeros <= teleferico1:
                                        print("Su numero de teleferico es 1, los espacios reservados son:", cantidadPasajeros)
                                    elif cantidadPasajeros > teleferico1 and cantidadPasajeros <= teleferico1 + teleferico2:
                                         print ("La cantidad excede la capacidad de 1 teleferico, por lo que seran distribuidos. En el teleferico 1 iran: ", teleferico1, "personas.\nEn el teleferico 2 viajaran: ", cantidadPasajeros - teleferico1, "personas.")
                                    elif cantidadPasajeros > teleferico1 + teleferico2 and cantidadPasajeros <= teleferico1 + teleferico2 + teleferico3:
                                         print("La cantidad excede la capacidad de 1 teleferico, por lo que seran distribuidos. En el teleferico 1 iran: ", teleferico1, "personas.\nEn el teleferico 2 viajaran: ", teleferico2, "personas.\nY en el teleferico 3 viajaran: ", cantidadPasajeros - teleferico1 - teleferico2, "personas.")
                                    else:
                                        print ("La cantidad de pasajeros excede nuestra capacidad, favor de realizar nuevamente la gestion pero con un tope de ", teleferico1 + teleferico2 + teleferico3, " personas.")
                                reserva(cantidadPasajeros,totalEspacios)
                        elif seleccion == 2 and numeroId == "":
                                print("Error -> primero debe realizar una reservacion para poder ver la facturacion")
                                continue
                        elif seleccion == 2 and numeroId != "":
                                print("Aventuras Sky Monteverde, se complace en indicarle al cliente: ", pasajero, ", cedula :", numeroId, "factura",r1, "que su reservacion a sido creada exitosamente")
                                continue
                        elif seleccion == 3:
                                print("Usted a salido de la opcion de reserva del programa lindo dia")
                                break
#Modulo de facturacion
                        import random
                        r1 = random.randint(0,1000)
                        numeroId = int(input("Ingrese en formato numerico su numero de cedula: "))
                        print("Aventuras Sky Monteverde, se complace en indicarle al cliente: ", pasajero, ", cedula :", numeroId, "factura",r1, "que su reservacion a sido creada exitosamente")
    
# Parte final    
                if esc == 'esc':
                        print("Usted a salido de la opcion cliente del programa lindo dia")
                        break
                else:
                        print("Los datos son incorrectos por favor vuelvalo a intentar")

        while eleccion == 2:
                print("Por favor digite sus datos como administrador:")
                print("Si desea salir al menu principal digite esc si aun no desea salir digite espacio")
                esc = input()
                print("Si desea salir y ya digito esc por favor dejar vacio usuario y contraseña de lo contrario siga con su registro")
                print("Usuario: ")
                user = input()
                print("Contraseña: ")
                pwd = input()
                if user == "admin" or user == "Admin" and pwd == "321":
                        while True:
                                menuAdmin()
                                seleccion = int(input("Ingrese la opcion que desea realizar: "))
                                if seleccion == 1:
                                        print("La cantidad de reservas de la semana es # y el dia con la menor cantidad de reserva es #")
                                        continue
                                elif seleccion == 2:
                                        print("La cantidad de reservas a nivel monetario de la semana es # y el dia con la menor cantidad monetaria fue # con una cantidad de  #")
                                        continue
                                elif seleccion == 3:
                                        print("Usted a salido de la opcion de administrador del programa lindo dia")
                                        break
                if esc == 'esc':
                        print("Usted a salido de la opcion administrador del programa lindo dia")
                        break
                else: print("Datos incorrectos por favor vuelva a intentarlo")

        while eleccion == 3:
                print("Usted a salido de la opcion cliente del programa lindo dia")
                break







                



