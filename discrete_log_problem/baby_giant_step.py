import math
import time
from modarithmetic import get_mod_inverse, xgcd

def babygiantstep(p,g,h, verbose=False, generate_all=False):
    start_time = time.time()

    # get the order m = p - 1
    N = int(math.ceil(math.sqrt(p - 1)))
    
    # get mod inverse of g
    g_inv = get_mod_inverse(g, p)

    # Compute g^−n
    g_inv_n = pow(g_inv, N, p)

    s = 1
    t = h

    # Use a dictionary/hash for the babystep array
    tbl = {}

    x = None

    if verbose:
        print('n=', N, 'g_inv=', g_inv,'g_inv_n=', g_inv_n)

    for i in range(N):
        
        # Save babystep {value => index}
        tbl[s] = i

        if verbose: print(f'i={i}, s={s}, t={t}')

        # Check if giantstep is in table
        if t in tbl:
            j = tbl[t]
            if verbose: print('found t=', t, 'i=', i, 'j=', j)
            x = i * N + j
            if not generate_all: break
        
        # Increment values
        s = s*g % p
        t = (t * g_inv_n) % p

    end_time = time.time()
    if verbose: print('Elapsed duration: ', int(end_time - start_time), 'seconds')

    # Return the discovered x
    if x:
        return x
    else:
        raise Exception('No discrete log found for g=%s, h=%s, p=%s' % (g, h, p))