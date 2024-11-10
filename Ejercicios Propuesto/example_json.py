import base64
import json
import os

name_json = 'Ejercicios Propuesto/data.json'
def get_query():
    with open(name_json,'r') as get:
        data = json.load(get)

    for d in data["person"]:
        print(f"Name: {d['name']}\nPassword: {decode_pass(d['password'])}\n")


def set_data(name,password):
    nueva_persona = {
        "name" : name,
        "password": encrypt_pass(password)
    }

    if os.path.exists(name_json):
        with open(name_json,'r') as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = {"person" : []}
    else:
        datos = {"person": []}
    
    datos["person"].append(nueva_persona)

    with open(name_json,'w') as archive_json:
        json.dump(datos,archive_json,indent=4)

def encrypt_pass(password):
    encoded = base64.b64encode(password.encode())
    return encoded.decode()

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    return decode_bytes.decode()


# set_data("Juan","JuanPedro")
# set_data("Pedro","PedroPerez")
# set_data("Leonardo","leonardo1234454")

get_query()