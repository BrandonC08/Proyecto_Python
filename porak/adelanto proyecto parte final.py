#Proyecto Aventuras "Sky Monteverde"
#Estudiantes:
#Brandon Cespedes Morales
#Danny Morales Marenco
#Sebas Acuña Canton
#Yenni Chaves Fernandez



import copy
import json
import random
teleferico1 = 6
teleferico2 = 6
teleferico3 = 6
totalEspacios = teleferico1+teleferico2+teleferico3
numeroId = ""
r1 = ""
listaReservas = []


class SetEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class ReservaDTO():
    def __init__(self, **kwargs) -> None:
        self.IdReserva = kwargs["IdReserva"]
        self.Nombre = kwargs["Nombre"]
        # self.Apellidos = kwargs["Apellidos"]
        self.Cedula = kwargs["Cedula"]
        self.Cantidad = kwargs["Cantidad"]
        self.CantidadNacionales = kwargs["CantidadNacionales"]
        self.CantidadExtranjeros = kwargs["CantidadExtranjeros"]
        self.CantidadAdultosMayores = kwargs["CantidadAdultosMayores"]
        self.CantidadNinnos = kwargs["CantidadNinnos"]
        self.Teleferico = kwargs["Teleferico"]
        self.PrecioUnitario = kwargs["PrecioUnitario"]
        self.Fecha = kwargs["Fecha"]
        self.Hora = kwargs["Hora"]


def menuTipoPasajero():
    print("El pasajero #"+str(i)+" es una persona:")
    print("1. Adulto Nacional")
    print("2. Adulto Extranjero")
    print("3. Adulto Mayor")
    print("4. Niño")
    return int(input("Seleccione una de las opciones anteriores"))


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


def saludar(pasajero):
    print("\nBienvenido(a)", pasajero, "a Aventuras Sky Monteverde!\n")

def LeerArchivo():
    fp = open('reservas.json', 'r+', encoding='utf-8')
    return json.load(fp, object_hook=lambda d: ReservaDTO(**d))


def GuardarArchivo():
    with open('reservas.json', 'w+', encoding='utf-8') as fp:
        json.dump(listaReservas, fp, ensure_ascii=False,
                  indent=4, cls=SetEncoder)


while True:
    menuPrincipal()
    eleccion = int(input())
    while eleccion != 3:
        if eleccion == 1:
            menuSecundario()
            user = str
            pwd = str
            while user != 'Cliente' and pwd != "123" or user != 'cliente' and pwd != "123":
                print("Usuario: ")
                user = input()
                print("\nContraseña: ")
                pwd = input()
                if user != 'Cliente' and pwd != "123" or user != 'cliente' and pwd != "123":
                    print(
                        "No ha introducio credenciales correctas, intente nuevamente.\n")

            pasajero = str(
                input("Para empezar con la reserva, por favor, indiquenos su nombre: "))
            saludar(pasajero)
            menuCliente()
            seleccion = int(input("Ingrese la opcion que desea realizar: "))
            # Modulo de reserva
            while seleccion != 3:
                if seleccion == 1:
                    try:
                    
                        listaReservas = LeerArchivo()
                    except: 
                        listaReservas = []
                    print("Nuestro servicio cuenta con 3 telifericos con una capacidad maxima de 6 cada uno por favor tome esto en cuenta cuando realice su reservacion")
                    Dia = input(
                        "ingrese su fecha, fotmato de 'DD/MM/YYYY'")
                    horario = int(input(
                        "Seleccione su horario teniendo en cuenta que: \n1.9am\n1.10am\n1.11am"))
                    cantidadPasajeros = int(
                        input("Ingrese la cantidad de pasajeros: "))
                    CantidadNacionales = 0
                    CantidadExtranjeros = 0
                    CantidadAdultosMayores = 0
                    CantidadNinnos = 0
                    espaciosocupados = 0
                    espaciosTeleferico1 = 6
                    espaciosTeleferico2 = 6
                    espaciosTeleferico3 = 6
                    for reserva in listaReservas:
                        if reserva.Fecha == Dia and reserva.Hora == horario:
                            espaciosocupados = espaciosocupados+reserva.Cantidad
                            if reserva.Teleferico == 1:
                                espaciosTeleferico1 = espaciosTeleferico1-reserva.Cantidad
                            if reserva.Teleferico == 2:
                                espaciosTeleferico2 = espaciosTeleferico2-reserva.Cantidad
                            if reserva.Teleferico == 3:
                                espaciosTeleferico3 = espaciosTeleferico3-reserva.Cantidad

                    if cantidadPasajeros > (totalEspacios-espaciosocupados):
                        print(
                            "La cantidad de espacios solicitados excede la cantidad de espacios disponibles")
                    for i in range(1, cantidadPasajeros+1):
                        tipopasajero = menuTipoPasajero()
                        while tipopasajero < 1 or tipopasajero > 4:
                            print("Ha seleccionado una opcion incorrecta")
                            tipopasajero = menuTipoPasajero()
                        if tipopasajero == 1:
                            CantidadNacionales = CantidadNacionales+1
                        if tipopasajero == 2:
                            CantidadExtranjeros = CantidadExtranjeros+1
                        if tipopasajero == 3:
                            CantidadAdultosMayores = CantidadAdultosMayores+1
                        if tipopasajero == 4:
                            CantidadNinnos = CantidadNinnos+1
                    r1 = random.randint(0, 1000)
                    numeroId = int(
                        input("Ingrese en formato numerico su numero de cedula: "))
                    # print("Aventuras Sky Monteverde, se complace en indicarle al cliente: ", pasajero,
                    #   ", cedula :", numeroId, "factura", r1, "que su reservacion a sido creada exitosamente")

                    objetoReserva = ReservaDTO(
                        IdReserva=r1,
                        Nombre=pasajero,
                        Cantidad=0,
                        Cedula=numeroId,
                        CantidadNacionales=CantidadNacionales,
                        CantidadExtranjeros=CantidadExtranjeros,
                        CantidadAdultosMayores=CantidadAdultosMayores,
                        CantidadNinnos=CantidadNinnos,
                        Teleferico=1,
                        PrecioUnitario=1000,
                        Fecha=Dia,
                        Hora=horario
                    )
                   
                    objetoReserva2 = copy.deepcopy(objetoReserva)
                    objetoReserva3 = copy.deepcopy(objetoReserva)
                    if cantidadPasajeros < espaciosTeleferico1:
                        objetoReserva.Cantidad = cantidadPasajeros
                        objetoReserva.Teleferico = 1
                        cantidadPasajeros = cantidadPasajeros-cantidadPasajeros
                    if cantidadPasajeros > espaciosTeleferico1 and cantidadPasajeros > 0:
                        objetoReserva.Cantidad = espaciosTeleferico1
                        objetoReserva.Teleferico = 1
                        cantidadPasajeros = cantidadPasajeros - espaciosTeleferico1
                    if cantidadPasajeros <= espaciosTeleferico2:
                        objetoReserva2.Cantidad = cantidadPasajeros
                        objetoReserva2.Teleferico = 2
                        cantidadPasajeros = cantidadPasajeros-cantidadPasajeros
                    if cantidadPasajeros > espaciosTeleferico2 and cantidadPasajeros > 0:
                        objetoReserva2.Cantidad = espaciosTeleferico2
                        objetoReserva2.Teleferico = 2
                        cantidadPasajeros = cantidadPasajeros - espaciosTeleferico2
                    if cantidadPasajeros <= espaciosTeleferico3:
                        objetoReserva3.Cantidad = cantidadPasajeros
                        objetoReserva3.Teleferico = 3
                        cantidadPasajeros = cantidadPasajeros-cantidadPasajeros
                    if cantidadPasajeros > espaciosTeleferico3 and cantidadPasajeros > 0:
                        objetoReserva3.Cantidad = espaciosTeleferico3
                        objetoReserva3.Teleferico = 3
                        cantidadPasajeros = cantidadPasajeros - espaciosTeleferico3
                    if objetoReserva.Cantidad > 0:
                        listaReservas.append(objetoReserva)
                    if objetoReserva2.Cantidad > 0:
                        listaReservas.append(objetoReserva2)
                    if objetoReserva3.Cantidad > 0:
                        listaReservas.append(objetoReserva3)
                    GuardarArchivo()
                   



                    employeeJSONData = json.dumps(
                        listaReservas, cls=SetEncoder)
                    print(employeeJSONData)
                elif seleccion == 2 and numeroId == "":
                    print(
                        "Error -> primero debe realizar una reservacion para poder ver la facturacion")
                    continue
                elif seleccion == 2 and numeroId != "":
                    print("Aventuras Sky Monteverde, se complace en indicarle al cliente: ", pasajero,
                          ", cedula :", numeroId, "factura", r1, "que su reservacion a sido creada exitosamente")
                    continue

                menuCliente()
                seleccion = int(
                    input("Ingrese la opcion que desea realizar: "))
            # Parte final
            print("Usted a salido de la opcion cliente del programa lindo dia")
            break

        if eleccion == 2:
            print("Por favor digite sus datos como administrador:")
            print(
                "Si desea salir al menu principal digite ESC si aun no desea salir digite espacio")
            esc = input()
            print("Si desea salir y ya digito ESC por favor dejar vacio usuario y contraseña de lo contrario siga con su registro")
            print("Usuario: ")
            user = input()
            print("Contraseña: ")
            pwd = input()
            if user == "admin" or user == "Admin" and pwd == "321":
                while True:
                    menuAdmin()
                    seleccion = int(
                        input("Ingrese la opcion que desea realizar: "))
                    if seleccion == 1:
                        print(
                            "La cantidad de reservas de la semana es # y el dia con la menor cantidad de reserva es #")
                        continue
                    elif seleccion == 2:
                        print(
                            "La cantidad de reservas a nivel monetario de la semana es # y el dia con la menor cantidad monetaria fue # con una cantidad de  #")
                        continue
                    elif seleccion == 3:
                        print(
                            "Usted a salido de la opcion de administrador del programa lindo dia")
                        break
            if esc == 'esc':
                print("Usted a salido de la opcion administrador del programa lindo dia")
                break
            else:
                print("Datos incorrectos por favor vuelva a intentarlo")

    print("Usted a salido del programa lindo dia")
    break
