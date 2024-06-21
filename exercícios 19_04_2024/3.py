num1 = float(input("Insira a primeira nota do aluno:"))
num2 = float (input("Insira a segunda nota do aluno:"))

media = (num1 + num2) / 2

if media >= 7 and media < 10:
    print("Aprovado")
    
elif media < 7:
    print ("Reprovado")

else:
    print ("Aprovado com distinção!")
    


