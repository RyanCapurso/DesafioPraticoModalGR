def calcular_opcoes_retirada(valor_emprestimo):
    """Calcula a quantidade das notas de cada opção de retirada
    :param valor_emprestimo: Valor do emprestimo solicitado pelo usuário
    :return: Retorna as possiveis opções de retirada com base nas notas e métodos disponíveis
    """
    notas_maiores = [100, 50, 20, 5]
    notas_menores = [20, 10, 5, 2]

    salva_valor_emprestimo = valor_emprestimo

    opcoes_retirada = {
        'Notas de maior valor': [],
        'Notas de menor valor': [],
        'Notas meio a meio': {
            'Notas de maior valor': [],
            'Notas de menor valor': []
        }
    }

    # Calcular notas de maior valor
    for nota in notas_maiores:
        quantidade = valor_emprestimo // nota
        opcoes_retirada['Notas de maior valor'].append(f"{quantidade} x {nota} reais")
        valor_emprestimo -= quantidade * nota

    valor_emprestimo = salva_valor_emprestimo

    # Calcular notas de menor valor
    for nota in notas_menores:
        quantidade = valor_emprestimo // nota
        opcoes_retirada['Notas de menor valor'].append(f"{quantidade} x {nota} reais")
        valor_emprestimo -= quantidade * nota

    valor_emprestimo = salva_valor_emprestimo

    # Calcular notas meio a meio
    valor_maiores = valor_emprestimo // 2
    valor_menores = valor_emprestimo - valor_maiores

    for nota in notas_maiores:
        quantidade = valor_maiores // nota
        opcoes_retirada['Notas meio a meio'][f'Notas de maior valor'].append(f"{quantidade} x {nota} reais")
        valor_maiores -= quantidade * nota

    for nota in notas_menores:
        quantidade = valor_menores // nota
        opcoes_retirada['Notas meio a meio']['Notas de menor valor'].append(f"{quantidade} x {nota} reais")
        valor_menores -= quantidade * nota

    return opcoes_retirada


# Entrada dos dados do colaborador
nome_colaborador = input("Digite o nome do colaborador: ")
data_admissao = input("Digite a data de admissão (dd/mm/aaaa): ")
salario_atual = float(input("Digite o salário atual: "))
valor_emprestimo = float(input("Digite o valor do empréstimo desejado: "))

# Verificar se o colaborador atende aos requisitos mínimos
anos_trabalho = 2023 - int(data_admissao[-4:])

if anos_trabalho <= 5:
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa: Não possui ao menos 5 anos de empresa")

elif valor_emprestimo > salario_atual * 2:
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa: Valor do emprestimo excede o dobro do salário")

elif valor_emprestimo % 2 != 0:
    print("Insira um valor válido!")
else:
    # Calcular as opções de retirada
    opcoes_retirada = calcular_opcoes_retirada(valor_emprestimo)

    # Exibir as opções de retirada
    print(f"\nValor empréstimo: {valor_emprestimo} reais")
    print("\nOpções de retirada:")
    for tipo, notas in opcoes_retirada.items():
        print(f"\n{tipo}:")
        if isinstance(notas, list):
            for nota in notas:
                print(f"• {nota}")
        else:
            for tipo_notas, notas_valor in notas.items():
                print(f"\n{tipo_notas}:")
                for nota in notas_valor:
                    print(f"• {nota}")