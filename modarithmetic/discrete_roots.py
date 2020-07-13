import math
from sage.all import factor
from .modarithmetic import find_x_for_mod
from .chinese_remainder import chinese_remainder_theorem

def get_discrete_root(c, p, verbose=False):
    if p % 4 == 3:
        n = int((p+1)/4)
        b = pow(c, n, p)
        print(f'calc discrete root p % 4 === 4: n={n} b={b}')
    else:
        b = find_x_for_mod(lambda x: x**2, c=c, m=p, verbose=True)
        print(f'trial and error: b={b}')
    return (b, b*-1)

def get_composite_discrete_root(a,m):
    
    # Prime factorization of m
    m_factors = factor(m)   # returns [(base, exp), (base,exp)...]
    
    cr = []
    
    for m_factor in m_factors:

        p = m_factor[0]
        
        # Find x s.t. x^ = p
        y1, y2 = get_discrete_root(a,p)
        y1, y2 = int(y1), int(y2)

        factor_roots = ((y1, p),(y2, p))
        cr.append(factor_roots)
        
        y = y1 if y1 < y2 else y2

    roots = []
    n = len(cr)
    
    i = 0
    while i < math.ceil(n/2):
        factor_roots = cr[i]
        for j, froot in enumerate(factor_roots):
            k = 0
            while k < n:
                if k != i:
                    k_root = cr[k]
                    for other_root in k_root:
                        sys_eq = [ froot, other_root ] 
                        x, m = chinese_remainder_theorem(sys_eq)
                        roots.append(x)
                k = k + 1
        i = i + 1

    return roots