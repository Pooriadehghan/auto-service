import re


def name_validator(name, message):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)

def label_validator(label,message):
    if type(label)== str and re.match(r"^[a-zA-Z\s.\-_\d]{3,30}$",label):
        return label
    else:
        raise ValueError(message)

def price_validator(price,message):
    if type(price) == int or type(price)==float and price > 0:
        return price
    else:
        raise ValueError(message)

def quantity_validator(quantity,message):
    if type(quantity)==int and quantity > 0:
        return quantity

    else:
        raise  ValueError(message)

