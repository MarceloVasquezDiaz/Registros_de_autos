import vehiculos
import csv

def menu():
    valor = True
    while valor:
        try:
            print('Menu de gestion\n1.- Ver vehiculos \n2.- Ingresar vehiculo\n0.- Salir')
            key = int(input(''))
            match(key):
                case 0:
                    valor = False
                case 1:
                    with open('vehiculos.csv','r', encoding='utf-8') as data:
                        lector = csv.reader(data, delimiter=',')
                        for row in lector:
                            print(row)
                case 2:
                    ingresar_vehiculo()
                case _:
                    print('Ingrese solo el numero valido')
        except TypeError:
            print('Solo puede usar numeros')

def ingresar_vehiculo():
    valor = True
    while valor:
        print('¿Qué tipo de vehiculo desea ingresar?\n1.-Vehiculo Particular.\n2.-Vehiculo de Carga.\n3.-Bicileta.\n4.-Motocicleta.\n0.-Salir')
        key = int(input(''))
        match(key):
            case 0:
                valor = False
            case 1:
                marca = input('Ingrese la marca: ')
                modelo = input('Ingrese el modelo: ')
                numero_ruedas = int(input('Ingrese el N° de ruedas: '))
                velocidad = int(input('Ingrese la velocidad: '))
                cilindraje = int(input('Ingrese el cilindraje: '))
                puesto = int(input('Ingrese la cantidad de puestos: '))
                auto = vehiculos.Particular(marca, modelo, numero_ruedas, velocidad, cilindraje, puesto)
                auto.escribir_csv('vehiculos.csv')
            case 2:
                marca = input('Ingrese la marca: ')
                modelo = input('Ingrese el modelo: ')
                numero_ruedas = int(input('Ingrese el N° de ruedas: '))
                velocidad = int(input('Ingrese la velocidad: '))
                cilindraje = int(input('Ingrese el cilindraje: '))
                carga = int(input('Ingrese la cantidad de carga: '))
                auto = vehiculos.Carga(marca, modelo, numero_ruedas, velocidad, cilindraje, carga)
                auto.escribir_csv('vehiculos.csv')
            case 3:
                marca = input('Ingrese la marca: ')
                modelo = input('Ingrese el modelo: ')
                numero_ruedas = int(input('Ingrese el N° de ruedas: '))
                tipo = input('Ingrese el tipo (Urbana o Carrera): ')
                auto = vehiculos.Bicicleta(marca, modelo, numero_ruedas, tipo)
                auto.escribir_csv('vehiculos.csv')
            case 4:
                marca = input('Ingrese la marca: ')
                modelo = input('Ingrese el modelo: ')
                numero_ruedas = int(input('Ingrese el N° de ruedas: '))
                tipo = input('Ingrese el tipo (Urbana o Carrera): ')
                nro_radios = int(input('Ingrese el N° de radios: '))
                cuadros = input('Ingrese los cuadros: ')
                motor = input('Ingrese el motor: ')
                auto = vehiculos.Bicicleta(marca, modelo, numero_ruedas, tipo, nro_radios, cuadros, motor)
                auto.escribir_csv('vehiculos.csv')

menu()