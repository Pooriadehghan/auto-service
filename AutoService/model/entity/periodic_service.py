from model.entity import *

class PeriodicService(Base):
    __tablename__ = 'periodic_services'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name_part = Column("name_part", String(30))
    _price = Column("price", Float)
    _salary = Column("salary", Float)

    def __init__(self,name_part,price,salary):
        self.id=None
        self.name_part=name_part
        self.price=price
        self.salary=salary

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id=value

    @property
    def name_part(self):
        return self._name_part

    @name_part.setter
    def name_part(self, value):
        self._name_part=name_validator(value,"Invalid Name Part !!!")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price=price_validator(value,"Invalid Price !!!")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary=price_validator(value,"Invalid Salary !!!")