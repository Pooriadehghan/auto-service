from sqlalchemy import Column, Integer, String
from model.entity.base import Base
from model.tools.validation import *

class User(Base):
    __tablename__ = 'user'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _phone_number = Column("phone_number", Integer)
    _address = Column("address", String(30))
    _department = Column("department", String(30))

    def __init__(self, name, family, phone_number, address, department):
        self.id = None
        self.name = name
        self.family = family
        self.phone_number = phone_number
        self.address = address
        self.department = department

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = name_validator(value,"Invalid name !!!")

    @property
    def famiy(self):
        return self._family

    @famiy.setter
    def famiy(self, value):
        self._family = family_validator(value,"Invalid family !!!")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = phone_number_validator(value,"Invalid phone_number !!!")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = address_validator(value,"Invalid address !!!")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = name_validator(value,"Invalid department !!!")
