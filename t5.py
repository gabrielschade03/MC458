V = int(input())
num_intervalos = int(input())
intervalos = []
for i in range(num_intervalos):
    intervalo = tuple(map(int, input().split()))
    intervalos.append(intervalo)
intervalos.sort(key=lambda x: x[0])
selected_intervalos = []

def calc_cob_min_intervalos(V, intervalos, index, selected_intervalos):
    min_intervalos = 0
    counter = 0
    index_intervalo = -1
    while True:
        max_reach = float('-inf')
        while counter < len(intervalos) and index >= intervalos[counter][0]:
            if intervalos[counter][1] > max_reach:
                max_reach = intervalos[counter][1]
                index_intervalo = counter
            counter += 1
        
        if max_reach == float('-inf'):
            return 0
        selected_intervalos.append(intervalos[index_intervalo])
        if max_reach >= V:
            min_intervalos += 1
            return min_intervalos
        index = max_reach
        min_intervalos += 1
         

result = calc_cob_min_intervalos(V, intervalos, 0, selected_intervalos)
print(result)
if result != 0:
    for intervalo in selected_intervalos:
        print(intervalo[0], intervalo[1])
