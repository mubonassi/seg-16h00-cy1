#Calculando Variaveis e Recebendo Informações

#Calculando com Numeros (int/float)
num1 = 10
num2 = 20
soma = num1+num2
calculo = num1+num1+num2*num1/num2*num1/num2-num2*num1

print(f"{num1} + {num2} = {soma}")
print(f"Calculo inventado: {calculo}")

#Calculando com Texto (string)
val1 = "banana"
val2 = "maçã"
frase = val1 + " " + val2
frase2 = f"{val1} com {val2}"

print(frase)
print(frase2)

#Calculando com outros tipos de dados
#Convertendo valores
#str() -> transformando em string
#int() ou float() -> transformando em numero

val1 = 10
val2 = "20"
teste1 = str(val1) + val2
teste2 = val1 + int(val2)

print(teste1)
print(teste2)

#Recebendo informações do usuário pelo terminal
#Função input()
variavel = input("Digite alguma coisa: ")
print(f"Você digitou {variavel}")

#Transformando o input em número
numero = int(input("Digite um numero: "))
soma = numero + numero
print(f"{numero} + {numero} = {soma}")