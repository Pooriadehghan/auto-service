from model.da.da import DataAccess
from model.entity.admin import Admin
from model.tools.logging import Logger
from typing import Tuple, Any


def save(username: str, password: str) -> Tuple[bool, Any]:
    try:
        admin = Admin(username, password)
        admin_da = DataAccess(Admin)
        admin_da.save(admin)
        Logger.info(f"Admin {admin} Saved")
        return True, admin
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, str(e)


def edit(admin_id: int, username: str, password: str) -> Tuple[bool, Any]:
    try:
        admin = Admin(username, password)
        admin.id = admin_id
        admin_da = DataAccess(Admin)
        admin_da.edit(admin)
        Logger.info(f"Admin {admin} Edited")
        return True, admin
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, str(e)


def remove_by_id(admin_id: int) -> Tuple[bool, Any]:
    try:
        admin_da = DataAccess(Admin)
        removed = admin_da.remove_by_id(admin_id)
        Logger.info(f"Admin {removed} Removed")
        return True, removed
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, str(e)


def find_all() -> Tuple[bool, Any]:
    try:
        admin_da = DataAccess(Admin)
        admin_list = admin_da.find_all()
        Logger.info("Admin FindAll")
        return True, admin_list
    except Exception as e:
        Logger.error(f"{e} - FindAll")
        return False, str(e)


def find_by_id(admin_id: int) -> Tuple[bool, Any]:
    try:
        admin_da = DataAccess(Admin)
        admin = admin_da.find_by_id(admin_id)
        if admin:
            Logger.info(f"Admin FindById {admin_id}")
            return True, admin
        else:
            raise ValueError("No Admin Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {admin_id}")
        return False, str(e)


def find_by_user_name(user_name: str) -> Tuple[bool, Any]:
    try:
        admin_da = DataAccess(Admin)
        user = admin_da.find_by(Admin.username == user_name)
        if user:
            Logger.info(f"Admin FindByUserName {user_name}")
            return True, user
        else:
            raise ValueError("No Admin Found")
    except Exception as e:
        Logger.error(f"{e} - FindByUserName {user_name}")
        return False, str(e)