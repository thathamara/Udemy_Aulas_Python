"""
Desempacotamento em chamadas de metodos e funçoes
Em Python, o desempacotamento permite que você passe elementos de uma lista ou tupla como argumentos separados para uma função ou método. 
Isso é feito usando o operador * para listas ou tuplas, e ** para dicionários. 

Exemplo com listas:

def soma(a, b, c):
    return a + b + c
numeros = [1, 2, 3]
resultado = soma(*numeros)  # Desempacota a lista em argumentos separados
print(resultado)  # Saída: 6

Exemplo com dicionários:

def saudacao(nome, idade):
    return f"Olá, meu nome é {nome} e tenho {idade} anos."
"""
#desmpacotamento ele retira os colchetes ou chaves de listas,tuplas ou dicionários

lista=['maria','joão',1,2,3,'pedro']
a,b,*_,c=lista
print(a,b,c)
#Nesse exemplo usamos o desempacotamento com o operador * para ignorar os elementos do meio da lista.