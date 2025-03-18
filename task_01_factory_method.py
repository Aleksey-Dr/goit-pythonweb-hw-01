from abc import ABC, abstractmethod
from typing import Protocol
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

eu_car = eu_factory.create_car("Volkswagen", "Golf")
eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")

us_car.start_engine()
us_motorcycle.start_engine()
eu_car.start_engine()
eu_motorcycle.start_engine()
