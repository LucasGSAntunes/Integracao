import json

def saveJson(data, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(data, arquivo, indent=4)

    print("Arquivo gerado com sucesso")
    return True