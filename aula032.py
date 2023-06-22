"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num = int(input('Digite um número:'))

# if num == int:
#     print('Não é inteiro')
# else:
#     print('Número não é inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

nome = str(input('Digite seu nome:'))
hora = int(input('Que horas são?'))

if hora < 0:
    print('Bom dia', nome)
    if hora >= 12:
        print('Boa tarde', nome)
else:
    print('Boa noite', nome)



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""