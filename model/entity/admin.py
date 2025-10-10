from model.entity import *
from model.tools.validation import *


class Admin(Base):
    __tablename__ = 'admin'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _username = Column("username", String(30))
    _password = Column("password", String(30))

    def __init__(self, username, password):
        self.id=None
        self.username = username
        self.password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = username_validator(value, "Invalid username !!!")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = password_validator(value, "Invalid password !!!")
