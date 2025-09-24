from model.entity import *
from model.tools.validation import *


class User(base):
    __tablename__="user"

    def __init__(self, name, family, phone_number, address, department):
        self._id = None
        self._name = name
        self._family = family
        self._phone_number = phone_number
        self._address = address
        self._department = department

    # --- id ---
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # --- name ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # --- family ---
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = value

    # --- phone_number ---
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    # --- address ---
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    # --- department ---
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    def __str__(self):
        return f"User(id={self._id}, name={self._name}, family={self._family})"
