def encontra_repeticoes(a: int, b: int):
    """ Cria um terceiro vetor para armazenar os valores repetidos nos vetores 'A' + 'B'
    :param a: Valores inseridos no Vetor A
    :param b: Valores inseridos no Vetor B
    :return: Retorna os valores repetidos dentro do vetor 'A' e vetor 'B'
    """
    vetor_final = []
    numeros_verificados = set()
    # Verifica os elementos repetidos no vetor 'A' e no vetor 'B'
    for num in a:
        if num not in numeros_verificados and num in b:
            vetor_final.append(num)
            numeros_verificados.add(num)
    return vetor_final


# Vetores definidos
a: list[int] = []
b: list[int] = []


print("Digite os valores do vetor A (20 números inteiros):")
for i in range(20):
    valor = int(input(f"Digite o valor {i + 1}: "))
    a.append(valor)


print("\nDigite os valores do vetor B (20 números inteiros):")
for i in range(20):
    valor = int(input(f"Digite o valor {i + 1}: "))
    b.append(valor)


resultado = encontra_repeticoes(a, b)


print("\nValores repetidos nos vetores A e B:")
print(resultado)
