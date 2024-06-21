altura = float (input("Digite sua altura em metros:"))

sexo = input(
    "Digite o seu sexo: 'M' para Masculino ou 'F' para Feminino: ").upper()
while sexo != 'M' and sexo != 'F':
    sexo = input("Inválido! Tente novamente, 'M' ou 'F'':").upper()

if sexo == 'M':
    pesoIDEAL = (72.7 * altura) - 58
    print(f"Seu peso ideal é {pesoIDEAL:.2f} kg")

elif sexo == 'F':
    pesoIDEAL = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {pesoIDEAL:.2f} kg")
