n = 0                                   # n = número de elementos do subconjunto
N, Q = map(int, input().split())   
pos = [0] * N                           # vetor com as posições de cada elemento em set. pos[i] = posição de i em set
set = [0] * N                           # vetor com os elementos, ordenado pela ordem de inserção

for i in range(Q): 
    comand = input().split()
    operator = comand[0]

    if operator == "l":                 # se o operador for l, zera o subconjunto
        n = 0

    else:
        x = int(comand[1])              # pega x do comando
        if x < N:                       # verifica antes de tudo se o x é um número que está no conjunto

            if operator == "i":
                if pos[x] > n-1 or x != set[pos[x]]:    # só insere se ele não estiver no subconjunto.
                    set[n] = x
                    pos[x] = n
                    n = n + 1

            elif operator == "r":
                y = pos[x]                          # y = posição em set do valor x  
                if y <= n-1 and set[y] == x:        # verifica se o x está em uma posição válida
                    z = set[n-1]                    # z = valor do número na última posição da sequência S
                    set[y] = z                      # coloco z na posição de x em set
                    pos[z] = y                      # coloco que a posição de z é y, a posição onde x estava
                    n = n-1

            else: 
                y = pos[x]
                if y <= n-1 and set[y] == x:        # verifica se ele está no subconjunto
                    print(1)
                else:
                    print(0)
