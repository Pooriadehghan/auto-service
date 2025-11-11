from model.da import *
from model.entity import *

connection_string = "mysql+pymysql://root:P09378922886d@localhost:3306/auto_service"
# connection_string = "mysql+pymysql://root:root123@localhost:3306/auto_service"

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# class DataAccess:
#     def __init__(self, class_name):
#         self.class_name = class_name
#
#     def save(self, entity):
#         entity = self.session.merge(entity)
#
#         session.add(entity)
#         session.commit()
#         session.refresh(entity)
#         return entity
#
#     def edit(self, entity):
#         session.merge(entity)
#         session.commit()
#         return entity
#
#     def remove(self, entity):
#         entity = session.get(self.class_name, entity.id)
#         session.delete(entity)
#         session.commit()
#         return entity
#
#     def remove_by_id(self, entity_id):
#         entity = session.get(self.class_name, entity_id)
#         session.delete(entity)
#         session.commit()
#         return entity
#
#     def remove_owner_by_id(self, entity_id, entity_owner):
#         entity = session.get(self.class_name, entity_id, entity_owner)
#         session.delete(entity)
#         session.commit()
#         return entity
#
#     def find_all(self):
#         entity_list = session.query(self.class_name).all()
#         return entity_list
#
#     def find_by_id(self, id):
#         entity = session.get(self.class_name, id)
#         return entity
#
#     def find_by(self, find_statement):
#         entity = session.query(self.class_name).filter(find_statement).all()
#         return entity
#

class DataAccess:
    def __init__(self, class_name):
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.class_name = class_name

    def save(self, entity):
        # print(datetime.now(), "SAVE", entity)
        entity = self.session.merge(entity)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def edit(self, entity):
        self.session.merge(entity)
        self.session.commit()
        return entity

    def remove(self, entity):
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