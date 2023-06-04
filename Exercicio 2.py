def converte_notas_para_graus(notas: str):
    """Cria uma lista contendo a conversão das notas em graus
    :param notas: notas que serão convertidas
    :return: Retorna o grau da nota já convertida
    """
    graus = {
        'Dó': 'I',
        'Ré': 'II',
        'Mi': 'III',
        'Fá': 'IV',
        'Sol': 'V',
        'Lá': 'VI',
        'Si': 'VII'
    }

    graus_notas = []

    for nota in notas:
        grau = graus.get(nota)

        if grau is not None:
            graus_notas.append(grau)

    return graus_notas


# Entrada de notas musicais
notas = []

print("Digite as notas musicais:")
print("Opções: Dó, Ré, Mi, Fá, Sol, Lá, Si")
print("Digite 'fim' para encerrar")

while True:
    nota = input("Digite uma nota (ou 'fim' para encerrar): ")

    if nota.lower() == 'fim':
        break

    notas.append(nota)

# Converter notas para graus
resultado = converte_notas_para_graus(notas)

print("\nGraus correspondentes às notas musicais:")
print(resultado)