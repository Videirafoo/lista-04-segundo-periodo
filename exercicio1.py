def mdc(a, b):
    if b == 0:
        return abs(a)
    return mdc(b, a % b)


def exercicio1():
    print("Exercício 1 - MDC Recursivo")

    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))

    resultado = mdc(a, b)

    print(f"MDC de {a} e {b}: {resultado}")


if __name__ == "__main__":
    exercicio1()
