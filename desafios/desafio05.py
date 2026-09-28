print("| CALCULO DE TEMPO DE VIAGEM |")
print("-"*60)

velocidadeMedia = float(input("> Digite a velocidade média (km/h): "))
distanciaTotal = float(input("> Digite a distância que será percorrida (km): "))

tempoViagem = distanciaTotal/velocidadeMedia

print(f"Tempo total de viagem (estimada): {tempoViagem}hrs")