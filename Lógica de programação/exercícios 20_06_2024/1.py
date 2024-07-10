salario = float(input("Informe seu salário R$:"))

if salario <= 280:
        percentual = 20
elif salario <= 700:
        percentual = 15
elif salario <= 1500:
        percentual = 10
else:
        percentual = 5

salarioANTERIOR = salario * (percentual / 100)
salarioNOVO = salario + salarioANTERIOR

print(f"\nO percentual de aumento para seu salário é:{percentual}%")
print(f"Salário antes do reajuste era R${salario:.2f}")
print(f"Valor incrementado ao novo salário R${salarioANTERIOR:.2f}")
print(f"Seu salário atual é de R${salarioNOVO:.2f}")


