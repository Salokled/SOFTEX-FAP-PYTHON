peso = float(input("Digite o peso da pesca em kg:"))
excesso = peso - 50
multa = excesso * 4

if peso > 50: 
    print(f"Multa R$:{multa:.2f}")

else:
    print("Este valor não resulta em multa.")




