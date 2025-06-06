def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))
    print()

# Тема: Генераторы списков
# Упражнение 1: Перемножение матриц
# - Создайте с помощью генераторов списков две матрицы размером 3x3 со значениями от 1 до 9 и от 9 до 1.
#     Ожидаемая матрица: matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     Ожидаемая матрица: matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
matrix1 = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
matrix2 = [[9 - (i + j * 3) for i in range(3)] for j in range(3)]
# - Используйте генераторы списков для вычисления произведения этих матриц.
#     Ожидаемая матрица: product = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
product = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
# - Выведите исходные матрицы и результат их произведения.
print_matrix(matrix1)
print_matrix(matrix2)
print_matrix(product)
# Создаем вторую матрицу 3x3 с числами от 9 до 1
matrix3 = [[9 - (i + j * 3) for i in range(3)] for j in range(3)]
print_matrix(matrix3)
# Транспонируем вторую матрицу, чтобы было удобнее умножать строки на столбцы
transposed_matrix2 = [[matrix2[j][i] for j in range(3)] for i in range(3)]
print_matrix(transposed_matrix2)
# Создаем матрицу произведения
matrix_product = [[sum(matrix1[i][k] * transposed_matrix2[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
print_matrix(matrix_product)
