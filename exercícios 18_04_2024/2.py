tamanhoMB = float(input("Digite o tamanho do arquivo em MB:"))
velocidadeMBPS = float(input("Digite a velocidade em mbps:"))
tempo = (tamanhoMB * 8) / velocidadeMBPS
minuto = tempo / 60
segundo = tempo * 60

print(f"O tempo de download é {minuto:.0f} minutos e {segundo:.0f} segundos.")