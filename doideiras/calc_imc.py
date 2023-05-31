peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
elif imc < 35:
    categoria = "Obesidade Grau 1"
elif imc < 40:
    categoria = "Obesidade Grau 2"
else:
    categoria = "Obesidade Grau 3"

print(f"O imc é: {imc:.2f}")
print("Categoria:", categoria)