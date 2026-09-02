from pathlib import Path
import shutil
import logging

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


for item in origem.iterdir():    
    if item.is_file():
        destino = pasta_destino(item)
        try:
            shutil.move(item, str(destino))
            logging.info(f"{item.name} -> {destino.name}")
        except (PermissionError, shutil.Error, OSError) as e:
            logging.error(f"Erro ao mover {item.name}: {e}")

