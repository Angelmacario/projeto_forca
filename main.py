# Main do jogo da forca
from palavras import escolher_palavra
from logica import mostrar_palavra, verificar_letra, verificar_vitoria  
from utils import limpar_tela, exibir_titulo

# Função principal do jogo
def main():
    palavra = escolher_palavra()
    letras_certas = set() # definir conjunto vazio das palavras
    letras_erradas = set()  
    tentativas = 6

    #cria o loop do jogo
    while tentativas > 0:
        limpar_tela()
        exibir_titulo()
        print(mostrar_palavra(palavra, letras_certas))
        print(f"\n❌ Letras erradas: {', '.join(letras_erradas)}")
        print(f"🔄 Tentativas restantes: {tentativas}")
        letra = input("\nDigite uma letra: ").lower() #deixar tudo minúsculo
        if len(letra) != 1 or not letra.isalpha(): #len = verifica se entrada é um unico caracter | isalpha = verifica se é numero ou qlqr outro caracter
            print("Por favor, digite apenas uma letra válida.")
            input("Pressione Enter para continuar...")
            continue
        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            input("Pressione Enter para continuar...")
            continue
        if verificar_letra(letra, palavra, letras_certas, letras_erradas):
            print("✅ Boa! Letra Correta!")
        else:
            print("❌ Letra Errada!")
            tentativas -= 1
        if verificar_vitoria(palavra, letras_certas):
            limpar_tela()
            exibir_titulo()
            print(f"🥳 Parabéns você acertou a palavra: {palavra}")
            break
    else:
        print("😒 Fim de Jogo! A palavra era: {palavra}")

#permite que o arquivo python
if __name__ == "__main__":
    main()
