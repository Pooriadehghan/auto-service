from controller import *


def save_Carwash(car_id, price, type_wash):
    try:
        Carwash = CarWash(car_id, price, type_wash)

        Carwash_da = DataAccess(CarWash)
        Carwash_da.save(Carwash)
        Logger.info(f"Car wash{Carwash}Saved")
        return True, Carwash
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit_Carwash(id, car_id, price, type_wash):
    try:
        Carwash = CarWash(car_id, price, type_wash)
        Carwash.id = id
        Carwash_da = DataAccess(CarWash)
        Carwash_da.edit(Carwash)
        Logger.info(f"Car wash{Carwash}Edited")
        return True, Carwash
    except Exception as e:
        Logger.error(f"{e}-Not Edited")
        return False, f"{e}"


def remove_Car_wash_by_id(id):
    try:
        da = DataAccess(CarWash)
        car_wash = da.find_by_id(id)
        if car_wash is None:
            return False, f"CarWash with id={id} not found"

        da.remove(car_wash)  # یا session.delete(carwash) اگه مستقیم کار میکنی
        return True, "Removed"
    except Exception as e:
        return False, f"{e}"


def find_all_Carwash():
    try:
        Carwash_da = DataAccess(CarWash)
        all_Carwash = Carwash_da.find_all()
        return all_Carwash
    except Exception as e:
        return False, f"{e}"


def find_Carwash_by_id(id):
    try:
        Carwash_da = DataAccess(CarWash)
        Carwash = Carwash_da.find_by_id(id)
        if Carwash:
            return True, Carwash
        else:
            raise ValueError("No Car wash Found")
    except Exception as e:
        return False, f"{e}"
