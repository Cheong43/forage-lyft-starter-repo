from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, engine, battery, model, last_service_date, last_service_mileage, current_mileage):
        self.engine = engine
        self.battery = battery
        self.model = model
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        

    @abstractmethod
    def needs_service(self):
        return bool
