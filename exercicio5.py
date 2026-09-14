def soma_digitos(numero):
    if numero < 10:
        return numero

    return numero % 10 + soma_digitos(numero // 10)


def exercicio5():
    print("Exercício 5 - Soma dos Dígitos")

    numero = int(input("Digite um número inteiro positivo: "))

    if numero < 0:
        print("Digite apenas um número inteiro positivo.")
        return

    resultado = soma_digitos(numero)

    print(f"Soma dos dígitos de {numero}: {resultado}")


if __name__ == "__main__":
    exercicio5()
