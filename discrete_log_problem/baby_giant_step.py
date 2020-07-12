import math
import time
from modarithmetic import get_mod_inverse, xgcd

def babygiantstep(p,g,h, verbose=False, generate_all=False):
    start_time = time.time()

    # get the order m = p - 1
    N = int(math.ceil(math.sqrt(p - 1)))
    print('n=', N)
    
    # get mod inverse of g
    g_inv = get_mod_inverse(g, p)
    print('g_inv=', g_inv)

    # Compute g^−n
    g_inv_n = pow(g_inv, N, p)
    print('g_inv_n=', g_inv_n)

    s = 1
    t = h

    # Use a dictionary/hash for the babystep array
    tbl = {}

    x = None

    for i in range(N):
        
        # Save babystep {value => index}
        tbl[s] = i

        if verbose: print(f'i={i}, s={s}, t={t}')

        # Check if giantstep is in table
        if t in tbl:
            j = tbl[t]
            print('found t=', t, 'i=', i, 'j=', j)
            x = i * N + j
            print('x=',x)
            if not generate_all: break
        
        # Increment values
        s = s*g % p
        t = (t * g_inv_n) % p

    end_time = time.time()
    print('Elapsed duration: ', int(end_time - start_time), 'seconds')

    # Return the discovered x
    return x