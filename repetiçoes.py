"""
Repetiçoes
while(enquanto)
Executa uma condicao enquanto for verdadeira

"""
"""
Loop infinito
condicao=True

while condicao:
    print(1)
    print(2)
    print(3)
    
"""
"""
condicao=input("Digite seu nome:")

if condicao=="thamara":
    condicao=True
else:
    condicao=False

while condicao:
    print(condicao)
    
    #break ele para o while mais proximo
   
"""
"""
contador=0

while contador<=10:
    print(contador)
    contador=contador+1
    
    print("Acabou!")
    
"""

while True:
    print("Calculadora!")
    try:
        x = int(input("Dê o primeiro número: "))
        y = int(input("Dê o segundo número: "))
        sinal = input("Operador (+, -, *, /): ")

        if sinal == "+":
            print("Resultado:", x + y)
        elif sinal == "-":
            print("Resultado:", x - y)
        elif sinal == "*":
            print("Resultado:", x * y)
        elif sinal == "/":
            print("Resultado:", x / y)
        else:
            print("Operador inválido.")

    except Exception as e:
        print("Ocorreu um erro:", e)
#.lower ou .upper
    sair = input("Quer sair? [s]im: ").lower().startswith('s')
    if sair:
        break
    
