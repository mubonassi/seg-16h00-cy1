print("| TODOS OS CÁLCULOS |")
print("-"*60)

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))

soma = numero1+numero2
sub = numero1-numero2
mult = numero1*numero2
div = numero1/numero2
exp = numero1**numero2
res = numero1%numero2
divInt = numero1//numero2

print("-"*60)

print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {sub}")
print(f"{numero1} * {numero2} = {mult}")
print(f"{numero1} / {numero2} = {div}")
print(f"{numero1} ** {numero2} = {exp}")
print(f"{numero1} % {numero2} = {res}")
print(f"{numero1} // {numero2} = {divInt}")