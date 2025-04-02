from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import create_database, database_exists, drop_database
from model.entity.base import Base
from datetime import datetime
from sqlalchemy import Table
connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)



class DataAccess:
    def __init__(self, class_name):
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.class_name = class_name

    def save(self, entity):
        #print(datetime.now(), "SAVE", entity)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def edit(self, entity):
        self.session.merge(entity)
        self.session.commit()
        return entity

    def remove(self, entity):
        entity = self.session.get(self.class_name, entity.id)
        self.session.delete(entity)
        self.session.commit()
        return entity


    def remove_by_id(self, entity_id):
        entity = self.session.get(self.class_name, entity_id)
        self.session.delete(entity)
        self.session.commit()
        return entity

    def find_all(self):
        entity_list = self.session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = self.session.get(self.class_name, id)
        return entity

    def find_by(self, find_statement):
        print(datetime.now(), "FIND", find_statement)
        entity = self.session.query(self.class_name).filter(find_statement).all()
        return entity

