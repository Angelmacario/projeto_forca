# Gera a lógica do jogo da forca
def mostrar_palavra(palavra, letras_certas):
    # mostra a palavra com letras corretas reveladas
    return " ".join([letra if letra in letras_certas else "_" for letra in palavra])

# Verifica se a letra está na palavra
def verificar_letra(letra, palavra, letras_certas, letras_erradas):
    #verifica se a letra já foi acertada antes de adicionar
    if letra in palavra:
        letras_certas.add(letra)
        return True
    else:
        #verifica se a letra já foi errada antes de adicionar
        letras_erradas.add(letra)
        return False

# Verifica se o jogador venceu  
def verificar_vitoria(palavra, letras_certas):
    #all() retorna True se todas as letras da palavra estiverem em letras_certas
    return all(letra in letras_certas for letra in palavra)