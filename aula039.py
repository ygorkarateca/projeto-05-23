"""
Iterando string com while
"""

nome = input('Digite um nome: ') #Iteráveis
tamanho_nome = len(nome)
print(f'{nome}, Qtd.:{tamanho_nome}')


indice = 0
novo_nome = ''
while indice < len(nome):
  letra = nome[indice]
  novo_nome += f'*{letra}'
  indice += 1

novo_nome += '*'
print(novo_nome)
