from model.entity import *
from model.tools.validation import *


class CarWash(Base):
    __tablename__ = "Car_Wash"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _Car_id = Column("car_id", Integer, ForeignKey("acceptance.id"))
    _price = Column("price", Integer, nullable=False)
    _type_wash = Column("type_wash", String(30), nullable=False)

    acceptance = relationship("Acceptance")

    def __init__(self, car_id, price, type_wash):
        self.id = None
        self._Car_id = car_id
        self._price = price
        self._type_wash = type_wash

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def car_id(self):
        return self._Car_id

    @car_id.setter
    def car_id(self, value):

        if type(value) == int:
            self._Car_id = value
        else:
            raise ValueError("Car ID must be an integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = price_validator(value, "Price must be a positive number")

    @property
    def type_wash(self):
        return self._type_wash

    @type_wash.setter
    def type_wash(self, value):
        self._type_wash = value
