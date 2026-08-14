
def calcular_moedas(preco, moedas):
    moedas.sort()
    menor_moeda = moedas[0]
    qnt_moeda_por_valor = []
    for i in range(menor_moeda):
        qnt_moeda_por_valor.append(0)
    j = menor_moeda
    while True:
        menor = float('inf')
        possivel_formar_somando_notas = False
        aux = 0
        for moeda in moedas:
            if moeda == j:
                if j >= preco:
                    return 1, j
                aux = 1
                possivel_formar_somando_notas = False
                break
            elif moeda > j:
                break
            else:
                complemento = j - moeda
                if qnt_moeda_por_valor[complemento] != 0:
                    menor = min(menor, qnt_moeda_por_valor[complemento] + 1)
                    possivel_formar_somando_notas = True

        if possivel_formar_somando_notas:
            if j >= preco:
                return menor, j
            qnt_moeda_por_valor.append(menor)
        else:
            qnt_moeda_por_valor.append(aux)
        j += 1

preco = int(input())
num_moedas = int(input())
moedas = [int(x) for x in input().split()]
quantidade_moedas, valor_a_pagar = calcular_moedas(preco, moedas)
print(f"{valor_a_pagar} {quantidade_moedas}")