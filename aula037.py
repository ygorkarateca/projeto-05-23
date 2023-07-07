"""
Repetições
while (enquanto)
Executra uma ação enquanto uma condição for verdade
Loop infinito -> Quando um código não tem fim
"""

contador = 0
while contador < 100:
  contador += 1
  
  if contador == 6:
    print('não vou mostar o', contador)
    continue

  if contador >= 10 and contador <= 27:
    print('não vou mostar o', contador)
    continue
    
  print(contador)
  
  if contador == 40:
    break
    
print('Acabou')
