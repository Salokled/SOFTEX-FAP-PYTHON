nome = input("Digite seu nome:")
whats = int(input("Digite o número do seu telefone Whatsapp:"))
peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))
imc = float(peso / (altura**2))
consumo_AGUA = peso*0.035

print("Nome:", nome)
print("Número de telefone Whatsapp:", whats)
print("Peso:", peso)
print("Altura:", altura)
print("Seu consumo de água diário deve ser: {:.2f} litros".format(
    consumo_AGUA))
print("Seu IMC é: {:.2f}".format(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif 30 <= imc <= 34.9:
    print("Obesidade grau 1 (leve)")
elif 35 <= imc <= 39.9:
    print("Obesidade grau 2 (moderada)")
else:
    print("Obesidade grau 3 (mórbida)")
