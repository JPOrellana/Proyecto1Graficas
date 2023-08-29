from math import isclose, sqrt
import math

def matrixMultiplier(matrixA, matrixB):

    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])


    if colsA == rowsB:
 
        matrixC = [[0 for _ in range(colsB)] for _ in range(rowsA)]
 
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                  
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        return None


def vectorXmatrix(matrix, vector):
 
    rows = len(matrix)
    cols = len(matrix[0])
    size = len(vector)

  
    if cols == size:
      
        newVector = [0 for row in range(rows)]

        for i in range(rows):
            for j in range(cols):
                newVector[i] += matrix[i][j] * vector[j]
        return newVector
    else:
        return None

def barycentricCoords(A, B, C, P):

    areaPCB = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])
    
    areaACP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])
    
    areaABC = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1])


    try:
        u = areaPCB / areaABC
        v = areaACP / areaABC
        w = 1 - u - v 
        return u, v, w
    except:
        return -1,-1,-1


def identity_matrix(n):
    result = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        result.append(row)
    return result

def matrix_multiply(matrixA, matrixB):
    n = len(matrixA)
    m = len(matrixB[0])
    result = []

    for i in range(n):
        row = []
        for j in range(m):
            dot_product = 0
            for k in range(len(matrixB)):
                dot_product += matrixA[i][k] * matrixB[k][j]
            row.append(dot_product)
        result.append(row)
    
    return result

def inverse_matrix(matrix):
    n = len(matrix)
    identity = identity_matrix(n)

    for i in range(n):
        diagonal_element = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= diagonal_element
            identity[i][j] /= diagonal_element
        
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity[k][j] -= factor * identity[i][j]

    return identity

def cross_product(vecA, vecB):
    if len(vecA) != 3 or len(vecB) != 3:
        raise ValueError("Los vectores deben ser de 3 componentes.")
    
    result = [
        vecA[1] * vecB[2] - vecA[2] * vecB[1],
        vecA[2] * vecB[0] - vecA[0] * vecB[2],
        vecA[0] * vecB[1] - vecA[1] * vecB[0]
    ]
    return result

def vector_normalize(vector):
    magnitude = math.sqrt(sum(component ** 2 for component in vector))
    normalized_vector = [component / magnitude for component in vector]
    return normalized_vector

def subtract_vector(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise ValueError("Los vectores deben tener la misma longitud.")
    return [a - b for a, b in zip(vectorA, vectorB)]

def dot_product(A, B):
    if len(A) != len(B):
        raise ValueError("Los vectores deben tener la misma longitud.")

    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    
    return result












