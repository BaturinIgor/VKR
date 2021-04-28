import numpy as np


def array_to_matrix(coefficients, m, n, file):
    if len(coefficients) > m*n:
        file.write("ОШИБКА! Коэффициентов больше размерности матрицы. Коэффициентов " +
                   str(len(coefficients)) +
                   ", а должно быть " +
                   str(m*n))
        exit()

    if len(coefficients) < m*n:
        file.write("ОШИБКА! Коэффициентов меньше размерности матрицы. Коэффициентов " +
                   str(len(coefficients)) +
                   ", а должно быть " +
                   str(m * n))
        exit()

    original_matrix = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            original_matrix[i][j] = coefficients[i*n + j]
    return original_matrix


def array_to_vector(coefficients, m, file):
    if len(coefficients) > m:
        file.write("ОШИБКА! Коэффициентов больше размерности матрицы. Коэффициентов " +
                   str(len(coefficients)) +
                   ", а должно быть " +
                   str(m))
        exit()

    if len(coefficients) < m:
        file.write("ОШИБКА! Коэффициентов меньше размерности матрицы. Коэффициентов " +
                   str(len(coefficients)) +
                   ", а должно быть " +
                   str(m))
        exit()

    vector = [0]*m

    for i in range(m):
        vector[i] = coefficients[i]
    return vector


def rounding_number(value, accuracy):
    return round(value, accuracy)


def rounding_vector(value, accuracy):
    for i in range(0, len(value)):
        value[i] = round(value[i], accuracy)
    return value


def rounding_matrix(value, accuracy):
    for i in range(0, len(value)):
        for j in range(0, len(value[0])):
            value[i][j] = round(value[i][j], accuracy)
    return value
