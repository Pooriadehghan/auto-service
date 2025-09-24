from controller import *


def add(name_part, price, salary):
    try:
        periodic_service = PeriodicService(name_part, price, salary)
        periodic_service_da = DataAccess(PeriodicService)
        periodic_service_da.save(periodic_service)
        Logger.info(f"Periodic Service {periodic_service} Saved")
        return True, periodic_service

    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, name_part, price, salary):
    try:
        periodic_service = PeriodicService(name_part, price, salary)
        periodic_service.id = id
        periodic_service_da = DataAccess(PeriodicService)
        periodic_service_da.edit(periodic_service)
        Logger.info(f"Periodic Service {periodic_service} Edited")
        return True, periodic_service



    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        periodic_service_da = DataAccess(PeriodicService)
        periodic_service = periodic_service_da.remove_by_id(id)
        Logger.info(f"Periodic Service {periodic_service} Removed")
        return True, periodic_service

    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"
