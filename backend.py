import requests
import json
import random
import string
import data_params
import PySimpleGUI as sg


def gen_password(stringlength):
    """ Generate a random string of fixed length """
    random_int = random.randint(1, 99)
    password_string = string.ascii_letters + string.ascii_uppercase + string.digits
    return str(random_int) + ''.join(random.choice(password_string) for i in range(stringlength))


def generate_data(num_val):
    try:
        for i in range(num_val):
            response = requests.get("https://www.slumpa.net/api")
            person = response.json()
            print(person)
            password = gen_password(6)
            name = person["name"]
            last_name = person["lastname"]
            email = "{}.{}@testmail.com".format(name.lower(), last_name.lower())
            for x in email:
                if x == "å" or x == "ä" or x == "á":
                    email = email.replace(x, "a")
                if x == "ö":
                    email = email.replace(x, "o")
                if x == "é":
                    email = email.replace(x, "e")
            data_params.personer = {
                "name": name,
                "lastname": last_name,
                "full_SSN": person["century"] + person["ssn"],
                "short_SSN": person["ssn"],
                "address": person["address"],
                "email": email,
                "password": password
            }
            data_params.final.append(data_params.personer)
    except TypeError:
        sg.popup("Incorrect value \nCannot be 0 or letters")


def save_output(path):
    try:
        f = open("{}/testdata.json".format(path), "xt")
        json.dump(data_params.final, f, indent=4, ensure_ascii=False)
        f.close()
        sg.Popup("File saved!")
    except FileExistsError:
        f = open("{}/testdata.json".format(path), "at")
        json.dump(data_params.final, f, indent=4, ensure_ascii=False)
        f.close()
        sg.Popup("File already exists! \nAdded result to existing file")


def reset():
    data_params.personer = ""
    data_params.final = []
    data_params.personer_formatted = ""
