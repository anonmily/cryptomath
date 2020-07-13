import numpy as np
from .modarithmetic import get_mod_inverse

def get_determinant(a):
    det = np.linalg.det(a)
    return det

def get_matrix_cofactor(matrix):
    return np.linalg.inv(matrix) * np.linalg.det(matrix)

def get_matrix_inverse(a, m=False):
    '''
    Find the matrix inverse (optionally modular):

    get_matrix_inverse(a, m=26)
    '''
    a = np.array(a)
    
    det = get_determinant(a)
    det_inv = get_mod_inverse(det, m=m) if m else 1/det

    adj = get_matrix_cofactor(a)
    if m: adj = adj % m

    matrix_inverse = det_inv*adj

    if m: 
        matrix_inverse = matrix_inverse % m
    return matrix_inverse
