import re
from datetime import datetime, time
import matplotlib.colors as mcolors


def name_validator(name, message):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)


def family_validator(family, message):
    if type(family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", family):
        return family
    else:
        raise ValueError(message)


def phone_validator(phone_number, massage):
    if type(phone_number) == str and re.match(r"(09|\+989)\d{9}", phone_number):
        return phone_number
    else:
        raise ValueError(massage)


def address_validator(address, message):
    if type(address) == str and re.match(r"^[a-zA-Z\s]{5,}$", address):
        return address
    else:
        raise ValueError(message)


def age_validator(age, message):
    if type(age) == str and re.match(r"^\d{1,2}$", age) and 0 <= int(age) <= 150:
        return age
    else:
        raise ValueError(message)


# def price_validator(price, message):
#     if type(price) == str and 0 <= int(price):
#         return price
#     else:
#         raise ValueError(message)


def label_validator(label, message):
    if type(label) == str and re.match(r"^[a-zA-Z\s.\-_\d]{3,30}$", label):
        return label
    else:
        raise ValueError(message)


def price_validator(price, message="Invalid price"):
    # بررسی None یا رشته خالی
    if price is None or str(price).strip() == "":
        raise ValueError(message)

    try:
        # تبدیل به float
        value = float(str(price).strip())
    except (ValueError, TypeError):
        raise ValueError(message)

    # بررسی مثبت بودن (اگر صفر هم مجاز است: value >= 0)
    if value < 0:
        raise ValueError(message)

    return value


def quantity_validator(quantity, message):
    if type(quantity) == int and quantity > 0:
        return quantity

    else:
        raise ValueError(message)


def national_id_validator(national_id, message):
    if type(national_id) == str and re.match(r"\d{3}-?\d{6}-?\d", national_id):
        return national_id
    else:
        raise ValueError(message)


def postal_code_validator(postal_code, message):
    if type(postal_code) == str and re.match(r"\d{5}-?\d{5}", postal_code):
        return postal_code
    else:
        raise ValueError(message)


def gmail_validator(gmail, message):
    if type(gmail) == str and re.match(r"[\w.]+@(gmail|yahoo)\.com", gmail):
        return gmail
    else:
        raise ValueError(message)


def type_validator(type):
    if type(type) == str and re.match(r"^[a-zA-Z\s]{3,30}$", type):
        return type
    else:
        raise ValueError("Invalid type !!!")


def amount_validator(amount):
    if type(amount) == int and amount > 0:
        return amount
    else:
        raise ValueError("Invalid amount !!!")


def time_validator(time, message):
    try:
        if type(time) == datetime:
            return datetime.strptime(time, "%H:%M ").time()
    except:
        raise ValueError(message)


def date_validator(date, message):
    try:
        if type(date) == str:
            return datetime.strptime(date, "%Y-%m-%d").date()
    except:
        raise ValueError(message)


def title_pay_validator(title_pay, message):
    if title_pay in ["card", "active", "invested"]:
        return title_pay
    else:
        raise ValueError(message)


def id_validator(account_id, message):
    if type(account_id) == str and re.match(r"^\d{16}$", account_id):
        return account_id
    else:
        raise ValueError(message)


def amount_validator(amount, message):
    if type(amount) == int and amount > 0:
        return amount
    else:
        raise ValueError(message)


def username_validator(username, message):
    if type(username) == str and re.match(r"^[a-zA-Z\s]{5,}$", username):
        return username
    else:
        raise ValueError(message)


def password_validator(password, message):
    if type(password) == str and re.match(r"^[a-zA-Z\s]{5,}$", password):
        return password
    else:
        raise ValueError(message)


def day_validator(day, message):
    if type(day) == str and day in ["shanbeh", "1shanbeh", "2shanbeh", "3shanbeh", "4shanbeh", "5shanbeh", "jomeh"]:
        return day
    else:
        raise ValueError(message)


def car_year_validator(car_year, message):
    if type(car_year) == int and 2000 < car_year < 2025:
        return car_year
    else:
        raise ValueError(message)


def car_model_validator(car_model, message):
    if type(car_model) == str and re.match(r"^[a-zA-Z\s]{5,10}$", car_model):
        return car_model
    else:
        raise ValueError(message)


def plate_validator(plate, message):
    if type(plate) == str and re.match(r"^\d{2}-[a-zA-z]-\d{3}-\d{2}$", plate):
        return plate
    else:
        raise ValueError(message)


def vin_validator(vin, message):
    if type(vin) == str and re.match(r"^[A-Z\d]{16}$", vin):
        return vin
    else:
        raise ValueError(message)


def kilometer_validator(kilometer, message):
    if type(kilometer) == int and 0 <= int(kilometer):
        return kilometer
    else:
        raise ValueError(message)


def type_service_validator(type_service, message):
    if type(type_service) == str and type_service in ["pdr", "carwash", "repairs", "periodic service"]:
        return type_service
    else:
        raise ValueError(message)


def color_validator(color, message):
    if type(color) == str and color in mcolors:
        return color
    else:
        raise ValueError(message)


def id_validation(car_id, message):
    if type(car_id) == int and 0 <= car_id:
        return car_id
    else:
        return ValueError(message)
