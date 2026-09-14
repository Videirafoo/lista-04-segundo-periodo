from exercicio1 import exercicio1
from exercicio2 import exercicio2
from exercicio3 import exercicio3
from exercicio4 import exercicio4
from exercicio5 import exercicio5
from exercicio6 import exercicio6


exercicios = [
    exercicio1,
    exercicio2,
    exercicio3,
    exercicio4,
    exercicio5,
    exercicio6,
]

print("Lista de Exercícios de Recursividade")
print("Os exercícios serão executados em sequência.")

for numero, exercicio in enumerate(exercicios, start=1):
    exercicio()

    if numero < len(exercicios):
        input(
            f"Pressione Enter para continuar para o próximo exercício "
            f"({numero + 1})..."
        )
        print("\n" + "-" * 50 + "\n")
