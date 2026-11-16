import operacoes
from operacoes import dobro

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Soma:", operacoes.somar(numero1, numero2))
print("Média:", operacoes.media(numero1, numero2))
print("Dobro do primeiro número:", dobro(numero1))
print("Triplo de 4:", operacoes.triplo(4))
print("Média de 6 e 8:", operacoes.media(6, 8))
