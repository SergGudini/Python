# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и 
# возвращает транспонированную матрицу.


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matrix = [[1, 2], [3, 4]]
#matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

# def transpose(matrix):
#     #new_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
#     new_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
            
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             new_matrix[j][i] = matrix[i][j]
      
#     return new_matrix
def transpose(matrix):
    matrix_T = [list(i) for i in zip(*matrix)]
    return matrix_T
transposed_matrix = transpose(matrix)
print(transposed_matrix)

