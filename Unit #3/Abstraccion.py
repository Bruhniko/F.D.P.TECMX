from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass

class Poder(Vehiculo):
    pass

# Crear objetos de las clases hijas
auto1 = Auto("Lamborghini", "Huracan", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")

Poder1 = Vehiculo ("500HP","Gasolina","V8","Turbo" )
auto2 = Auto("Honda", "Civic", 2023, "Azul")
moto2 = Moto("Ducati", "Monster", 2022, "Rojo")
poder2 = Poder("600HP","Gasolina","V12","Supercharger" )
camion2 = Camion("Scania", "R500", 2021, "Gris")
poder3 = Poder("700HP","Diésel","V10","Twin-Turbo" )
auto3 = Auto("Ford", "Mustang", 2020, "Negro")
poder4 = Poder("800HP","Eléctrico","Motor Dual","Sin Turbo" )

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(Poder1)
print(auto2)
print(moto2)
print(poder2)
print(camion2)
print(poder3)
print(auto3)
print(poder4)
# Salida esperada