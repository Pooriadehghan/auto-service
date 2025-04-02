from controller import *


def add(name_part,label,price,quantity,salary):
    try:
        repair=Repair(name_part,label,price,quantity,salary)
        repair_da=DataAccess(Repair)
        repair_da.save(repair)
        Logger.info(f"Repair {repair} Saved")
        return True,repair

    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False,f"{e}"

def edit(id,name_part,label,price,quantity,salary):
    try:
        repair=Repair(name_part,label,price,quantity,salary)
        repair.id=id
        repair_da=DataAccess(Repair)
        repair_da.edit(repair)
        Logger.info(f"Repair {repair} Edited")
        return True,repair

    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"

def remove_by_id(id):
    try:
        repair_da=DataAccess(Repair)
        repair=repair_da.remove_by_id(id)
        Logger.info(f"Repair {repair} Removed")
        return True,repair

    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"

