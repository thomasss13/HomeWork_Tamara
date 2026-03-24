N = int(input('Размер массива: '))
arr = []

for i in range(N):
    num = int(input(f"{i + 1}-й элемент массива: "))
    arr.append(num)

processed = []

for i in range(N):
    if arr[i] in processed:
        continue
    
    index = []
    
    for j in range(N):
        if arr[i] == arr[j]:
            index.append(j)
    
    if len(index) < 2:
        print(f"Для числа {arr[i]} нет минимального расстояния т.к элемент в массиве один.")
    else:
        min_dist = float('inf')
        best_i, best_j = -1, -1
        
        for k in range(len(index) - 1):
            dist = index[k + 1] - index[k]
            if dist < min_dist:
                min_dist = dist
                best_i, best_j = index[k], index[k + 1]
        
        print(f"Для числа {arr[i]} минимальное расстояние в массиве по индексам: {best_i} и {best_j}")
    
    processed.append(arr[i])