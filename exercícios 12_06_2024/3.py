num1 = int(input("Digite o primeiro número: "))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

numMAIOR = num1

if (num2 > num1):
        numMAIOR= num2
if (num3 > numMAIOR):
        numMAIOR = num3

print("O número maior entre os três números é:", numMAIOR)