import logging

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def loga_execucao(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Função chamada {func.__name__}")
        resultado = func(*args,**kwargs)
        logging.info(f"{func.__name__} finalizada")
        return resultado
    return wrapper

