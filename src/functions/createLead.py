import requests

url = "https://api.exactspotter.com/v3/Leads"
token = "d53a044d-913a-4e82-bf85-9bb30be1d74f"

headers = {
    "Content-Type": "application/json",
    "token_exact": token,
}


def createLead(name, phone, perguntas):

    body = {
        "duplicityValidation": "true",
        "lead": {
            "name": name,
            "ddiPhone": "55",
            "phone": phone,
            "description": perguntas,
            "source": "Questionário",
        }
    }
