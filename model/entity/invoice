from sqlalchemy import Column,Integer,String,Date
from base import Base

class Invoice(Base):
    __tablename__ = 'invoice'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _date= Column("date", Date, nullable=False)
    _time= Column("time", Date, nullable=False)
    _cost= Column("cost", String(30), nullable=False)
    _pay_type= Column("pay_type", String(30), nullable=False)

    def __init__(self, id, date, time, cost, pay_type):
        self.id = id
        self.date = date
        self.time = time
        self.cost = cost
        self.pay_type = pay_type

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date =value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
