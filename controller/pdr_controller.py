from controller import *


def add(car_id, service_description, equipment_used, salary):
    try:
        pdr = Pdr(car_id, service_description, equipment_used, salary)
        pdr_da = DataAccess(Pdr)
        pdr_da.save(pdr)
        Logger.info(f"Pdr {pdr} saved")
        return True, pdr
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, car_id, service_description, equipment_used, salary):
    try:
        pdr = Pdr(car_id, service_description, equipment_used, salary)
        pdr.id = id
        pdr_da = DataAccess(Pdr)
        pdr_da.edit(pdr)
        Logger.info(f"Pdr {pdr} Edited")
        return True, pdr
    except Exception as e:
        Logger.error(f"{e} - Not Edited")


def remove_by_id(id):
    try:
        pdr_da = DataAccess(Pdr)
        pdr = pdr_da.remove_by_id(id)
        Logger.info(f"Pdr {pdr} Removed")
        return True, pdr

    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        pdr_da = DataAccess(Pdr)
        pdr = pdr_da.find_all()
        Logger.info("Pdr FindAll")
        return True, pdr

    except Exception as e:
        Logger.error(f"{e} - FindAll")
        return False, f"{e}"
