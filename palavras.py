# Gera Lista de palavras para o jogo
import random

# Escolhe uma palavra aleatória da lista
def escolher_palavra():
    lista_palavras = ["python", "java", "kotlin", "javascript", "ruby", "swift", "html", "css", "react", "angular"]
    #random.choice escolhe um elemento aleatório da lista
    return random.choice(lista_palavras)