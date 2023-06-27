num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))

if num1 > num2:
  print(f'{num1=} é maior que o {num2=}')
elif num2 > num1:
  print(f'{num2=} é maior que o {num1=}')
else:
  print("OS NÚMEROS SÃO IGUAIS!")
