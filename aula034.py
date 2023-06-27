"""
Repetições
while (enquanto)
Executra uma ação enquanto uma condição for verdade
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
  nome = input('Digite alguma palavra: ').lower()
  print(f'seu nome {nome}')

  if nome == 'sair':
    break
print('Acabou!')
