from model.entity import *
from model.tools.validation import *


class Pdr(Base):
    __tablename__ = 'pdrs'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _car_id = Column("car_id", Integer, ForeignKey("acceptance.id"))
    _service_description = Column("service_description", String(70))
    _equipment_used = Column("equipment_used", String(50))
    _salary = Column("salary", Float)

    acceptance = relationship("Acceptance")

    def __init__(self, car_id, service_description, equipment_used, salary):
        self.id = None
        self.car_id = car_id
        self.service_description = service_description
        self.equipment_used = equipment_used
        self.salary = salary

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        self._car_id = id_validation(value, "Car ID must be an integer")

    @property
    def service_description(self):
        return self._service_description

    @service_description.setter
    def service_description(self, value):
        self._service_description = description_validation(value, "description must be an string")

    @property
    def equipment_used(self):
        return self._equipment_used

    @equipment_used.setter
    def equipment_used(self, value):
        self._equipment_used = description_validation(value, "equipment must be an string")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = price_validator(value, "Invalid Salary !!!")

# pdr1 = Pdr("dsfsdfseee", "wdsd", 200)
