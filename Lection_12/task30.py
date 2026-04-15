def msum(matrix):
    return sum([element for row in matrix for element in row])

if __name__ == "__main__":
    # Пример 1: Матрица 2x3
    matrix1 = [[1, 2, 3], 
               [4, 5, 6]]
    
    print("Матрица 1:")
    for row in matrix1:
        print(row)
    print(f"Сумма элементов: {msum(matrix1)}")  # 21
    print()
    
    # Пример 2: Матрица 3x3
    matrix2 = [[1, 2, 3], 
               [4, 5, 6], 
               [7, 8, 9]]
    
    print("Матрица 2:")
    for row in matrix2:
        print(row)
    print(f"Сумма элементов: {msum(matrix2)}")  # 45
    print()
    
    # Пример 3: Матрица 4x2
    matrix3 = [[10, 20], 
               [30, 40], 
               [50, 60], 
               [70, 80]]
    
    print("Матрица 3:")
    for row in matrix3:
        print(row)
    print(f"Сумма элементов: {msum(matrix3)}")  # 360
    print()
    
    # Пример 4: Пустая матрица
    matrix4 = []
    print("Матрица 4 (пустая):")
    print(f"Сумма элементов: {msum(matrix4)}")  # 0