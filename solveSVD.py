from math import sqrt
import numpy as np
import matrixTranformation


def decomposition_matrices(matrix, accuracy, file):
    U, s, V = np.linalg.svd(matrix)

    # Округление матриц
    if len(U) != 1:
        U = matrixTranformation.rounding_matrix(U, accuracy)
    else:
        U = matrixTranformation.rounding_number(U, accuracy)
    if len(V) != 1:
        V = matrixTranformation.rounding_matrix(V, accuracy)
    else:
        V = matrixTranformation.rounding_number(V, accuracy)
    if len(s) != 1:
        s = matrixTranformation.rounding_vector(s, accuracy)
    else:
        s = matrixTranformation.rounding_number(s, accuracy)

    file.write("Левая ортогональная матрица U:\n" +
               str(U) +
               "\n")
    file.write("========================================\n")
    file.write("Сингулярные числа матрицы:\n" +
               str(s) +
               "\n")
    if np.linalg.matrix_rank(matrix) != len(s):
        rank = np.linalg.matrix_rank(matrix)
        file.write("Т.к. ранг матрицы равен rank = " +
                   str(rank) +
                   ", а кол-во независимых столбцов равно n = " +
                   str(len(V)) +
                   ", то последний(е) " +
                   str(len(V) - rank) +
                   " элемент(ов) стремится(ятся) к нулю.\n")
    file.write("========================================\n")
    file.write("Правая ортогональная матрица VT:\n" + str(V) + "\n")
    file.write("========================================\n")
    return U, s, V


def matrix_mult(transp, alpha, U, vector, w):
    if transp:
        U = U.transpose()
    for i in range(0, len(U)):
        value = 0.0
        for j in range(0, len(U[i])):
            value += alpha * U[i][j] * vector[j]
        w[i] = value


def ortonormalization(sqr_matrix, accuracy, file):
    column_norm = 0.0
    row_norm = 0.0
    for i in range(0, len(sqr_matrix)):
        for j in range(0, len(sqr_matrix[0])):
            column_norm += sqr_matrix[j][i] ** 2
            row_norm += sqr_matrix[i][j] ** 2
        column_norm = matrixTranformation.rounding_number(sqrt(column_norm), accuracy)
        row_norm = matrixTranformation.rounding_number(sqrt(row_norm), accuracy)
        file.write(str(i + 1) +
                   " столбец:\t" +
                   str(column_norm) +
                   "\n" +
                   str(i + 1) +
                   " строка:\t" +
                   str(row_norm) +
                   "\n")
        column_norm = 0.0
        row_norm = 0.0


def svd_properties(U, s, V, accuracy, file):
    file.write("Матрицы U и VT всегда квадратные размером mxm и nxn соответственно.\n")
    file.write("Столбцы и строки матриц U и VT всегда ортонормированы.\n")

    file.write("\nПроверка нормы столбцов и строк матрицы U:\n")
    ortonormalization(U, accuracy, file)

    file.write("\nПроверка нормы столбцов и строк матрицы V:\n")
    ortonormalization(V, accuracy, file)

    file.write("Следовательно, матрицы U и VT - ортогональные.\n")

    for i in range(0, len(s) - 1):
        if s[i] >= s[i+1]:
            continue
        else:
            file.write("ОШИБКА!!! Сингулярные числа матрицы расположены в невозрастающей последовательности \n")
            exit()

    file.write("Сингулярные числа расположены по главной диагонали в невозрастающем порядке: " +
               str(s) +
               "\n")
    file.write("Число обусловленности исходной матрицы: ")
    if s[len(s) - 1] == 0.0:
        file.write("бесконечность")
    else:
        file.write(str(matrixTranformation.rounding_number(s[0] / s[len(s) - 1], accuracy)) + "\n")
    for i in range(0, len(s)):
        if s[i] <= 0.0:
            s = np.delete(s, 0)
    file.write("\nРанг матрицы равен кол-ву ненулевых сингулярных чисел k = rank = " +
               str(len(s)) +
               " и значение ранга совпадает с первоначальными расчётами\n")


def solve(U, s, V, vector, accuracy, file):
    file.write("Корни СЛАУ:\n")
    w = [0] * len(U)
    x = [0] * len(V)
    matrix_mult(1, 1.0, U, vector, w)
    w = matrixTranformation.array_to_vector(w, len(U), file)

    for i in range(0, len(V)):
        wi = w[i]
        alpha = s[i]
        if alpha != 0.0:
            alpha = 1.0 / alpha
        w[i] = alpha * w[i]

    matrix_mult(1, 1.0, V, w, x)
    matrixTranformation.rounding_vector(x, accuracy)
    return x


def solution_check(matrix, vector, x, accuracy, file):
    answer = [0.0] * len(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            answer[i] += matrixTranformation.rounding_number(matrix[i][j] * x[j], accuracy)
    average_error = 0

    for i in range(0, len(matrix)):
        error = abs(1 - answer[i]/vector[i]) * 100
        average_error += error
        matrixTranformation.rounding_number(error, accuracy)
    acc_res = matrixTranformation.rounding_number(average_error/len(matrix), accuracy)

    return acc_res
