"""
CPF: 151.193.396-89
Validação de CPF em Python
Colete a soma dos 9 primeiros digitos do CPF, multiplicando cada digito por uma contagem regressiva de 10.

Exemplo: CPF 151.193.396-89
1*10 + 5*9 + 1*8 + 1*7 + 9*6 + 3*5 + 3*4 + 9*3 + 6*2
Soma = 10 + 45 + 8 + 7 + 54 + 15 + 12 + 27 + 12 = 190
Multiplique a soma por 10 e encontre o resto da divisão por 11.
190 * 10 = 1900
1900 % 11 = 9
Se o resultado for 10 ou maior, considere como 0,contrario disso: resultado é o valor da conta. Este é o primeiro dígito verificador.
Agora, repita o processo para encontrar o segundo dígito verificador, mas agora inclua o primeiro dígito verificador na contagem.

"""
cpf=input("Digite seu CPF (apenas números): ")
cpf= [int(digito) for digito in cpf if digito.isdigit()]  # Convertendo cada caractere em inteiro e ignorando pontos e traço

nove_digitos=cpf[:9]  # Pegando os primeiros 9 dígitos

print('Nove primeiros dígitos do CPF:',nove_digitos)

contador_regressivo_1=10
resultado_digito_1=0
for digito in nove_digitos:
    resultado_digito_1+=digito*contador_regressivo_1
    contador_regressivo_1-=1
primeiro_digito_verificador=(resultado_digito_1 * 10) % 11
primeiro_digito_verificador= primeiro_digito_verificador if primeiro_digito_verificador < 10 else 0
print('Resultado do primeiro dígito verificador:',primeiro_digito_verificador)


dez_digitos=nove_digitos+[primeiro_digito_verificador]  # Adicionando o primeiro dígito verificador aos 9 primeiros dígitos
contador_regressivo_2=11
resultado_digito_2=0
for digito in dez_digitos:
    resultado_digito_2+=digito*contador_regressivo_2
    contador_regressivo_2-=1
segundo_digito_verificador=(resultado_digito_2 * 10) % 11
segundo_digito_verificador= segundo_digito_verificador if segundo_digito_verificador < 10 else 0
print('Resultado do segundo dígito verificador:',segundo_digito_verificador)

cpf_calculado=nove_digitos+[primeiro_digito_verificador,segundo_digito_verificador]
if cpf_calculado==cpf:
    print('CPF válido!')
else:
    print('CPF inválido!')



    
    
    
        