import re



def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-z\s]{3,13}$", name):
        return name
    else:
       raise ValueError("Name is invalid")

def model_validator(model):
    if type(model) == str and re.match(r"^[a-zA-z\s\d]{3,13}$",model):
        return model
    else:
        raise ValueError("car model is invalid")

def man_year_validator(man_year):
    if type(man_year) == str and re.match(r"^\d{4}$", man_year):
        return man_year
    else:
        raise ValueError("car year is invalid")

def pelak_validator(pelak):
    if type(pelak) == str and re.match(r"^\d{2}[a-z]\d{3}[i][r]\d{2}$", pelak):
        return pelak
    else:
        raise ValueError("car pelak is invalid")