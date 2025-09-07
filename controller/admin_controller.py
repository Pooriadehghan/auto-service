from model.da.da import DataAccess
from model.entity import admin
from model.entity.admin import Admin
from model.tools.logging import Logger


def save(username,password):
    try:
        admin = Admin(username,password)

        admin_da = DataAccess(Admin)
        admin_da.save(admin)
        Logger.info(f"Member {admin} Saved")
        return True, admin
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id,username,password):
    try:
        member = Admin(username,password)
        member.id = id

        admin = DataAccess(Admin)
        admin.edit(admin)
        Logger.info(f"Member {admin} Edited")
        return True, member
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        admin = DataAccess(Admin)
        admin = admin.remove_by_id(id)

        Logger.info(f"Admin {admin} Removed")
        return True, admin
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        admin_da = DataAccess()
        admin_list = admin_da.find_all()
        Logger.info(f"Admin FindALL")
        return True, admin_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def find_by_id(id):
    try:
        admin_da = DataAccess(Admin)
        admin = admin_da.find_by_id(id)
        if user:
            Logger.info(f"Admin FindById {id}")
            return True, user
        else:
            raise ValueError("No Admin Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_by_user_name(user_name):
    try:
        user_da = DataAccess(Admin)
        user = user_da.find_by(Admin._user_name == user_name)
        if admin:
            Logger.info(f"User FindByUserName {user_name}")
            return True, admin
        else:
            raise ValueError("No Member Found")
    except Exception as e:
        Logger.error(f"{e} - FindByUseName {user_name}")
        return False
