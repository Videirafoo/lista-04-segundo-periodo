def inverter_string(texto):
    if len(texto) <= 1:
        return texto

    return inverter_string(texto[1:]) + texto[0]


def exercicio3():
    print("Exercício 3 - Inverter String")

    texto = input("Digite uma string: ")

    resultado = inverter_string(texto)

    print(f"String invertida: {resultado}")


if __name__ == "__main__":
    exercicio3()
