"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero e par ou inpar.
Caso o usuario nao digite um numero inteiro,
informe que nao e um numero inteiro.

"""
"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito,exiba a saudação apropriada.Ex
bom dia 0-11,boa tarde 12-17,e boa noite 18-23.

"""
"""
Faça um programa que peça o primeiro nome do usuario.Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver 5 e 6 letras,escreva
"Seu nome e normal"; maior que 6 escreva "Seu nome e muito grande".

"""
"""
#Exercicio 1:

numero=int(input("Digite um número inteiro: "))
print(f"O número informado é: {numero}")

if(numero%2==0):
    print("Ele é um número par!")
else:
    print("O numero informado é impar")
    
""" 
""" 
#Exercicio 2:

horas=int(input("Que horas são? "))
print(f"A hora informada é: {horas}")

if(horas>=0 and horas<=11):
    print("Bom dia!")
elif(horas>=12 and horas<=17):
    print("Boa tarde!")
else:
    print("Boa noite!")
    
""" 
#Exercicio 3:

nome=(input("Qual é seu primeiro nome? "))
tamanho=len(nome)

if(tamanho>=0 and tamanho<=4):
    print(f"Seu nome é pequeno {nome}!")
elif(tamanho>=5 and tamanho<=6):
    print(f"Seu nome é normal {nome}!")
elif(tamanho>6):
    print(f"Seu nome é grande {nome}!")
else:
    print("Erro")
