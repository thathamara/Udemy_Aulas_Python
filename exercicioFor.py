"""
     Faça um jogo para o usuario advinhar qual 
     a palavra secreta.
     -Vc vai propor uma plavra secreta 
     qualquer e vai dar a possibilidade para
     o usuario digitar apenas 1 letra.
     -Quando o usuario digitar uma letra,vc
     vai conferir se a letra digitada esta 
     na palavra secreta.
     -Se a letra digitada estiver na palvra;exiba a letra;
     -Se a letra nao estiver na palavra;exiba *
     Faça a contagem de tentativas do seu 
     usuario.
     
"""
palavra = "Atum".lower()
acertos = ""

while True:
    letra_digitada = input("Digite uma letra: ").lower()

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue

    if letra_digitada in palavra:
        print("Acertou!")
        acertos += letra_digitada
    else:
        print("Errou!")

    # Mostra como está a palavra até agora
    exibicao = ""
    for letra in palavra:
        if letra in acertos:
            exibicao += letra
        else:
            exibicao += "*"

    print(exibicao)
    print()  # linha em branco

    # VERIFICA SE GANHOU
    if exibicao == palavra:
        print("Parabéns! Você descobriu a palavra!")
        break
    
    
