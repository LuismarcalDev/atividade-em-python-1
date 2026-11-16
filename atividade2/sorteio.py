from random import randint, choice
import math as matematica
import random as rd

dado1 = randint(1, 6)
dado2 = randint(1, 6)

print("Primeiro dado:", dado1)
print("Segundo dado:", dado2)
print("Soma dos dados:", dado1 + dado2)

nomes = ["Ana", "Bruno", "Carla"]
print("Nome sorteado com choice:", choice(nomes))
print("Nome sorteado com rd.choice:", rd.choice(nomes))
print("Raiz quadrada de 81:", matematica.sqrt(81))
