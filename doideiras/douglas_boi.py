import emoji, time

print(emoji.emojize('Olá, Douglas boi, 🐂'))
nome = input('Qual seu nome?')
idade = input('Quala sua idade?')

print(f'Olá, {nome}, você tem {idade}?')

if idade >= '31':
    print(f'OK! - {nome}, Vamos continuar!')
else:
    print('Vamos continuar assim mesmo!')
time.sleep(1)

dist = int(input('Insira distância em Km: '))
velo = float(input('Insira velocidade em Km/H: '))

print(

    f'Distância percorrida é {dist}Km\n'
    f'Velocidade atingida é {velo}Km/H'
)

minutos = 60 * dist / velo
horas = minutos / 60
min_conv = (minutos - horas) * 60

print(minutos, horas, min_conv)