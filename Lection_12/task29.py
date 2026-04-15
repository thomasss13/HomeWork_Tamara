def transpose(matrix):

    transposed = [[matrix[row][col] for row in range(len(matrix))] 
                  for col in range(len(matrix[0]))]
    return transposed


if __name__ == "__main__":
    
    # Пример 1: Матрица 2x3
    matrix1 = [[1, 2, 3], 
               [4, 5, 6]]
    
    print("Исходная матрица 2x3:")
    for row in matrix1:
        print(row)
    
    result1 = transpose(matrix1)
    
    print("\nТранспонированная матрица 3x2:")
    for row in result1:
        print(row)
    
    # Пример 2: Матрица 3x3
    matrix2 = [[1, 2, 3], 
               [4, 5, 6], 
               [7, 8, 9]]
    
    print("\n\nИсходная матрица 3x3:")
    for row in matrix2:
        print(row)
    
    result2 = transpose(matrix2)
    
    print("\nТранспонированная матрица 3x3:")
    for row in result2:
        print(row)
    
    # Пример 3: Матрица 4x2
    matrix3 = [[1, 2], 
               [3, 4], 
               [5, 6], 
               [7, 8]]
    
    print("\n\nИсходная матрица 4x2:")
    for row in matrix3:
        print(row)
    
    result3 = transpose(matrix3)
    
    print("\nТранспонированная матрица 2x4:")
    for row in result3:
        print(row)