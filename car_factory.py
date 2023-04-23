from abc import ABC, abstractmethod
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

class CarFactory:
    @staticmethod
    def __int__(self):
        pass

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)