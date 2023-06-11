# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Ygor'
print(nome[2])
print(nome[-1])
print('')
# Vai mostar TRUE dizendo que CONTÉM no nome
print('Yg' in nome)
print('or' in nome)
print('')

# Vai mostrar TRUE dizendo que NÃO CONTÉM no nome
print('zero' not in nome) 
print('gravit' not in nome)
print('')

# Fazendo teste com IN e NOT IN

nome = input('Digite seu nome: ')
search = input('Digite o que deseja encontrar: ')

if search in nome:
  print(
      
      f'{search}, está em {nome}'
      f'{search}, está localizado na coluna: {nome.find(search)}'
)
 
else:
  print(f'{search}, não está em{nome}')
