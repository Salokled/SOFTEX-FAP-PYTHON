sexo = input("Digite 'M' ou 'F':").upper()

while sexo != 'M' and sexo != 'F':
    sexo = input("Sexo inválido, tente novamente:").upper()

if sexo == 'M':
    print("\nSexo Masculino")

elif sexo == 'F':
    print("\nSexo Feminino")
