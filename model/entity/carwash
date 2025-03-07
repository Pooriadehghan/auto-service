from sqlalchemy import Column,Integer,String
from base import Base

class Carwash(Base):
    __tablename__ = 'carwash'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _type_wash=Column("wash_type",String(30),nullable=False)
    _price=Column("price",Integer,nullable=False)

    def __init__(self,id,wash_type,price):
        self._id=id
        self._type_wash=wash_type
        self._price=price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id=value

    @property
    def type_wash(self):
        return self._type_wash

    @type_wash.setter
    def type_wash(self, value):
        self._type_wash=value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price=value
