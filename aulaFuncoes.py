"""
Introducao a funcoes em Python
Funcoes sao blocos de codigo que realizam tarefas especificas e podem ser reutilizadas ao longo do programa.
Elas ajudam a organizar o codigo, melhorar a legibilidade e facilitar a manutencao.
Definicao de funcoes
Em Python, uma funcao e definida usando a palavra-chave 'def', seguida pelo nome da funcao e parênteses que podem conter parametros.
Exemplo:
def saudacao(nome):
    print(f"Ola, {nome}!")

"""
milho=int(input("Quantas gramas de milho voce quer estourar? "))


def estourarPipoca(milho):
    gramas_milho=milho
    print(f"Estourando {gramas_milho} gramas de pipoca!")
    print("Pipoca pronta! Aproveite seu lanche.")
    
estourarPipoca(milho)
    

# x=input("Digite o primeiro numero:")
# y=input("Digite o segundo numero:")

# def soma(x,y):
#     return x + y

# print(soma(int(x),int(y)))

"""
Escopo da funcao:
O escopo(corpo) de uma funcao refere-se ao contexto em que as variaveis e parametros sao acessiveis.
Variaveis definidas dentro de uma funcao sao locais a essa funcao e nao podem ser acessadas fora dela.
Dessa forma para ser uma variavel global deve ser declarada fora de qualquer funcao.
"""