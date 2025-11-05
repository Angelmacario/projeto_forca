# Main do jogo da forca
from palavras import escolher_palavra
from logica import mostrar_palavra, verificar_letra, verificar_vitoria  
from utils import limpar_tela, exibir_titulo

# Função principal do jogo
def main():
    palavras = escolher_palavra()
    letras_certas = set() # definir conjunto vazio das palavras
    letras_erradas = set() # 
    tentativas = 6
