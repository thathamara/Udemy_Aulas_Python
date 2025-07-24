#teste
print('helloow,world')
print(1+1)
"""
Doc string
isso nao e um comentario

"""
print(12,34,sep="-")
print(13,32,sep="lalala") #separador
print(type(3),type('thamara'),type(1.2),type(10==9),10==10,type(True)) #separador


#converter um tipo em outro

print(int("1"),type(int("1")))
print(float("1"),type(float("1")))
print(bool("1"),type(bool("1")))
print(bool("0"),type(bool("0")))

adicao=10+10
subtracao=10-5
mult=10*10
divisao=10/2
exponenciacao=10**2
resto=55%2
print(adicao)
print(subtracao)
print(mult)
print(divisao)
print(exponenciacao)
print(resto)

print('a'+'b'+'c')

peso=49
altura=1.60
nome='Thamara'
imc=peso/altura**2
print(nome,"tem o imc de:",imc)
linha1=f'{nome} tem o imc de: {imc:.2f}' #formatacao
print(linha1)

#todos os inputs recebe o tipo str,sendo numero ou letra,
# dessa forma e necessario conversão para int caso necessario
x=input("Qual é o resultado de uma colisão entre duas galaxias?")
print("sua resposta foi:",x)

if x=="buraco negro supermassivo":

    print("correto,voce entrou no sistema")
elif x=="explodir":
    print ("quase isso...")
else:
    print('errado,voce nao tem acesso ao sistema')

#operadores de comparaçao
maior=2>1
maior_ou_igual=2>=2
menor=1<2
menor_ou_igual=2<=2
igual='a'=='a'
diferente= 'a'!='b'
print(diferente) 

if maior>menor:
    print(maior)
else:
    print(menor)

# and/or/not/none

entrada= input('[E]ntrar [S]air:')
senha_digitada= input("senha")
senha_permitida= '123456'
if entrada == "E" and senha_digitada == senha_permitida:
    print('entrar')
elif entrada == "E" or entrada == "e" and senha_digitada == '':
    print('sem senha')
else:
    print('sair')

    #Operador logico "not" 
    #usado para inverter expressoes
    #not True=False
    #not False=True
    print(not True)
    
    #in  esta entre
    #not in não esta entre

    nome='Thamara'
    print(nome[2])
    print('Tha' in nome)
print('mara' not in nome) 

nome=input('Digite seu nome: ')
encontrar= input('Digite oq deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

    #interpolação de strings

    nome='Thamara'
    preco=1000.11
    variavel='%s,o preço e R$%.2f' % (nome,preco)
    print(variavel)
    print(len(variavel))


    #try-> tentar executar o codigo
#except -> ocorreu algum erro ao tentar executar

numero= input('Vou dobrar o numero que vc digitar: ')

numeroInt=int(numero)
print(f'O dobro de {numero} e {numeroInt*2}')

try:
    print(f'O dobro de {numero} e {numero*2}')
except:
    print('isso nao e um numero')

#CONSTANTE = 'Variaveis' que nao vao mudar
