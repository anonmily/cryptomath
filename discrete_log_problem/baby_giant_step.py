import math
import time
from modarithmetic import get_mod_inverse
from divisibility import xgcd

def babygiantstep(p,g,h):
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

    # Search for an equivalence in the table. Giant step.
    for i in range(N):
        
        # Save babystep {value => index}
        tbl[s] = i

        print('i=',i,'s=', s, 't=', t)

        # Check if giantstep is in table
        if t in tbl:
            j = tbl[t]
            print('found t=', t, 'i=', i, 'j=', j)
            x = i * N + j
            print('x=',x)
            break
        
        # Increment values
        s = s*g % p
        t = (t * g_inv_n) % p

    # Return the discovered x
    
    end_time = time.time()
    print('Elapsed duration: ', int(end_time - start_time), 'seconds')
    return x

if __name__ == "__main__":
    p = 200003000003
    g = 3
    A = 387420489
    B = 131128838694
    X = 'HNKFNOJXPQRASSUTRFQGTBKMLRZSJNVHIXYAGVKLLFXHFBGWWJHRJDDXXBJESDYHTFWTNOU'
    x = babygiantstep(p,g,A)
    assert( pow(g, x, p) == A )
    print(x)