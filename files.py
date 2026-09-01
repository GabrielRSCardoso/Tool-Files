from pathlib import Path
import shutil

origem = Path.home() / "Documentos" / "pasta_teste"

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
            print(f"{item.name} -> {destino.name}")
        except (PermissionError, shutil.Error, OSError) as e:
            print(f"Erro ao mover {item.name}: {e}")

