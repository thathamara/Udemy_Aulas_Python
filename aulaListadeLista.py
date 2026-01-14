"""
Listas de listas em Python
Listas de listas, ou listas aninhadas, são listas que contêm outras listas como seus elementos.
Elas são úteis para representar estruturas de dados mais complexas, como matrizes ou tabelas.
Exemplo de criação de lista de listas:

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Acessando elementos:
Os elementos em listas de listas podem ser acessados usando múltiplos índices.  
print(matriz[0][1])  # Saída: 2 (elemento da primeira lista, segunda posição)
Modificando elementos:
Os elementos podem ser modificados atribuindo um novo valor usando múltiplos índices.
matriz[1][2] = 10  

"""
matriz = [[1, 2, 3], [4, 5, 6]]
print('Matriz original:', matriz)

matriz[1][2]=10
print('Após modificar o elemento na posição [1][2]:', matriz)

#lembrando que os índices começam em 0

lista_de_pessoas=[
    ["thamara",25,"JF"],
    ["carlos",30,"SP"],
    ["ana",22,"RJ"]
]
print('Eu sou a',lista_de_pessoas[0][0],'tenho',lista_de_pessoas[0][1],'e moro em:',lista_de_pessoas[0][2])

print('Lista de pessoas:',lista_de_pessoas)

for pessoa in lista_de_pessoas:
    for atributo in pessoa:
        print(atributo) 
#Aqui e como se pessoa fosse i(linha) e atributo fosse j(coluna) de uma matriz,dessa forma 
#percorrendo todos os atributos antes de ir para a próxima pessoa.


