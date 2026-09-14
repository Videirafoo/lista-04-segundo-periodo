def anagramas(texto):
    if len(texto) <= 1:
        return [texto]

    resultado = []

    for indice in range(len(texto)):
        caractere = texto[indice]
        restante = texto[:indice] + texto[indice + 1:]

        for anagrama in anagramas(restante):
            palavra = caractere + anagrama

            if palavra not in resultado:
                resultado.append(palavra)

    return resultado


def exercicio6():
    print("Exercício 6 - Anagramas Recursivos")

    texto = input("Digite uma string: ")

    resultado = anagramas(texto)

    print("Anagramas encontrados:")

    for palavra in resultado:
        print(palavra)

    print(f"Total: {len(resultado)}")


if __name__ == "__main__":
    exercicio6()
