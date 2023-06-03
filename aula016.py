# if /    elif    / else
# se / se não se / se não

entrada = input('Digite "entrar" ou "sair"!').lower()

if entrada == 'entrar':
  print('Acesso concedido')
elif entrada == 'sair':
  print('Acesso negado')
else:
  print('Palavra "entrar" ou "sair" não reconhecido!')
