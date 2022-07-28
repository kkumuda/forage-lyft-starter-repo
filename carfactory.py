from battery.nubbin import Nubbin
from battery.spindler import Spindler

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(cd,lsd,cm,lsm):
        engine=CapuletEngine(cm,lsm)
        battery=Spindler(cd,lsd)
        car=Car(engine,battery)
        return car

    @staticmethod
    def create_glissade(cd,lsd,cm,lsm):
        engine=WilloughbyEngine(cm,lsm)
        battery=Spindler(cd,lsd)
        car=Car(engine,battery)
        return car

    @staticmethod
    def create_palindrome(cd,lsd,cm,lsm):
        engine=SternmanEngine(cm,lsm)
        battery=Spindler(cd,lsd)
        car=Car(engine,battery)
        return car

    @staticmethod
    def create_rorschach(cd,lsd,cm,lsm):
        engine=WilloughbyEngine(cm,lsm)
        battery=Nubbin(cd,lsd)
        car=Car(engine,battery)
        return car
    @staticmethod
    def create_thovex(cd,lsd,cm,lsm):
        engine=CapuletEngine(cm,lsm)
        battery=Nubbin(cd,lsd)
        car=Car(engine,battery)
        return car