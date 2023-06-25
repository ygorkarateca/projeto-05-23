from time import sleep

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número: ')


if not num.isdigit():
  print('Número não é inteiro')
else:
  num = int(num)
  
  if num % 2 == 0:
    print('Número é PAR')
  else:
    print('Número é IMPAR')
sleep(2)
print()

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

nome = str(input('Digite seu nome: '))
hora = int(input('Que horas são? '))

if hora >= 0 and hora < 11:
  print(f'Bom dia, {nome}')
elif hora >= 12 and hora < 17:
  print(f'Boa tarde, {nome}')
else:
  print(f'Boa noite, {nome}')
sleep(1)
print()


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
  print('Seu nome é curto')
elif len(nome) <=6:
  print('Seu nome é normal')
else:
  print('Seu nome é muito grande!')
  
print()
sleep(1)
print('ACABEI SEU ARROMBADO!')
