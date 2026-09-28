print("| DIAS > HORAS > MINUTOS > SEGUNDOS > SEMANAS > MESES > ANOS")
print("-"*60)

dias = int(input("> Digite aqui o valor em dias: "))

semanas = dias/7
meses = semanas/4
anos = meses/12

horas = dias*24
minutos = horas*60
segundos = minutos*60

print(f"Anos: {anos} | Meses {meses} | Semanas {semanas} | Dias: {dias} ")
print(f"Horas: {horas} | Minutos: {minutos} | Segundos: {segundos}")