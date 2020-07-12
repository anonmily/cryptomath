import math

from modarithmetic import get_mod_inverse

def chinese_remainder_theorem_2(sys_of_congruences, verbose=False):
    '''
    Chinese Remainder Theorem for 2 congruences.
    TODO: expand for more than 2 congruences

    x = 3 (mod 7)     and     x = 9 (mod 13)
    sys_of_congruences = [(3,7), (9,13)]
    chinese_remainder_theorem(sys_of_congruences)
    '''
    if len(sys_of_congruences) < 2:
        raise ValueError('Less than 2 congruence equations given.')

    x1, x2 = sys_of_congruences
    c1, m1 = x1
    c2, m2 = x2
    print(sys_of_congruences)

    # the moduli must have gcd(m1,m2) = 1
    m1_m2_gcd = math.gcd(m1, m2) 
    if m1_m2_gcd != 1:
        raise ValueError('gcd(%s,%s)=%s. gcd=1 is required for a unique solution to the Chinese Remainder Theorem.' % (m1,m2, m1_m2_gcd))
    
    c_diff = c2 - c1
    m1_inv = get_mod_inverse(a=m1, m=m2)
    k = (c_diff * m1_inv) % m2
    x = c1 + m1*k
    m1_m2 = m1*m2

    # Print results
    if verbose:
        print('---------------------')
        print('Given:')
        print(f'x={c1} (mod {m1})')
        print(f'x={c2} (mod {c2})')
        print('---------------------')
        print(f'x = {c1} + {m1}*k == {c2} (mod {m2})')
        print(f'{m1}k === {c_diff} (mod {m2})')
        print(f'm1_inv = {m1_inv}')
        print(f'k === ({m1_inv})({c_diff}) (mod {m2})')
        print(f'k === {k}')
        print('\nThen, ')
        print(f'x = c1 + m1*k = {c1} + ({m1})({k})')
        print(f'{x=}')
        print(f'general x = {x} + {m1_m2}t')
     
    #general_x = lambda k: x + m1_m2*k
    return (x, m1_m2)

def chinese_remainder_theorem(sys_of_congruences, verbose=False):
    '''
    Chinese Remainder Theorem: More than 2 congruences
    '''
    n = len(sys_of_congruences)
    if n <= 2:
        return chinese_remainder_theorem_2(sys_of_congruences, verbose=verbose)
    else:
        i = 0
        c1, m1 = sys_of_congruences[i]
        while i < n - 1:
            c2, m2 = sys_of_congruences[i+1]
            c1, m1 = chinese_remainder_theorem_2([ (c1, m1), (c2, m2) ])
            i = i + 1
        return (c1, m1)
