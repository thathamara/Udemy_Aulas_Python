"""Aula sobre listas em Python
Listas são estruturas de dados que armazenam múltiplos valores em uma única variável.
Elas são mutáveis, ou seja, seus elementos podem ser alterados após a criação da lista.
As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.
Exemplo de criação de lista:
frutas = ["maçã", "banana", "laranja"]

Acessando elementos:
Os elementos da lista podem ser acessados usando índices, que começam em 0.
print(frutas[0])  # Saída: maçã
Modificando elementos:
Os elementos da lista podem ser modificados atribuindo um novo valor ao índice desejado.
frutas[1] = "uva"  # Agora a lista é ["maçã", "uva", "laranja"]
Adicionando elementos:
Você pode adicionar elementos a uma lista usando o método append() ou insert().
frutas.append("abacaxi")  # Adiciona ao final da lista
frutas.insert(1, "morango")  # Adiciona na posição 1
Removendo elementos:

Você pode remover elementos usando o método remove() ou pop().
frutas.remove("laranja")  # Remove o elemento "laranja"
frutas.pop(0)  # Remove o elemento na posição 0 (maçã)

Percorrendo listas:
Você pode usar loops para percorrer os elementos de uma lista.
for fruta in frutas:    
    print(fruta)
Listas aninhadas:
Listas podem conter outras listas como elementos.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])  # Saída: 2                     
Métodos úteis:
len(lista) - Retorna o número de elementos na lista.
sort() - Ordena os elementos da lista.
reverse() - Inverte a ordem dos elementos na lista.
copy() - Cria uma cópia da lista.

Exemplo completo:

"""
frutas = ["maçã", "banana", "laranja"]
print("Lista original:", frutas)
frutas.append("abacaxi")
print("Após adicionar abacaxi:", frutas)

frutas[1] = "uva"
print("Após modificar banana para uva:", frutas)    

for fruta in frutas:
    print("Fruta:", fruta)
print("Número de frutas na lista:", len(frutas))
frutas.remove("laranja")
print("Após remover laranja:", frutas)
frutas.sort()
print("Após ordenar a lista:", frutas)
frutas.reverse()
print("Após inverter a lista:", frutas)
ultimo=frutas.pop()
print("último elemento:", ultimo)   

"""
    del - Remove um elemento pelo índice ou a lista inteira.
    del frutas[0]  # Remove o elemento na posição 0
    del frutas  # Remove a lista inteira
    print(frutas)  # Isso causará um erro, pois a lista foi deletada
    
    clear() - Remove todos os elementos da lista.
    frutas.clear()  # Agora a lista está vazia  
    print(frutas)  # Saída: []
    
    extend() - Adiciona múltiplos elementos de outra lista.
    frutas.extend(["kiwi", "manga"])  # Adiciona kiwi e manga   
    print(frutas)  # Saída: ['kiwi', 'manga']
    
    insert() - Insere um elemento em uma posição específica.
    frutas.insert(1, "pera")  # Insere pera na posição 1
    print(frutas)  # Saída: ['kiwi', 'pera', 'manga']
    
    
    
"""
# lista = ['Thamara',25,1.65,True]
# for item in lista:
#     print(item)
    
#     indices=range(len(lista)) #tamanho da lista
#     for i in indices:
#         print(f'Índice {i}: {lista[i]}')
        
        
# lista= ["maçã","banana","laranja"]
# listaEnumerada= enumerate(lista)
# for item in listaEnumerada:
#     print(item)
        
"""
Faça uma lista de compras com listas
O usuario deve poder adicionar, remover e visualizar itens na lista de compras.
"""
lista_compras = []

opcao=''

while True:
    
 opcao=input("Selecione uma opção: [I]nserir item, [R]emover item, [V]isualizar ou [S]air lista: ")
    
 if opcao == 'I':
    produto = input("Digite o nome do produto para adicionar à lista de compras: ")
    lista_compras.append(produto)
    print("Lista de compras atual:", lista_compras)
 elif opcao == 'V':
    print("Lista de compras:", lista_compras)
 elif opcao == 'R':
     remover=input("Digite o nome do item que deseja remover da lista de compras: ")
     if remover in lista_compras:
      lista_compras.remove(remover)
      print(f"{remover} foi removido da lista de compras.")
 elif opcao == 'S':
      print("Saindo da lista de compras.") 
      break

    
    
    



            
            