from model.da.da import DataAccess
from model.entity import user
from model.entity.user import User
from model.tools.logging import Logger


def save(name, family,phone_number,address,department):
    try:
        user = User(name, family,phone_number,address,department)

        user_da = DataAccess(User)
        user_da.save(user)
        Logger.info(f"Member {user} Saved")
        return True, user
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, name, family,phone_number,address,department):
    try:
        member = User(name, family,phone_number,address,department)
        member.id = id

        user_da = DataAccess(User)
        user_da.edit(user)
        Logger.info(f"Member {user} Edited")
        return True, member
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        user_da = DataAccess(User)
        user = user_da.remove_by_id(id)

        Logger.info(f"User {user} Removed")
        return True, user
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        user_da = DataAccess(User)
        user_list = user_da.find_all()
        Logger.info(f"User FindALL")
        return True, user_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def find_by_id(id):
    try:
        user_da = DataAccess(User)
        user = user_da.find_by_id(id)
        if user:
            Logger.info(f"User FindById {id}")
            return True, user
        else:
            raise ValueError("No User Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_by_family(family):
    try:
        user_da = DataAccess(User)
        user = user_da.find_by(User._family == family)
        if user:
            Logger.info(f"User FindByFamily {family}")
            return True, user
        else:
            raise ValueError("No Member Found")
    except Exception as e:
        Logger.error(f"{e} - FindByFamily {family}")
        return False

def find_by_phone_number(phone_number):
    try:
        user_da = DataAccess(User)
        user = user_da.find_by(User._phone_number == phone_number)
        if user:
            Logger.info(f"User FindByPhoneNumber {phone_number}")
            return True, user
        else:
            raise ValueError("No PhoneNumber Found")
    except Exception as e:
        Logger.error(f"{e} - FindByPhoneNumber {find_by_phone_number}")
        return False

def find_by_address(address):
    try:
        user_da = DataAccess(User)
        user = user_da.find_by(User._address == address)
        if user:
            Logger.info(f"User FindByAddress {address}")
            return True, user
        else:
            raise ValueError("No Address Found")
    except Exception as e:
        Logger.error(f"{e} - FindByAddress {find_by_address}")
        return False

def find_by_department(department):
    try:
        user_da = DataAccess(User)
        user = user_da.find_by(User._department == department)
        if user:
            Logger.info(f"User FindByDepartment {department}")
            return True, user
        else:
            raise ValueError("No Department Found")
    except Exception as e:
        Logger.error(f"{e} - FindByDepartment {find_by_department}")
        return False
