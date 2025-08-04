"""
 WHILE: Usamos quando não sabemos exatamente quantas vezes será necessário repetir.
        O laço continua até que uma condição de parada seja atendida.
       Exemplo típico: esperar uma senha correta ser digitada.

 FOR: Usamos quando já sabemos o número de repetições, 
     ou queremos percorrer algo com tamanho definido (como listas, strings, etc).
"""

texto = "Python"

for letra in texto:
    print(letra)
    
"""
 Explicação:
 O for percorre automaticamente cada caractere da string "texto"
 A cada repetição, a variável "letra" recebe um caractere diferente da string
 Não é necessário declarar uma variável de controle manualmente,
 pois o Python gerencia isso internamente.

"""

"""
for + range
range -> range(start,stop,step(pular))

"""
numeros=range(0,10,2)

for numero in numeros:
    print(numero)