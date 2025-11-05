#interage com o sistema operacional
import os 

#limpa a tela do terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#exibe o título do jogo
def exibir_titulo():
    print("🎯 JOGO DA FORCA 🎯")
    #aparecer uma linha abaixo do título
    print("-" * 25)