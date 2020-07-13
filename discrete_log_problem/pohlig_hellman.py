import math
from sage.all import factor
from .baby_giant_step import babygiantstep
from . import babygiantstep
from modarithmetic import chinese_remainder_theorem

def pohlig_hellman(g,h,p):
    '''
    Pohlig Hellman Algorithm:
    - currently only applicable to <g> = Fp
    '''
    n = p - 1 # order of group
    print('n=',n)

    # factor n
    n_factors = factor(n)
    print('n_factors=', n_factors)
    
    i = 0
    eqs  = []

    for i, f in enumerate(n_factors):
        q, e = f
        q, e = int(q), int(e)

        pi = int(pow(q,e))
        exp = int(n/pi)
        gi = pow(g, exp)
        hi = pow(h, exp)  
        print('--------------------')
        print(f'p{i}={pi}')
        print(f'exp{i}={exp}')
        print(f'g{i}={gi}')
        print(f'h{i}={hi}')

        # Solve the DLP: gi^yi = hi (mod p)
        yi = babygiantstep(p, gi, hi)
        print(f'y{i}={yi}')

        # Generate equation to solve using Chinese Remainder Theorem
        eqs.append((yi, pi))
        print(f'x{i}={yi} (mod {pi})')

    print('--------------------')
    # Knit together the smaller DLP solutions using the Chinese 
    # Remainder Theorem to get the actual solution

    x, m = chinese_remainder_theorem(eqs)
    print('x=', x)

    return x
