import csv
from datetime import datetime
from pathlib import Path

now = datetime.now()
cabecalho = ["Data", "Movidos", "Falhas"]

def cria_linha(movidos, nao_movidos):
    return[
        now.strftime("%Y-%m-%d %H:%M:%S"),
        movidos,
        nao_movidos
    ]

def salvar_historico(linha, caminho="historico.csv"):
    arquivo = Path(caminho)
    arquivo_existe = Path.exists(arquivo)
    with open(caminho, "a", newline="") as f:
        escritor = csv.writer(f)
        if not arquivo_existe:
            escritor.writerow(cabecalho)
        escritor.writerow(linha)