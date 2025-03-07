from controller import *


def save(car_name, car_model, car_year, color, plate, vin, owner, owner_phone, kilometers, type_service,
         date_service):
    try:
        acceptance = Acceptance(car_name, car_model, car_year, color, plate, vin, owner, owner_phone, kilometers,
                                type_service,
                                date_service)

        acceptance_da = DataAccess(Acceptance)
        acceptance_da.save(acceptance)
        Logger.info(f"Acceptance {acceptance} Saved")
        return True, acceptance
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, car_name, car_model, car_year, color, plate, vin, owner, owner_phone, kilometers, type_service,
         date_service):
    try:
        acceptance = Acceptance(car_name, car_model, car_year, color, plate, vin, owner, owner_phone, kilometers,
                                type_service,
                                date_service)
        acceptance.id = id

        acceptance_da = DataAccess(Acceptance)
        acceptance_da.edit(acceptance)
        Logger.info(f"Acceptance {acceptance} Edited")
        return True, acceptance
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        acceptance_da = DataAccess(Acceptance)
        acceptance = acceptance_da.remove_by_id(id)

        Logger.info(f"Acceptance {acceptance} Removed")
        return True, acceptance
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def remove_owner_by_id(id, owner):
    try:
        acceptance_da = DataAccess(Acceptance)
        acceptance = acceptance_da.remove_owner_by_id(id, owner)

        Logger.info(f"Acceptance {acceptance} Removed")
        return True, acceptance
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        acceptance_da = DataAccess(Acceptance)
        acceptance_list = acceptance_da.find_all()
        Logger.info(f"Acceptance FindALL")
        return True, acceptance_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"


def find_by_id(id):
    try:
        acceptance_da = DataAccess(Acceptance)
        acceptance = acceptance_da.find_by_id(id)
        if acceptance:
            Logger.info(f"Acceptance FindById {id}")
            return True, acceptance
        else:
            raise ValueError("No Acceptance Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_by_owner(owner):
    try:
        acceptance_da = DataAccess(Acceptance)
        acceptance = acceptance_da.find_by_owner(Acceptance._owner == owner)
        if acceptance:
            Logger.info(f"Acceptance FindByFamily {owner}")
            return True, acceptance
        else:
            raise ValueError("No Acceptance Found")
    except Exception as e:
        Logger.error(f"{e} - FindByFamily {owner}")
        return False, f"{e}"
