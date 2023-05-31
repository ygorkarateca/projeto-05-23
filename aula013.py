nome = input('Digite seu nome:')
peso = float(input('Digite seu peso:'))
alt = float(input('Digite sua altura:'))
imc = peso / (alt ** 2)

print(f'{nome} - Tem IMC de = {imc:.4f}')