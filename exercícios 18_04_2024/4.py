ganhoPorHORA = float(input("Quanto você ganha por hora? R$:"))
horasPorMES = int(input("Quantidade de horas trabalhadas no mês:"))

salario = ganhoPorHORA * horasPorMES

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

salario_liquido = salario - ir - inss - sindicato

print(f"\n+Salário bruto R$ {salario:.2f}\n-IR R${ir:.2f},\n-INSS R${inss:.2f},\n-SINDICATO R${sindicato:.2f} \nSeu salário líquido: R${salario_liquido:.2f}")
