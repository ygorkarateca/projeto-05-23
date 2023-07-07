""" Calculadora com While """

while True:
  num1 = input('Digite um número: ')
  num2 = input('Digite outro número: ')
  operador = input('Digite um operador (+ - / *): ')

  numeros_validos = None
  
  try:
    num_1_float = float(num1)
    num_2_float = float(num2)
    numeros_validos = True
  except Exception:
    numeros_validos = None

  if numeros_validos is None:
    print('Um ou ambos os números digitados são inválidos. ')
    continue
    
  operadores_permitidos = '+-/*'
  
  if operador not in operadores_permitidos:
    print('Operador inválido!')
    continue

  if len(operador) > 1:
    print('Digite apenas um operador')
    continue
  
  if operador == '+':
    print(f'Somando os {num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
  elif operador == '-':
    print(f'Subtraindo os {num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
  elif operador == '*':
    print(f'Multiplicando os {num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
  elif operador == '/':
    print(f'Dividindo os {num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
  else:
    print('Ouve algum erro!')
    
  sair = input('Quer Sair? [s]im: ').lower().startswith('s')
  print(sair)

  if sair is True:
    break
