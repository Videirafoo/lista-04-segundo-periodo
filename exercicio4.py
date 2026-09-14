def limpar_texto(texto):
    return "".join(
        caractere.lower()
        for caractere in texto
        if not caractere.isspace()
    )


def palindromo(texto):
    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return palindromo(texto[1:-1])


def exercicio4():
    print("Exercício 4 - Palíndromo Recursivo")

    texto = input("Digite uma palavra ou frase: ")
    texto_limpo = limpar_texto(texto)

    if palindromo(texto_limpo):
        print("A string é um palíndromo.")
    else:
        print("A string não é um palíndromo.")


if __name__ == "__main__":
    exercicio4()
