import json
from datetime import datetime

def montar_relatorio(movidos, nao_movidos, erros):
    return {
        "data_execucao": str(datetime.now()),
        "movidos": movidos,
        "falhas": nao_movidos,
        "erros": erros
    }

def salvar_relatorio(dados, caminho="relatorio.json"):
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=2)