import json
import requests


class Custom:
    var1 = "value1"

    @classmethod
    def set_custom_parameter(cls, string_json):
        response = json.loads(string_json)
        response["custom"] = cls.var1
        return response

    @classmethod
    def porcess_json(cls, string_json):
        response = json.loads(string_json)
        return response

    @classmethod
    def addition(cls, json_input):
        return json_input["primer_numero"] + json_input["segundo_numero"]

    @classmethod
    def check_clients(cls, index):
        url = 'https://alexander_sas/clientes'
        data = {'id': index}
        answer = ""

        response = requests.post(url, data=data)

        if response.json()["Respuesta"] == 0:
            answer = "No hay registros"
        else:
            answer = "Si hay registros"

        return answer
