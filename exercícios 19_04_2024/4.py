preco1= float(input("Digite o primeiro preço R$:"))
preco2= float(input("Digite o segundo preço R$:"))
preco3= float(input("Digite o terceiro preço R$:"))

if preco1 < preco2 and preco1 < preco3:
    print (f"Você deve comprar o produto que custa R${preco1:.2f}")
    
elif preco2 < preco1 and preco2 < preco3:
    print (f"Você deve comprar o produto que custa R${preco2:.2f}")
    
else:
   print (f"Você deve comprar o produto que custa R${preco3:.2f}") 
   
    