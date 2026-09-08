from pathlib import Path
import shutil
import logging
from gera_json import *
from gera_csv import *

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

origem = Path.home() / "Documentos" / "pasta_teste"


if not origem.exists():
    logging.critical(f"Pasta não encontrada: {origem}")
    exit()

def pasta_destino(item) -> Path:
    tipo = item.suffix
    if not tipo:
        tipo = "sem_extensao"
    tipo_nome = tipo.upper().removeprefix(".")
    destino = Path.home() / "Documentos" / "pasta_teste" / tipo_nome
    destino.mkdir(exist_ok=True)
    return destino

movidos = 0
nao_movidos = 0
erros = []

for item in origem.iterdir():    
    if item.is_file() and not item.name.startswith("."):
        destino = pasta_destino(item)
        try:
            shutil.move(item, str(destino))
            logging.info(f"{item.name} -> {destino.name}")
            movidos+=1
        except (PermissionError, shutil.Error, OSError) as e:
            logging.error(f"Erro ao mover {item.name}: {e}")
            erros.append(str(e))
            nao_movidos+=1


dados = montar_relatorio(movidos, nao_movidos, erros)
linha = cria_linha(movidos, nao_movidos)
salvar_historico(linha)
salvar_relatorio(dados)
logging.info(f"Arquivos movidos: {movidos}, não movidos: {nao_movidos}")

