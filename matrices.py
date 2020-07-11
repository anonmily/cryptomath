import numpy as np
from modarithmetic import find_mod_inverse

def get_determinant(a):
    det = np.linalg.det(a)
    return det

def get_matrix_cofactor(matrix):
    return np.linalg.inv(matrix) * np.linalg.det(matrix)

def get_matrix_inverse(a, mod=False):
    '''
    Find the matrix inverse (optionally modular):

    get_matrix_inverse(a, mod=26)
    '''
    a = np.array(a)
    det = get_determinant(a)
    det_inv = find_mod_inverse(det, m=mod)[0] if mod else 1/det
    adj = get_matrix_cofactor(a)
    print('\nA')
    print(a)
    print(f'\n{det_inv=}')
    print('\nAdj(a)')
    print(adj)
    if mod: 
        adj = adj % mod
        print(f'\nAdj(a) mod {mod}')
        print(adj)
    matrix_inverse = det_inv*adj
    print('\nA inverse')
    print(matrix_inverse)
    if mod: 
        matrix_inverse = matrix_inverse % mod
        print(f'\nA inverse mod {mod}')
        print(matrix_inverse)
    return matrix_inverse
