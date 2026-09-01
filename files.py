from pathlib import Path
import shutil

origem = Path.home() / "Documentos" / "pasta_teste"

for item in origem.iterdir():    
    if item.is_file():
        tipo = item.suffix
        if not tipo:
            tipo = "sem_extensao"
        tipo_nome = tipo.upper()
        tipo_nome = tipo_nome.removeprefix(".")
        destino = Path.home() / "Documentos" / "pasta_teste" / tipo_nome
        destino.mkdir(exist_ok=True)
        shutil.move(item, str(destino))
        print(f"{item.name} -> {destino.name}")
        