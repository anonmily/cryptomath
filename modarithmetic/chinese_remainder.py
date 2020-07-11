import math

from modarithmetic import get_mod_inverse

def chinese_remainder_theorem(sys_of_congruences):
    '''
    Chinese Remainder Theorem for 2 congruences.
    TODO: expand for more than 2 congruences

    x = 3 (mod 7)     and     x = 9 (mod 13)
    sys_of_congruences = [(3,7), (9,13)]
    chinese_remainder_theorem(sys_of_congruences)
    '''
    c1, c2 = sys_of_congruences
    c1_r = c1[0]
    c1_mod = c1[1]

    c2_r = c2[0]
    c2_mod = c2[1]

    # the moduli must have gcd(m1,m2) = 1
    are_mods_rel_prime = math.gcd(c1_mod, c2_mod) == 1
    assert( are_mods_rel_prime )
    
    r_diff = c2_r - c1_r
    inv_c1_mod = get_mod_inverse(a=c1_mod, m=c2_mod)
    k = r_diff*inv_c1_mod
    print('r_diff=', r_diff, 'inv_c1_mod=', inv_c1_mod, 'k=',k)

    x = c1_r + c1_mod*k
    print('x=', x)

    general_x = lambda t: x + c1_mod*c2_mod*t
    print(f'general x = {x} + {c1_mod*c2_mod}t')
    
    return general_x