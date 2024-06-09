from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        pass

class Bicicleta(Vehiculo):
    def conducir(self):
        pass

class VehiculoFactory:
    @staticmethod
    def crear_vehiculo(tipo_vehiculo):
        pass


