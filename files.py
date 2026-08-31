from pathlib import Path
import shutil

pasta = Path.home() / "Documentos" / "pasta_teste"
contagem = {}

for item in pasta.iterdir():    
    if item.is_file():
        # print(f"{item.name} -> {item.suffix}")
        tipo = item.suffix
        Path.mkdir(exist_ok=True)
        contagem[tipo] = contagem.get(tipo, 0) + 1
print(contagem)
