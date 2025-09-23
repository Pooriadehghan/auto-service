from model.da.da import DataAccess
from model.entity.user import User
from model.tools.logging import Logger


def save(name, family, phone_number, address, department):
    try:
        member = User(name, family, phone_number, address, department)
        user_da = DataAccess(User)
        user_da.save(member)
        Logger.info(f"Member {member} Saved")
        return True, member
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(user_id, name, family, phone_number, address, department):
    try:
        member = User(name, family, phone_number, address, department)
        member.id = user_id

        user_da = DataAccess(User)
        user_da.edit(member)
        Logger.info(f"Member {member} Edited")
        return True, member
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(user_id):
    try:
        user_da = DataAccess(User)
        member = user_da.remove_by_id(user_id)

        Logger.info(f"User {member} Removed")
        return True, member
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


def find_by_id(user_id):
    try:
        user_da = DataAccess(User)
        member = user_da.find_by_id(user_id)
        if member:
            Logger.info(f"User FindById {user_id}")
            return True, member
        else:
            raise ValueError("No User Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {user_id}")
        return False, f"{e}"


def find_by_family(family):
    try:
        user_da = DataAccess(User)
        member = user_da.find_by(User.family == family)
        if member:
            Logger.info(f"User FindByFamily {family}")
            return True, member
        else:
            raise ValueError("No Member Found")
    except Exception as e:
        Logger.error(f"{e} - FindByFamily {family}")
        return False, f"{e}"


def find_by_phone_number(phone_number):
    try:
        user_da = DataAccess(User)
        member = user_da.find_by(User.phone_number == phone_number)
        if member:
            Logger.info(f"User FindByPhoneNumber {phone_number}")
            return True, member
        else:
            raise ValueError("No PhoneNumber Found")
    except Exception as e:
        Logger.error(f"{e} - FindByPhoneNumber {phone_number}")
        return False, f"{e}"


def find_by_address(address):
    try:
        user_da = DataAccess(User)
        member = user_da.find_by(User.address == address)
        if member:
            Logger.info(f"User FindByAddress {address}")
            return True, member
        else:
            raise ValueError("No Address Found")
    except Exception as e:
        Logger.error(f"{e} - FindByAddress {address}")
        return False, f"{e}"


def find_by_department(department):
    try:
        user_da = DataAccess(User)
        member = user_da.find_by(User.department == department)
        if member:
            Logger.info(f"User FindByDepartment {department}")
            return True, member
        else:
            raise ValueError("No Department Found")
    except Exception as e:
        Logger.error(f"{e} - FindByDepartment {department}")
        return False, f"{e}"
