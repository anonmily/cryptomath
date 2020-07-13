import math
import time
from modarithmetic import get_mod_inverse, xgcd

def babygiantstep(p,g,h, use_element_order=False, verbose=False, generate_all=False):
    start_time = time.time()

    if not use_element_order:
        # get the order m = p - 1
        N = p - 1
    else:
        N = int(Mod(g,p).multiplicative_order())
     if verbose: print('N=',N)

    n = int(math.ceil(math.sqrt(N)))

    # get mod inverse of g
    g_inv = get_mod_inverse(g, p)

    # Compute g^−n
    g_inv_n = pow(g_inv, n, p)

    s = 1
    t = h

    # Use a dictionary/hash for the babystep array
    tbl = {}

    x = None

    if verbose:
        print('n=', N, 'g_inv=', g_inv,'g_inv_n=', g_inv_n)

    i = 0
    while i < n:

        # Save babystep {value => index}
        tbl[s] = i

        # print('i=%s, s=%s, t=%s' % (i,s,t))

        # Check if giantstep is in table
        if t in tbl:
            j = tbl[t]
            if verbose: print('found t=', t, 'i=', i, 'j=', j)
            x = i * n + j
            if not generate_all: break

        # Increment values
        s = s*g % p
        t = (t * g_inv_n) % p

        # Increment counter
        i = i + 1

    end_time = time.time()
    if verbose: print('Elapsed duration: ', int(end_time - start_time), 'seconds')

    # Return the discovered x
    if x:
        return x
    else:
        raise Exception('No discrete log found for g=%s, h=%s, p=%s' % (g, h, p))