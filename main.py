import matrixTranformation
import originalMatrixProperties
import solveSVD

accuracy = 5  # Кол-во знаков после запятой

if __name__ == '__main__':
    # Программа должна обрабатывать следующие матрицы:
    # 1. Квадратная невырожденная матрица
    # 2. Переопределенная матрица с полным рангом
    # 3. Квадратная вырожденная матрица
    # 4. Переопределенная матрица неполного ранга
    # 5. Недоопределенная матрица неполного ранга

    # Входные данные: размерность, точность, матрица коэффициентов, матрица векторов (правых членов)
    number_of_rows = 2
    number_of_columns = 2

    matrix_coefficients =  [1.0, 0.1, 0.01, 0.001,
                            1.0, 0.3, 0.09, 0.027,
                            1.0, 0.5, 0.25, 0.125,
                            1.0, 0.7, 0.49, 0.343,
                            1.0, 0.9, 0.81, 0.729,
                            1.0, 1.1, 1.21, 1.331,
                            1.0, 1.3, 1.69, 2.197,
                            1.0, 1.5, 2.25, 3.375,
                            1.0, 1.7, 2.89, 4.913,
                            1.0, 1.9, 3.61, 6.859,
                            1.0, 2.1, 4.41, 9.261,
                            1.0, 2.3, 5.29, 12.167,
                            1.0, 2.5, 6.25, 15.625,
                            1.0, 2.7, 7.29, 19.683,
                            1.0, 2.9, 8.41, 24.389,
                            1.0, 3.1, 9.61, 29.791,
                            1.0, 3.3, 10.89, 35.937,
                            1.0, 3.5, 12.25, 42.875,
                            1.0, 3.7, 13.69, 50.653,
                            1.0, 3.9, 15.21, 59.319,
                            1.0, 4.1, 16.81, 68.921,
                            1.0, 4.3, 18.49, 79.507,
                            1.0, 4.5, 20.25, 91.125,
                            1.0, 4.7, 22.09, 103.823,
                            1.0, 4.9, 24.01, 117.649,
                            1.0, 5.1, 26.01, 132.651,
                            1.0, 5.3, 28.09, 148.877,
                            1.0, 5.5, 30.25, 166.375,
                            1.0, 5.7, 32.49, 185.193,
                            1.0, 5.9, 34.81, 205.379]

    vector_coefficients =   [0.0998334,
                             0.29552,
                             0.479426,
                             0.644218,
                             0.783327,
                             0.891207,
                             0.963558,
                             0.997495,
                             0.991665,
                             0.9463,
                             0.863209,
                             0.745705,
                             0.598472,
                             0.42738,
                             0.239249,
                             0.0415807,
                             -0.157746,
                             -0.350783,
                             -0.529836,
                             -0.687766,
                             -0.818277,
                             -0.916166,
                             -0.97753,
                             -0.999923,
                             -0.982453,
                             -0.925815,
                             -0.832267,
                             -0.70554,
                             -0.550686,
                             -0.373877
    ]
    matr = [2, 2,
            1, 3
            ]
    vec = [4,
           4
           ]

    # Запись в файл
    file = open("results/matrix_" + str(number_of_rows) + "x" + str(number_of_columns) + '.txt', 'w')

    # Преобразование одномерного массива с коэффициентами в двумерный
    matrix = matrixTranformation.array_to_matrix(matr, number_of_rows, number_of_columns, file)
    vector = matrixTranformation.array_to_vector(vec, number_of_rows, file)

    # Анализ размерности матрицы
    originalMatrixProperties.matrix_dimension(matrix, file)

    # Анализ ранга матрицы
    originalMatrixProperties.matrix_rank(matrix, file)

    # Сингулярное разложение матрицы
    U, s, V = solveSVD.decomposition_matrices(matrix, accuracy, file)

    # Свойства матрицы, получаемые посредством сингулярного разложения
    file.write("СВОЙСТВА СИНГУЛЯРНОГО РАЗЛОЖЕНИЯ:\n")
    solveSVD.svd_properties(U, s, V, accuracy, file)
    file.write("========================================\n")

    # Нахождение корней. х - вектор решений системы А
    x = solveSVD.solve(U, s, V, vector, accuracy, file)
    file.write(str(x) + "\n")

    # Проверка и нахождение погрешности решения
    acc_of_origin_matrix = solveSVD.solution_check(matrix, vector, x, accuracy, file)
    file.write("Погрешность решения: " + str(acc_of_origin_matrix) +
               "%\n")

    # Нахождение числа обусловленности
    file.write("========================================\n")
    file.write("Изменение одного из значений матрицы (1 строка 1 столбец) на " + str(10 ** (-accuracy)) + "\n")

    matrix[0][0] += 10 ** (-accuracy)
    U, s, V = solveSVD.decomposition_matrices(matrix, accuracy, file)
    x = solveSVD.solve(U, s, V, vector, accuracy, file)
    file.write(str(x) + "\n")

    acc_of_modified_matrix = solveSVD.solution_check(matrix, vector, x, accuracy, file)
    file.write("Погрешность решения: " + str(acc_of_modified_matrix) +
               "%\n")

    changing_acc = acc_of_modified_matrix / acc_of_origin_matrix
    if acc_of_modified_matrix > acc_of_origin_matrix:
        file.write("Результаты вычислений ухудшились в " +
                   str(matrixTranformation.rounding_number(acc_of_modified_matrix / acc_of_origin_matrix, accuracy)) +
                   " раз(а)")
    else:
        file.write("Результаты вычислений улучшились в " +
                   str(matrixTranformation.rounding_number(acc_of_origin_matrix / acc_of_modified_matrix, accuracy)) +
                   " раз(а)")
