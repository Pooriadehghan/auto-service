from controller import *


def save(id, type_wash, price):
    try:
        carwash = Carwash(id, type_wash, price)

        carwash_da = DataAccess(Carwash)
        carwash_da.save(carwash)
        Logger.info(f"Carwash{carwash}Saved")
        return True, carwash
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, type_wash, price):
    try:
        carwash = Carwash(id, type_wash, price)
        carwash.id = id
        carwash_da = DataAccess(Carwash)
        carwash_da.edit(carwash)
        Logger.info(f"Carwash{carwash}Edited")
        return True, carwash
    except Exception as e:
        Logger.error(f"{e}-Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        carwash_da = DataAccess(Carwash)
        carwash = carwash_da.remove_by_id(id)

        Logger.info(f"Carwash {carwash} Removed")
        return True, carwash
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        carwash_da = DataAccess(Carwash)
        carwash_list = carwash_da.find_all()
        Logger.info(f"Carwash FindALL")
        return True, carwash_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"


def find_by_id(id):
    try:
        carwash_da = DataAccess(Carwash)
        carwash = carwash_da.find_by_id(id)
        if carwash:
            Logger.info(f"Carwash FindById {id}")
            return True, carwash
        else:
            raise ValueError("No Carwash Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_all_carwash():
    try:
        carwash_da = DataAccess(Carwash)
        all_carwash = carwash_da.find_all()
        return all_carwash
    except Exception as e:
        return False, f"{e}"
