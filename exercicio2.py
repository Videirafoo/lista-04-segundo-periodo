def potencia(x, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / potencia(x, -n)

    return x * potencia(x, n - 1)


def exercicio2():
    print("Exercício 2 - Potência Recursiva")

    x = float(input("Digite a base: "))
    n = int(input("Digite o expoente: "))

    resultado = potencia(x, n)

    print(f"{x} elevado a {n}: {resultado}")


if __name__ == "__main__":
    exercicio2()
