from model.entity import *
from model.tools.validation import *


class Acceptance(Base):
    __tablename__ = 'acceptance'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _car_name = Column("car_name", String(30))
    _car_model = Column("car_model", String(15))
    _car_year = Column("car_year", String(4))
    _color = Column("color", String(30))
    _plate = Column("plate", String(30))
    _vin = Column("vin", String(30))
    _owner = Column("owner", String(30))
    _owner_phone = Column("owner_phone", String(30))
    _kilometers = Column("kilometers", Integer)
    _type_service = Column("type_service", String(30))  # رادیو باتن یا چک باتن قرار میدهیم
    _date_service = Column("date_service", Date)

    def __init__(self, car_name, car_model, car_year, color, plate, vin, owner, owner_phone, kilometers, type_service,
                 date_service):
        self.id = None
        self._car_name = car_name
        self._car_model = car_model
        self._car_year = car_year
        self._color = color
        self._plate = plate
        self._vin = vin
        self._owner = owner
        self._owner_phone = owner_phone
        self._kilometers = kilometers
        self._type_service = type_service
        self._date_service = date_service

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def car_name(self):
        return self._car_name

    @car_name.setter
    def car_name(self, value):
        self._car_name = name_validator(value, "invalid car name!!!")

    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, value):
        self._car_model = car_model_validator(value, "invalid car model!!!")

    @property
    def car_year(self):
        return self._car_year

    @car_year.setter
    def car_year(self, value):
        self._car_year = car_year_validator(value, "invalid car year!!!")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = color_validator(value, "this color is not true!!!")

    @property
    def plate(self):
        return self._plate

    @plate.setter
    def plate(self, value):
        self._plate = plate_validator(value, "invalid plate!!!")

    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = vin_validator(value, "invalid  car vin!!!")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = name_validator(value, "invalid name owner!!!")

    @property
    def owner_phone(self):
        return self._owner_phone

    @owner_phone.setter
    def owner_phone(self, value):
        self._owner_phone = phone_validator(value, "invalid phone number owner!!!")

    @property
    def kilometers(self):
        return self._kilometers

    @kilometers.setter
    def kilometers(self, value):
        self._kilometers = kilometer_validator(value, "invalid kilometers!!!")

    @property
    def type_service(self):
        return self._type_service

    @type_service.setter
    def type_service(self, value):
        self._type_service = type_service_validator(value, "invalid type service!!!")

    @property
    def date_service(self):
        return self._date_service

    @date_service.setter
    def date_service(self, value):
        self._date_service = date_validator(value,"invalid date service!!!")

