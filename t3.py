def countingSort(A, B, n, k):
    C = [0] * (k+1)
    for i in range(n):
        C[A[i][1]] += 1
    for j in range(1, k+1):
        C[j] += C[j-1]
    for p in range(n-1, -1, -1):
        B[C[A[p][1]]-1] = A[p]
        C[A[p][1]] -= 1

M = int(input())

for i in range(M):
    linha = input()
    tam_string, num_strings = input().split()
    tam_string = int(tam_string)
    num_strings = int(num_strings)
    list_inversions = []
    max_inversions = 0

    for j in range(num_strings):
        string = input()
        counter_A = 0
        counter_B = 0
        counter_C = 0
        counter_D = 0
        counter_E = 0
        counter_F = 0
        counter_G = 0
        counter_H = 0
        counter_I = 0
        counter_J = 0
        counter_K = 0
        counter_L = 0
        counter_M = 0
        counter_N = 0
        counter_O = 0
        counter_P = 0
        counter_Q = 0
        counter_R = 0
        counter_S = 0
        counter_T = 0
        counter_U = 0
        counter_V = 0
        counter_W = 0
        counter_X = 0
        counter_Y = 0
        num_inversions = 0
        for k in range(tam_string - 1, -1, -1):
            if string[k] == 'A':
                counter_A += 1
            elif string[k] == 'B':
                counter_B += 1
                num_inversions = num_inversions + counter_A
            elif string[k] == 'C':
                counter_C += 1
                num_inversions = num_inversions + counter_A  + counter_B
            elif string[k] == 'D':
                counter_D += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C
            elif string[k] == 'E':
                counter_E += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D
            elif string[k] == 'F':
                counter_F += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E
            elif string[k] == 'G':
                counter_G += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F
            elif string[k] == 'H':
                counter_H += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G
            elif string[k] == 'I':
                counter_I += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H
            elif string[k] == 'J':      
                counter_J += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I
            elif string[k] == 'K':      
                counter_K += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J 
            elif string[k] == 'L':
                counter_L += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K 
            elif string[k] == 'M':
                counter_M += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J +	counter_K +	counter_L 
            elif string[k] == 'N':
                counter_N += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M 
            elif string[k] == 'O':
                counter_O += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N 
            elif string[k] == 'P':
                counter_P += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D +	counter_E +	counter_F +	counter_G +	counter_H +	counter_I +	counter_J +	counter_K +	counter_L +	counter_M +	counter_N +	counter_O 
            elif string[k] == 'Q':
                counter_Q += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P 
            elif string[k] == 'R':
                counter_R += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P +	counter_Q 
            elif string[k] == 'S':
                counter_S += 1
                num_inversions = num_inversions + counter_A + counter_B +	counter_C +	counter_D +	counter_E +	counter_F +	counter_G +	counter_H +	counter_I +	counter_J +	counter_K +	counter_L +	counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R	
            elif string[k] == 'T':
                counter_T += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R + counter_S
            elif string[k] == 'U':
                counter_U += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L +	counter_M +	counter_N +	counter_O +	counter_P +	counter_Q +	counter_R +	counter_S +	counter_T 
            elif string[k] == 'V':
                counter_V += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R + counter_S + counter_T + counter_U 
            elif string[k] == 'W':
                counter_W += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R + counter_S + counter_T + counter_U + counter_V 
            elif string[k] == 'X':
                counter_X += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R + counter_S + counter_T + counter_U + counter_V + counter_W 
            elif string[k] == 'Y':
                counter_Y += 1
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R + counter_S + counter_T + counter_U + counter_V + counter_W + counter_X
            elif string[k] == 'Z':
                num_inversions = num_inversions + counter_A + counter_B + counter_C + counter_D + counter_E + counter_F + counter_G + counter_H + counter_I + counter_J + counter_K + counter_L + counter_M + counter_N + counter_O + counter_P + counter_Q + counter_R + counter_S + counter_T + counter_U + counter_V + counter_W + counter_X + counter_Y
        list_inversions.append((string, num_inversions))
        if num_inversions > max_inversions:
            max_inversions = num_inversions
    auxiliar = list_inversions[0:num_strings]
    countingSort(list_inversions, auxiliar, num_strings, max_inversions)
    for string, num_inversions in auxiliar:
        print(string)
    if i < M - 1:
        print("")