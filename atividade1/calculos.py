import math

numero = float(input("Digite um número não negativo: "))
print("Raiz quadrada:", math.sqrt(numero))

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"Área: {area:.2f}")
