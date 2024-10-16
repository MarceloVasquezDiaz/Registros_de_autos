import csv

class Vehiculo:
    '''
    Clase de categoria vehiculo contiene marca, modelo y numero de ruedas, ademas de funciones get y set
    
    Atributos
    marca(str): Indica la marca del vehículo
    modelo(str): Indica el modelo del vehículo
    numero_ruedas(int): Indica el número de ruedas del vehículo
    
    Metodos
    get_marca(): Obtines la marca
    get_modelo(): Obtines el modelo
    get_numero_ruedas(): Obtines el n° de ruedas
    set_marca(valor: str): Modifica la marca
    set_modelo(valor: str): Modifica el modelo
    set_numero_ruedas(valor: int): Modifica el n° de ruedas
    imprimir_datos(): Imprime los datos de la clase
    leer_csv(ubicación: str): Lee un archivo csv
    escribir_csv(ubicación: str): Escribe un apendice del archivo csv
    '''
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
    
    # Permiten obtener los valores del objeto
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_numero_ruedas(self):
        return self.numero_ruedas
    
    # Permiten modificar los valores del objeto
    def set_marca(self, valor):
        self.marca = valor
    def set_modelo(self, valor):
        self.modelo = valor
    def set_numero_ruedas(self, valor):
        self.numero_ruedas = valor
    
    # Imprime información
    def imprimir_datos(self):
        print(f'Datos: Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas', end='')
    
    # Lectura de CSV
    def leer_csv(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as data:
            lector = csv.reader(data, delimiter = ',')
            for row in lector:
                print(row)
    
    # Escritura de CSV
    def escribir_csv(self, archivo):
        nombre_datos = str(type(self))
        datos = str(self.__dict__)
        with open(archivo, 'a', newline='') as data:
            escritor = csv.writer(data)
            escritor.writerow([nombre_datos, datos])

class Automovil(Vehiculo):
    '''
    Clase Automovil hija de Vehiculo.
    Añade velocidad y cilindraje
    
    Atributos
    marca(str): Indica la marca del vehículo
    modelo(str): Indica el modelo del vehículo
    numero_ruedas(int): Indica el número de ruedas del vehículo
    velocidad(int): Indica la velocidad del automovil
    cilindraje(int): Indica el cilindraje del automovil
    
    Metodos
    get_marca(): Obtines la marca
    get_modelo(): Obtines el modelo
    get_numero_ruedas(): Obtines el n° de ruedas
    get_velocidad(): Obtines la velocidad
    get_cilindraje(): Obtines el cilindraje
    set_marca(valor: str): Modifica la marca
    set_modelo(valor: str): Modifica el modelo
    set_numero_ruedas(valor: int): Modifica el n° de ruedas
    set_velocidad(valor: int): Modifica la velocidad
    set_cilindraje(valor: int): Modifica el cilindraje
    imprimir_datos(): Imprime los datos de la clase
    leer_csv(ubicación: str): Lee un archivo csv
    escribir_csv(ubicación: str): Escribe un apendice del archivo csv
    '''
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def get_velocidad(self):
        return self.velocidad
    def get_cilindraje(self):
        return self.cilindraje
    
    def set_velocidad(self, valor):
        self.velocidad = valor
    def set_cilindraje(self, valor):
        self.cilindraje = valor
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f', Velocidad {self.velocidad} Km/h, Cilindraje {self.cilindraje} cc', end='')

class Particular(Automovil):
    '''
    Clase Particula hija de Automovil.
    Añade n° de puestos
    
    Atributos
    marca(str): Indica la marca del vehículo
    modelo(str): Indica el modelo del vehículo
    numero_ruedas(int): Indica el número de ruedas del vehículo
    velocidad(int): Indica la velocidad del automovil
    cilindraje(int): Indica el cilindraje del automovil
    puesto(int): Indica el número de puestos
    
    Metodos
    get_marca(): Obtines la marca
    get_modelo(): Obtines el modelo
    get_numero_ruedas(): Obtines el n° de ruedas
    get_velocidad(): Obtines la velocidad
    get_cilindraje(): Obtines el cilindraje
    get_puesto(): Obtiene el n° de puestos
    set_marca(valor: str): Modifica la marca
    set_modelo(valor: str): Modifica el modelo
    set_numero_ruedas(valor: int): Modifica el n° de ruedas
    set_velocidad(valor: int): Modifica la velocidad
    set_cilindraje(valor: int): Modifica el cilindraje
    set_puesto(valor: int): Modifica el n° de puestos
    imprimir_datos(): Imprime los datos de la clase
    leer_csv(ubicación: str): Lee un archivo csv
    escribir_csv(ubicación: str): Escribe un apendice del archivo csv
    '''
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindraje, puesto):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindraje)
        self.puesto = puesto
        
    def get_puesto(self):
        return self.puesto
    
    def set_puesto(self, valor):
        self.puesto = valor
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f', {self.puesto} puestos')

class Carga(Automovil):
    '''
    Clase Carga hija de Automovil.
    Añade peso de carga
    
    Atributos
    marca(str): Indica la marca del vehículo
    modelo(str): Indica el modelo del vehículo
    numero_ruedas(int): Indica el número de ruedas del vehículo
    velocidad(int): Indica la velocidad del automovil
    cilindraje(int): Indica el cilindraje del automovil
    carga(int): Indica la capacidad de carga
    
    Metodos
    get_marca(): Obtines la marca
    get_modelo(): Obtines el modelo
    get_numero_ruedas(): Obtines el n° de ruedas
    get_velocidad(): Obtines la velocidad
    get_cilindraje(): Obtines el cilindraje
    get_carga(): Obtiene la carga
    set_marca(valor: str): Modifica la marca
    set_modelo(valor: str): Modifica el modelo
    set_numero_ruedas(valor: int): Modifica el n° de ruedas
    set_velocidad(valor: int): Modifica la velocidad
    set_cilindraje(valor: int): Modifica el cilindraje
    set_carga(valor: int): Modifica la carga
    imprimir_datos(): Imprime los datos de la clase
    leer_csv(ubicación: str): Lee un archivo csv
    escribir_csv(ubicación: str): Escribe un apendice del archivo csv
    '''
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindraje, carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindraje)
        self.carga = carga
        
    def get_carga(self):
        return self.carga
    
    def set_carga(self, valor):
        self.carga = valor
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f', {self.carga} Kg de carga maxima')

class Bicicleta(Vehiculo):
    '''
    Clase Bicicleta hija de la clase Vehiculo
    Añade tipo de bicicleta
    
    Atributos
    marca(str): Indica la marca del vehículo
    modelo(str): Indica el modelo del vehículo
    numero_ruedas(int): Indica el número de ruedas del vehículo
    tipo(str): Indica el tipo de bicicleta puede ser Urbana o de Carrera
    
    Metodos
    get_marca(): Obtines la marca
    get_modelo(): Obtines el modelo
    get_numero_ruedas(): Obtines el n° de ruedas
    get_tipo(): Obtines el tipo
    set_marca(valor: str): Modifica la marca
    set_modelo(valor: str): Modifica el modelo
    set_numero_ruedas(valor: int): Modifica el n° de ruedas
    set_tipo(valor: str): Modifica el tipo
    imprimir_datos(): Imprime los datos de la clase
    leer_csv(ubicación: str): Lee un archivo csv
    escribir_csv(ubicación: str): Escribe un apendice del archivo csv
    '''
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo
    
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, valor):
        self.tipo = valor
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f', Tipo {self.tipo}', end='')

class Motocicleta(Bicicleta):
    '''
    Clase Motocicleta hija de Bicicleta.
    Añade número de radios, cuadros y motor
    
    Atributos
    marca(str): Indica la marca del vehículo
    modelo(str): Indica el modelo del vehículo
    numero_ruedas(int): Indica el número de ruedas del vehículo
    tipo(str): Indica el tipo de bicicleta puede ser Urbana o de Carrera
    nro_radios(int): Indica el numero de radios
    cuadros(str): Indica los cuadros (doble cuna, multitubolar, doble viga)
    motor(str): Indica el motor (2T o 4T)
    
    Metodos
    get_marca(): Obtines la marca
    get_modelo(): Obtines el modelo
    get_numero_ruedas(): Obtines el n° de ruedas
    get_tipo(): Obtines el tipo
    get_nro_radios(): Obtine el n° de radios
    get_cuadros(): Obtienes los cuadros
    get_motor(): Obtienes el tipo de motor
    set_marca(valor: str): Modifica la marca
    set_modelo(valor: str): Modifica el modelo
    set_numero_ruedas(valor: int): Modifica el n° de ruedas
    set_tipo(valor: str): Modifica el tipo
    set_nro_radios(valor: int): Modifica el n° de radios
    set_cuadros(valor: str): Modifica los cuadros
    set_motor(valor: str): Modifica el tipo de motor
    imprimir_datos(): Imprime los datos de la clase
    leer_csv(ubicación: str): Lee un archivo csv
    escribir_csv(ubicación: str): Escribe un apendice del archivo csv
    '''
    def __init__(self, marca, modelo, numero_ruedas, tipo, nro_radios, cuadros, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadros = cuadros
        self.motor = motor
    
    def get_nro_radios(self):
        return self.nro_radios
    def get_cuadros(self):
        return self.cuadros
    def get_motor(self):
        return self.motor
    
    def set_nro_radios(self, valor):
        self.nro_radios = valor
    def set_cuadros(self, valor):
        self.cuadros = valor
    def set_motor(self, valor):
        self.motor = valor
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f', {self.nro_radios} radios, Tipo de cuadro {self.cuadros}, Tipo de motor {self.motor}')