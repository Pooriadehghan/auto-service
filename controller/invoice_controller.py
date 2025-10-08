from controller import *


def save(id, date, time, cost, pay_type):
    try:
        invoice = Invoice(id, date, time, cost, pay_type)
        invoice_da = DataAccess(Invoice)
        invoice_da.save(invoice)
        Logger.info(f"Invoice{invoice}Saved")
        return True, invoice
    except Exception as e:
        Logger.error(f"{e}-Not Saved")
        return False, f"{e}"


def edit_invoice(id, date, time, cost, pay_type):
    try:
        invoice = Invoice(id, date, time, cost, pay_type)
        invoice.id = id

        invoice_da = DataAccess(Invoice)
        invoice_da.edit(invoice)
        Logger.info(f"Invoice {invoice} Edited")
        return True, invoice
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_invoice_by_id(id):
    try:
        invoice_da = DataAccess(Invoice)
        invoice = invoice_da.remove_by_id(id)

        Logger.info(f"Invoice {invoice} Removed")
        return True, invoice
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"

def find_all():
    try:
        invoice_da = DataAccess(Invoice)
        invoice_list = invoice_da.find_all()
        Logger.info(f"Invoice FindALL")
        return True, invoice_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"


def find_by_id(id):
    try:
        invoice_da = DataAccess(Invoice)
        invoice = invoice_da.find_by_id(id)
        if invoice:
            Logger.info(f"Invoice FindById {id}")
            return True, invoice
        else:
            raise ValueError("No Invoice Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_all_invoice():
    try:
        invoice_da = DataAccess(Invoice)
        all_invoice = invoice_da.find_all()
        return all_invoice
    except Exception as e:
        return False, f"{e}"
