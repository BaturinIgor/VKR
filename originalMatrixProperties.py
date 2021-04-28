import numpy as np


def matrix_dimension(matrix, file):
    if len(matrix) == len(matrix[0]):
        determinant = np.linalg.det(matrix)
        file.write("Исходная матрица - квадратная с определителем " +
                   str(determinant) +
                   ".\n")
        if determinant == 0:
            file.write("Матрица вырожденная, т.к. определитель равен 0.\n")
        else:
            file.write("Матрица невырожденная, т.к. определитель не равен 0.\n")
    else:
        file.write("Исходная матрица - прямоугольная, а СЛАУ - ")
        if len(matrix) > len(matrix[0]):
            file.write("переопределенная, т.к. кол-во строк больше кол-ва столбцов\n")
        else:
            file.write("непереопределенная, т.к. кол-во столбцов больше кол-ва строк\n")


def matrix_rank(matrix, file):
    rank = np.linalg.matrix_rank(matrix)
    if rank == len(matrix[0]):
        file.write("Исходная матрица не является матрицей неполного ранга, т.к. ранг матрицы rank = " +
                   str(rank) +
                   " равен кол-ву независимых строк/столбцов n = " +
                   str(len(matrix[0])) +
                   "\n")
    else:
        file.write("Исходная матрица является матрицей неполного ранга, т.к. ранг матрицы rank = " +
                   str(rank) +
                   " не равен кол-ву независимых строк/столбцов n = " +
                   str(len(matrix[0])) +
                   "\n")
    file.write("========================================\n")